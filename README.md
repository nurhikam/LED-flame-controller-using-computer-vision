# LED-flame-controller-using-computer-vision

This is an Arduino-based project that utilizes computer vision techniques to control the flickering of an LED to simulate a flame effect. The position of a colored object detected by the camera is mapped to the flickering pattern of the LED.

## How it Works
- An OpenCV Python script running on the computer detects a specific colored object from the video stream and determines its coordinates.
- The x,y position of the object is serially communicated to an Arduino Uno board.
- The Arduino uses this coordinate data to control the flickering of an LED light connected to it, fading the LED when the object moves away from the center and brightening it when the object approaches the center.
- This creates a reactive flame-like flickering effect controlled by the position of the colored object in view of the webcam.

## Hardware Required
- Arduino Uno
- USB Webcam
- LED light
- 220 ohm resistor
- Jumper wires

## Software Required
- Visual Studio Code
- Python (OpenCV)
- Arduino IDE

# How to Use
- Install OpenCV and setup webcam access in Python
- Upload the Arduino code to the Uno
- Run the Python script to detect object and send data to Arduino
- Position the colored object to control the LED flickering

## Future Improvements
- Add more LEDs for a fuller flame effect
- Control brightness of multiple zones for better flame simulation
- Experiment with different color objects and flame colors

This project demonstrates how computer vision can be used to creatively interact with physical hardware and create interesting IoT applications. Potential use cases could include interactive installations, visual effects, or immersive environments.

## Explanatory Video
https://drive.google.com/file/d/1yI5MF-KmZtKJbgD_z4UIU2Cq07_pNG0E/view?usp=sharing
