from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid details")
            return redirect('login')
    else:
        return render(request,'login.html')
def register(request):
    if request.method=="POST":
        firstname = request.POST['first_Name']
        lastname = request.POST['last_Name']
        username = request.POST['username']
        email = request.POST['email']
        psw1 = request.POST['psw1']
        psw2 = request.POST['psw2']
        if psw1 == psw2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(password=psw1,first_name=firstname,last_name=lastname,username=username,email=email)
                user.save();
                print("User created")
        else:
             print("Password is not matched")
             return redirect('register')
        return redirect('/')
    else:

        return render(request,"registration.html")

def logout(request):
    auth.logout(request)
    return redirect('/')