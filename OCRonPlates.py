# After R.CNN and Yolo, try to read the contents of the plate
from django.contrib import admin
from django.urls import path
from ocr_app.views import ocr

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ocr/', ocr, name='ocr'),
]
