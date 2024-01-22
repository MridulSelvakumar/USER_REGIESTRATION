from django.shortcuts import render

# Create your views here.

from app.forms import *

def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
   # if request method=='POST' and request.files:

    d={'ufo1':ufo,'pfo1':pfo}
    return render(request,'register.html',d)
