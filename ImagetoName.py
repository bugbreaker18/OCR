# We import the necessary packages
#import the needed packages
import cv2
import os,argparse
import pytesseract
from PIL import Image
 
#We then Construct an Argument Parser
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",
                required=True,
                help="Path to the image folder")
ap.add_argument("-p","--pre_processor",
                default="thresh",
                help="the preprocessor usage")
args=vars(ap.parse_args())
 
#We then read the image with text
images=cv2.imread(args["image"])
 
#convert to grayscale image
gray=cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
 
#checking whether thresh or blur
if args["pre_processor"]=="thresh":
    cv2.threshold(gray, 0,255,cv2.THRESH_BINARY| cv2.THRESH_OTSU)[1]
if args["pre_processor"]=="blur":
    cv2.medianBlur(gray, 3)
     
#memory usage with image i.e. adding image to memory
filename = "{}.jpg".format(os.getpid())
cv2.imwrite(filename, gray)
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)
 
# show the output images
cv2.imshow("Image Input", images)
cv2.imshow("Output In Grayscale", gray)
cv2.waitKey(0)


# import pytesseract
# from PIL import Image

# # Path to the Tesseract executable (change this to your Tesseract installation path)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# def preprocess_image(image):
#     # You can add image preprocessing steps here
#     # For example, resizing, grayscale conversion, thresholding, noise reduction, etc.
#     # For demonstration purposes, let's just convert the image to grayscale
#     return image.convert('L')

# def extract_name_from_text(text):
#     words = text.split()
#     if words:
#         generated_name = words[0]
#     else:
#         generated_name = "Unknown"
#     return generated_name

# def main():
#     # Load an image using PIL (Python Imaging Library)
#     image_path = 'path_to_your_image.png'
#     image = Image.open(image_path)

#     # Preprocess the image
#     preprocessed_image = preprocess_image(image)

#     # Use pytesseract to extract text from the preprocessed image
#     extracted_text = pytesseract.image_to_string(preprocessed_image, lang='eng')

#     # You can process the extracted text to generate a name
#     generated_name = extract_name_from_text(extracted_text)

#     print("Generated Name:", generated_name)

#     # Save the extracted text to a file
#     with open('extracted_text.txt', 'w') as f:
#         f.write(extracted_text)

# if __name__ == "__main__":
#     main()
