# Hand Gesture Controlled LED System

*A real-time computer vision project using Python, MediaPipe, and Arduino.*
## Overview

This project allows users to control five LEDs using hand gestures captured through a computer webcam.

The system detects the number of raised fingers, processes the visual information using Python and MediaPipe, and transmits the detected finger count to an Arduino Uno through serial communication. The Arduino then illuminates the corresponding number of LEDs.

## How It Works

The system follows this workflow:

1. A webcam captures the user’s hand.
2. MediaPipe detects hand landmarks.
3. Python processes the landmarks and counts the raised fingers.
4. The detected finger count is transmitted to the Arduino through USB serial communication.
5. The Arduino receives the value and activates the corresponding LEDs.

## Technologies Used

### Software

* Python
* OpenCV
* MediaPipe
* PySerial
* C++ (Arduino)

### Hardware

* Arduino Uno
* Webcam
* 5 LEDs
* 5 current-limiting resistors
* Breadboard and jumper wires

## Project Structure
```text
HandGestureProject/
├── arduino/
│   └── led_testingfordetec_copy_20261031000130/
│       └── led_testingfordetec_copy_20261031000130.ino
├── python/
│   └── main.py
├── hand_landmarker.task
├── requirements.txt
└── README.md
```
## Installation

### Prerequisites

* Python 3
* Arduino IDE
* Arduino Uno
* Webcam

1. Clone the repository
git clone https://github.com/imene84/HandGestureProject.git
cd HandGestureProject

2. Create a virtual environment 
```bash
python3 -m venv venv
```
Activate it:

**macOS / Linux
```bash
source venv/bin/activate

**Windows**
```bash
venv\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure the Arduino

1. Open the Arduino sketch in the Arduino IDE.
2. Connect the Arduino Uno to your computer.
3. Select the correct board and serial port.
4. Upload the sketch.

### 5. Configure the serial port


Open `python/main.py` and locate the following line:

```python
arduino = serial.Serial('/dev/cu.usbmodem11201', 9600)
```
Replace `/dev/cu.usbmodem11201` with the serial port assigned to your Arduino.

**Note:** This port is specific to my Mac. Other users will need to replace it with their own Arduino serial port.

Open python/main.py and make sure the serial port matches the port assigned to your Arduino.

6. Run the Python application

From the project root:
```bash
python python/main.py
```

The webcam should open and begin detecting hand gestures.

Press q to exit.

## Current Features

* Real-time hand detection.
* Finger counting from 0 to 5.
* Serial communication between Python and Arduino.
* LED control based on detected finger count.
* Basic frame-stability filtering to reduce inconsistent readings.

## Future Improvements

* Improve gesture recognition accuracy.
* Replace blocking delays with non-blocking Arduino timing.
* Add more gesture-based controls.
* Improve the visual interface.
* Explore additional hardware integrations.

## Project Status

This project is a working prototype combining computer vision, Python programming, serial communication, and microcontroller-based hardware control.