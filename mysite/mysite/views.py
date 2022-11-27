from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from wscubetech.models import feature
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
def index(request):
    return render(request,"index.html")
def login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('/')
        else:
            messages.info(request, f'account done not exit plz sign in')
            return redirect('login')
    else:
        return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        repeatPassword = request.POST['repeatPassword']
        if password==repeatPassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,"€mail already exist")
                return redirect("register")
            elif User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                return redirect("register")
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password is not same')
            return redirect("register")
    else:          
        return render(request,"register.html")
    def logout(request):
        logout(request)
        return redirect('register')