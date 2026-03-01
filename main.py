import cv2
import numpy as np
import os

# --- Step 1: Define the "Brain" of the project ---
# This function finds the lines in a single image frame
def process_frame(frame):
    # Get the size of the video
    height = frame.shape[0]
    width = frame.shape[1]
    
    # A. Turn it Gray (Color is distracting for computers)
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # B. Blur it slightly (Removes rough texture of the road)
    blur_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    
    # C. Canny Edge Detection (Finds sharp changes in color/white lines)
    canny_image = cv2.Canny(blur_image, 50, 150)
    
    # D. Masking (Focus ONLY on the road in front, ignore the sky)
    region_of_interest_vertices = [
        (0, height),
        (width / 2, height / 2 + 60), 
        (width, height)
    ]
    
    mask = np.zeros_like(canny_image)   
    cv2.fillPoly(mask, np.array([region_of_interest_vertices], np.int32), 255)
    cropped_image = cv2.bitwise_and(canny_image, mask)
    
    # E. Hough Transform (Connect the dots to draw lines)
    lines = cv2.HoughLinesP(
        cropped_image,
        rho=2,
        theta=np.pi/180,
        threshold=100,
        lines=np.array([]),
        minLineLength=40,
        maxLineGap=100
    )
    
    # F. Draw the lines on the original video frame
    line_img = np.zeros_like(frame)
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_img, (x1, y1), (x2, y2), [0, 255, 0], 3)
                
    # Combine the lines with the original video
    final_image = cv2.addWeighted(frame, 0.8, line_img, 1.0, 0.0)
    return final_image

# --- Step 2: Run the Video ---
video_filename = 'vi1.mp4'         # Make sure this matches your file name!
output_filename = 'vi1out.mp4'    # <--- FIXED: Changed .mp5 to .mp4

if not os.path.exists(video_filename):
    print(f"❌ ERROR: I cannot find '{video_filename}'. Make sure it is in the folder!")
else:
    print(f"✅ Found video. Processing and saving to '{output_filename}'...")
    
    cap = cv2.VideoCapture(video_filename) 
    
    # Setup the Video Writer to save the file
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    out = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break # Video is finished
            
        try:
            # 1. Detect Lines
            processed_frame = process_frame(frame)
            
            # 2. Save to file
            out.write(processed_frame)
            
            # 3. Show on screen
            cv2.imshow('Lane Detection Project', processed_frame)
            
        except Exception as e:
            print(f"Error: {e}")
            break
        
        # Press 'q' to stop early
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"🎉 DONE! Your project video is saved as: {output_filename}")