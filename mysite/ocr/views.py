from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from PIL import Image
from pytesseract import pytesseract 
import pytesseract
import schedule
import time
import requests
from django.conf import settings
def index(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
 
        if form.is_valid():
            image = form.cleaned_data['text_Img']
            filename = 'bill.jpg'  # Desired filename
            image_path = os.path.join(settings.MEDIA_ROOT, filename)
            
            # Save the uploaded image with the desired filename
            with open(image_path, 'wb') as f:
                f.write(image.read())

            return redirect('choice')
    else:
        form = UploadForm()
    
    return render(request, 'index.html', {'form': form})

def choice(request):
    context = {
        'variable1' : 'Generate Result Now',
        'variable2' : 'Schedule the Result'
    }
    return render(request,'choice.html',context)

def setTimer(request):
    if request.method=="POST":
        setTimer = request.POST.get('setTimer')
        st = SetTimer(setTimer = setTimer)
        st.save()
        context={
            'variable' : setTimer
        }
        return render(request,'scd.html',context)
    return render( request, "setTime.html")
    
def convertor(request):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    print(pytesseract.get_languages(config=''))
    image_path = os.path.join('media', 'bill.jpg')
    img = Image.open(os.path.join(os.getcwd(), image_path))
    text = pytesseract.image_to_string(img)
    context = { 'variable' : text }
    return render(request,'result.html',context)

def scd(request):
    return render(request, 'result.html')