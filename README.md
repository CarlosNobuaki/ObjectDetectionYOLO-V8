# Object Detection using UltraLytics YOLO-V8

This repository contains code for performing object detection using UltraLytics YOLO-V8, a powerful and efficient object detection model. Whether you want to detect objects in images or videos, this project provides easy-to-use Python scripts to get you started.

## Prerequisites

Before you begin, make sure you have the following dependencies installed:

- Python 3
- OpenCV
- NumPy
- UltraLytics

You can install these packages using `pip`:

```bash
pip install opencv-python numpy ultralytics
```
# Usage
## Detect Objects in a Video

To run object detection on a video, execute the following command:

```bash
python3 yolo_n_opencv.py
```
This script uses the YOLO-V8 model with the pre-trained weights from yolov8n.pt to detect objects in the video stream.


## Detect Objects in an Image
To run object detection on an image, use the following command:

```bash
python3 yoloBasic.py
```
This script loads the YOLO-V8 model with the pre-trained weights and applies object detection to the specified image.


## Dataset
The labels for object detection are defined in coco.txt. This file contains the classes that the YOLO-V8 model can detect.

Feel free to replace coco.txt with your custom dataset if needed.

### I used the pre-trained model yolov8n.pt (pytorch)

