import cv2
import numpy as np

def detect_color(image_path):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    colors = {
        "red": ([136, 87, 111], [180, 255, 255]),
        "green": ([25, 52, 72], [102, 255, 255]),
        "blue": ([94, 80, 2], [120, 255, 255])
    }

    for color_name, (lower_bound, upper_bound) in colors.items():
        lower_bound = np.array(lower_bound, dtype=np.uint8)
        upper_bound = np.array(upper_bound, dtype=np.uint8)

        mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
        filtered_image = cv2.bitwise_and(image, image, mask=mask)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        if contours:
             x, y, w, h = cv2.boundingRect(contours[0])
             cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
             cv2.putText(image, color_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Color Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
img=input("Path to your image(in jpg):")
detect_color(img)