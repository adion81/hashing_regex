from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.

def index(request):
    return render(request,'index.html')


def register(request):
    if request.method == "POST":
        errors = User.objects.register_validator(request.POST)
        user = User.objects.filter(email=request.POST['email'])
        if len(user) > 0:
            messages.error(request,"Email already taken")
            return redirect('/')

        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('/')
        else:
            hash1 = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()).decode()
            User.objects.create(email=request.POST['email'],password=hash1)
            logged = User.objects.last()
            request.session['user_id'] = logged.id
            return redirect('/')
    else:
        return redirect('/')
