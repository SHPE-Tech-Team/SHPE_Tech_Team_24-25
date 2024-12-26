import cv2
import numpy as np
import pytesseract

# loading the image
image = cv2.imread(
    "/Users/laflame/SHPE TECH TEAM AI/AI_Loteria_24-25/loteria_dataset/IMG_5564.jpeg"
)
height, width = image.shape[:2]
bottom_fraction = 0.2
crop_bottom = int(height * 0.12)
crop_left = int(width * 0.15)
crop_right = int(width * 0.15)

# cropping image
cropped = image[
    int(height * (1 - bottom_fraction)) : height - crop_bottom,
    crop_left : width - crop_right,
]

# Enhanced preprocessing
gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
denoised = cv2.bilateralFilter(gray, 9, 75, 75)

# Enhance contrast
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
enhanced = clahe.apply(denoised)

# Otsu's thresholding
_, thresh = cv2.threshold(enhanced, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Modified OCR configuration
custom_config = r'--oem 3 --psm 7 -c preserve_interword_spaces=1 -c tessedit_char_whitelist="ABCDEFGHIJKLMNOPQRSTUVWXYZ " -c tosp_min_sane_kn_sp=0.1'
text = pytesseract.image_to_string(thresh, config=custom_config)
print(text)

# Display
cv2.imshow("Cropped", cropped)
cv2.imshow("Enhanced", enhanced)
cv2.imshow("Threshold", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
