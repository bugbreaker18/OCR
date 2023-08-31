# After R.CNN and Yolo, try to read the contents of the plate
from django.contrib import admin
from django.urls import path
from ocr_app.views import ocr

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ocr/', ocr, name='ocr'),
]
from django.shortcuts import render
from PIL import Image
import pytesseract

def ocr(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['image']
        image = Image.open(uploaded_file)
        text = pytesseract.image_to_string(image)
        return render(request, 'ocr_app/result.html', {'text': text})
    return render(request, 'ocr_app/index.html')
