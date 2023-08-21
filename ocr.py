import cv2
import pytesseract

# Set the path to your Tesseract executable (change accordingly)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_image(image_path):
    try:
        # Load the image using OpenCV
        image = cv2.imread(image_path)
        
        # Preprocess the image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(blurred, 30, 150)
        
        # Find contours in the edged image
        contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        
        for contour in contours:
            # Approximate the contour
            epsilon = 0.05 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            
            if len(approx) == 4:
                # Extract the ROI
                x, y, w, h = cv2.boundingRect(approx)
                roi = gray[y:y + h, x:x + w]
                text = pytesseract.image_to_string(roi)
                
                return text, approx
        
    except Exception as e:
        print("Error:", str(e))
        return None, None

if __name__ == "__main__":
    image_path = "path_to_your_image.jpg"  # Change this to the path of your image
    extracted_text, contour = ocr_image(image_path)
    
    if extracted_text:
        print("Extracted Text:")
        print(extracted_text)
        
        # Save the extracted text to a text file
        with open("extracted_text.txt", "w") as text_file:
            text_file.write(extracted_text)
        
        # Display the original image with the detected contour
        image = cv2.imread(image_path)
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
        cv2.imshow("Image with Contour", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    else:
        print("Text extraction failed.")
