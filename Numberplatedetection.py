import cv2

# Load the image
image_path = 'path_to_your_image.jpg'
image = cv2.imread(image_path)

# Load the pre-trained Haarcascades for license plate detection
plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')

# Detect license plates in the image
plates = plate_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(25, 25))

# Loop through detected plates and save them as separate images
for i, (x, y, w, h) in enumerate(plates):
    plate_image = image[y:y+h, x:x+w]
    plate_image_path = f'plate_{i+1}.jpg'
    cv2.imwrite(plate_image_path, plate_image)

print(f'{len(plates)} license plates detected and saved!')

