import cv2
import cv2.aruco as aruco
cap = cv2.VideoCapture(0)
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
detect = aruco.ArucoDetector(aruco_dict)
while True:
    ret, frame = cap.read()
    if not ret:
        continue
    corners, ids, rejected = detect.detectMarkers(frame)
    if ids is not None:
        aruco.drawDetectedMarkers(frame, corners, ids)
        for marker_id in ids.flatten():
            print("Detected ID:", marker_id)
    cv2.imshow("ArUco Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()