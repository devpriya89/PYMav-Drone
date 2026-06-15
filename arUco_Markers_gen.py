import cv2
import cv2.aruco as aruco
import os
folder = "markers"
os.makedirs(folder, exist_ok=True)
id = int(input("ArUco ID b/w 0-990: "))
aruco_dict = aruco.getPredefinedDictionary(
    aruco.DICT_6X6_1000
)
if 0 <= id < 1000:
    marker = aruco.generateImageMarker(
        aruco_dict,
        id,
        800
    )
    filename = os.path.join(
        folder,
        f"aruco_id_{id}.png"
    )
    cv2.imwrite(filename, marker)
    print(f"Saved: {filename}")
else:
    print("ID needs to be b/w 0 and 999")