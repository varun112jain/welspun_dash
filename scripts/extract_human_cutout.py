"""
Extracts human intruder cutout from green screen background.
"""
import os
import cv2
import numpy as np

img = cv2.imread("assets/human_intruder.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Green range
lower_green = np.array([35, 60, 60])
upper_green = np.array([85, 255, 255])

mask = cv2.inRange(hsv, lower_green, upper_green)
# Invert mask so person is 255 (white) and background is 0 (black)
person_mask = cv2.bitwise_not(mask)

# Clean up mask
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
person_mask = cv2.morphologyEx(person_mask, cv2.MORPH_CLOSE, kernel)
person_mask = cv2.GaussianBlur(person_mask, (3, 3), 0)

# Create RGBA image
b, g, r = cv2.split(img)
rgba = cv2.merge([b, g, r, person_mask])

# Find bounding box of person to crop tightly
pts = cv2.findNonZero(person_mask)
x, y, w, h = cv2.boundingRect(pts)
cropped_person = rgba[y:y+h, x:x+w]

cv2.imwrite("assets/human_intruder_transparent.png", cropped_person)
print(f"Extracted transparent human intruder cutout: {w}x{h} saved to assets/human_intruder_transparent.png")
