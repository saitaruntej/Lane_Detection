# 🚗 Lane Detection and Turn Prediction

This project focuses on detecting road lanes — both straight and curved — using classical computer vision techniques. The goal is to simulate a simplified Lane Departure Warning System, similar to what is used in self-driving cars.

Instead of relying on deep learning, this solution uses mathematical concepts like homography, polynomial curve fitting, Hough Transform, perspective warping, and curvature estimation to understand lane structure and predict vehicle turns.

## 🌟 Features
- **Straight Lane Detection**: Detects solid and dashed lines on straight roads.
- **Curve Lane Detection**: Handles curved roads using bird's-eye view transformations.
- **Turn Prediction**: Calculates the radius of curvature and predicts the direction of the turn (Left, Right, or Straight).
- **Video Processing**: Processes input video files and generates annotated output videos.

## 🛠 Project Structure
- `code/`: Contains the Python scripts for lane detection.
  - `straight_lane_detection.py`: Implementation for straight roads.
  - `curved_lane_detection.py`: Implementation for curved roads and turn prediction.
- `data/`: Input video files.
  - `straight_lane.mp4`: Original straight road video.
  - `curved_lane.mp4`: Original curved road video.
  - `solidWhiteRight.mp4`: New sample from Udacity project.
- `results/`: Directory where processed output videos are saved.
- `gif/`: Contains demonstration animations.

## 📋 Requirements
- Python 3.8+
- OpenCV (`opencv-python`)
- NumPy

## 🚀 Getting Started

### 1. Installation
Clone the repository and install the dependencies:
```bash
pip install opencv-python numpy
```

### 2. Running the Code
To run the lane detection on straight roads:
```bash
python code/straight_lane_detection.py
```

To run the lane detection on curved roads:
```bash
python code/curved_lane_detection.py
```

## 🔍 Implementation Pipeline

### Straight Lane Detection
1. **Region of Interest**: Apply a mask to focus only on the road area.
2. **Hough Transform**: Identify line segments in the filtered image.
3. **Line Filtering**: Distinguish between solid and dashed lanes based on slope and length.
4. **Line Averaging**: Compute the mean slope and intercepts to draw continuous lane lines.

### Curve Lane Detection & Turn Prediction
1. **Perspective Wrap**: Apply Homography to get a bird's-eye view of the road.
2. **Color Masking**: Use HSV thresholding to isolate white and yellow lane markings.
3. **Curve Fitting**: Fit a second-order polynomial to the detected lane pixels.
4. **Curvature Calculation**: Compute the radius of curvature from the polynomial coefficients.
5. **Turn Prediction**: Determine turn direction based on the curve's leading coefficient.

## 📊 Results
![Curved Lane Detection](gif/curved_lane_detection.gif)

## ⚖️ License
This project is licensed under the MIT License.
