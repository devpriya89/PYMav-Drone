# PYMav-Drone
ArUco Marker Controlled Drone is a Rpi based autonomous drone system that uses computer vision and MAVLink communication to detect ArUco markers and trigger actions such as takeoff and landing

Autonomous_Drone_Project/
│
├── markers/
│   ├── aruco_id_100.png
│
├── ArUco_ID_Detector.py
├── arUco_Markers_gen.py
├── Autonomous_drone.py
├── Check_Arming.py
├── Py_FC_Connection.py
└── README.md

**#File Descriptions**
| File Name            | Purpose                                                                |
| ---------------------| ---------------------------------------------------------------------- |
| arUco_Markers_gen.py | Generates custom ArUco markers and saves them in the markers folder    |
| ArUco_ID_Detector.py | Detects ArUco markers and displays/prints their IDs                    |
| Py_FC_Connection.py  | Tests MAVLink communication between Raspberry Pi and Flight Controller |
| Check_Arming.py      | Verifies whether the Raspberry Pi can arm the flight controller        |
| Autonomous_drone.py  | Main autonomous flight program                                         |
| markers/             | Stores all generated ArUco marker images                               |
| README.md            | Project documentation                                                  |

**#Python Dependencies**

Install the required Python packages before running the project.

pip3 install opencv-contrib-python pymavlink numpy

Verify Installation
python3 -c "import cv2, numpy, pymavlink; print('Installation Successful')"

Expected Output:
Installation Successful

# Configuration Guide

## 1. Marker Generator Configuration
File:
generate_marker.py

### Change the ArUco Dictionary
Default:

aruco.DICT_6X6_1000
Available options:
aruco.DICT_4X4_50
aruco.DICT_4X4_100
aruco.DICT_4X4_250
aruco.DICT_4X4_1000
aruco.DICT_5X5_1000
aruco.DICT_6X6_1000
aruco.DICT_7X7_1000


### Change Marker Size
MARKER_SIZE = 800
Larger values create higher resolution markers.

### Change Save Folder
folder = "markers"
All generated markers will be stored in this folder.

## 2. Marker Detection Configuration

File:
detect_marker.py
### Camera Selection
Default camera:
python
cap = cv2.VideoCapture(0)


Examples:
cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(1)
cap = cv2.VideoCapture(2)


### Detection Dictionary
Must match the generator:
python
aruco.DICT_6X6_1000
If the generator uses a different dictionary, detection will fail.


## 3. MAVLink Configuration
File:
mavlink_control.py


### Serial Port
Raspberry Pi UART:
CONNECTION_STRING = "/dev/ttyAMA0"

USB connection:
CONNECTION_STRING = "/dev/ttyUSB0"

Alternative USB:
CONNECTION_STRING = "/dev/ttyACM0"


### Baud Rate
Examples:
BAUD = 57600
BAUD = 115200
BAUD = 921600

Must match the flight controller serial configuration

## 4. Takeoff Marker Configuration

Change the marker ID that triggers takeoff:
TAKEOFF_ID = 100
Example:
TAKEOFF_ID = 15

When marker 15 is detected, the drone will take off

## 5. Landing Marker Configuration

Change the marker ID that triggers landing:
LAND_ID = 200

Example:
LAND_ID = 25

When marker 25 is detected, the drone will land

## 6. Takeoff Altitude

Set desired altitude:
TAKEOFF_ALTITUDE = 5

Examples:
TAKEOFF_ALTITUDE = 2
TAKEOFF_ALTITUDE = 5
TAKEOFF_ALTITUDE = 10

Units are meters

## 7. Marker Confirmation Frames
To prevent false detections:
TAKEOFF_CONFIRM = 20
LAND_CONFIRM = 20

Meaning:
The marker must be visible for 20 consecutive frames before an action is executed

Examples:

TAKEOFF_CONFIRM = 10
LAND_CONFIRM = 10

or

TAKEOFF_CONFIRM = 30
LAND_CONFIRM = 30

## 8. Camera Resolution

Optional:
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

Examples:
python
640x480
1280x720
1920x1080

Higher resolution improves detection distance

Quick Setup Checklist: 



**Camera connected:**

MAVLink connection verified
Correct serial port selected
Correct baud rate selected
Marker generated
Marker detection verified
Props removed for testing
Arm test passed
Takeoff test passed
Landing test passed
Flight test completed safely
