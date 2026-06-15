from dronekit import connect, VehicleMode  # type: ignore[import]
import cv2
import cv2.aruco as aruco
import time
TAKEOFF_ID = 100
LAND_ID = 200
TAKEOFF_ALTITUDE = 5
vehicle = connect('/dev/ttyAMA0', baud=57600, wait_ready=True)
cap = cv2.VideoCapture(0)
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_1000)
detector = aruco.ArucoDetector(aruco_dict)
airborne = False
def arm_and_takeoff(target_altitude):
    print("Arming...")
    while not vehicle.is_armable:
        print("Waiting for vehicle...")
        time.sleep(1)
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
    while not vehicle.armed:
        time.sleep(1)
    print("Taking off...")
    vehicle.simple_takeoff(target_altitude)
    while True:
        alt = vehicle.location.global_relative_frame.alt
        print(f"Altitude: {alt:.1f} m")
        if alt >= target_altitude * 0.95:
            print("Target altitude reached")
            break
        time.sleep(1)
while True:
    ret, frame = cap.read()
    if not ret:
        continue
    corners, ids, _ = detector.detectMarkers(frame)
    if ids is not None:
        for marker_id in ids.flatten():
            print("Detected:", marker_id)
            if marker_id == TAKEOFF_ID and not airborne:
                print("TAKEOFF MARKER FOUND")
                arm_and_takeoff(TAKEOFF_ALTITUDE)
                airborne = True
            elif marker_id == LAND_ID and airborne:
                print("LAND MARKER FOUND")
                vehicle.mode = VehicleMode("LAND")
                airborne = False
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
vehicle.close()
cv2.destroyAllWindows()