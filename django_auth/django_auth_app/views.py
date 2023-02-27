from django.shortcuts import render,redirect  
from django.contrib import messages  
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate

# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST.get("username").strip().lower()
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['data'] = {'name' : 'Roman', 'surname' : 'Safiullin', 'mail' : 'romsaaf@mail.ru', 'job':'Threat Intelligence engineer', 'linked':'https://www.linkedin.com/in/roman-safiullin-a09528252/', 'git':'https://github.com/Romsaaf', 'tg':'https://t.me/romsaaf', 'username':username}
            return redirect("profile")
        else:
            raise Exception()
    return render(request,"login.html")

def profile(request):  
 if request.user.is_authenticated:
    data = request.session['data']
    return render(request, "profile.html", data)
 else:
     return redirect("login")

def register(request):
    if request.method == "POST":
        username = request.POST.get("username").strip().lower()
        email = request.POST.get("email").strip().lower()
        password = request.POST.get("password")

        try:
            User.objects.create_user(username, email, password)
            messages.add_message(request, messages.INFO, 'Registration successful.')
            data = {'name' : 'Roman', 'surname' : 'Safiullin', 'mail' : 'romsaaf@mail.ru', 'job':'Threat Intelligence engineer', 'linked':'https://www.linkedin.com/in/roman-safiullin-a09528252/', 'git':'https://github.com/Romsaaf', 'tg':'https://t.me/romsaaf', 'username':username}
            return redirect("profile", data)
        except:
            messages.add_message(request, messages.INFO, 'Registration failed.')
            return redirect("register")
    return render(request,"register.html")