# Lane Detection Project

This project implements a lane detection system using OpenCV and Python. It processes video frames to identify and highlight road lanes using computer vision techniques.

## Features
- **Grayscale Conversion**: Simplifies the image for better processing.
- **Gaussian Blur**: Reduces noise and smooths the image.
- **Canny Edge Detection**: Identifies sharp gradients (edges) in the video.
- **Region of Interest (ROI) Masking**: Focuses only on the road area, ignoring irrelevant parts like the sky.
- **Hough Transform**: Detects lines from the edge points to identify lane markers.
- **Video Processing**: Processes an entire video file and saves the result with highlighted lanes.

## Project Structure
- `main.py`: The core script that contains the lane detection logic and video processing loop.
- `.gitignore`: Configured to exclude large video files and virtual environments to keep the repository clean.
- `vi1.mp4`: Base video for lane detection (local).

## How to Run
1. Ensure you have Python and OpenCV installed (`pip install opencv-python numpy`).
2. Place your video file in the project directory.
3. Update the `video_filename` in `main.py` if needed.
4. Run the script:
   ```bash
   python main.py
   ```
5. The processed video will be saved as `vi1out.mp4` (or your specified output name) and displayed in a window.

## Techniques Used
- **OpenCV**: Standard library for computer vision tasks.
- **NumPy**: Used for efficient array operations and masking.
- **Hough Line Transform**: For robust line detection in images.
