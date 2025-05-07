from django.shortcuts import render, redirect
from django.contrib import messages, auth

from django.contrib.auth.models import User


def login(request):
    if request.method == "POST":
        # get user values
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You logged in successfully')
            return redirect(dashboard)
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, "accounts/login.html")


def register(request):
    # Register User
    if request.method == 'POST':
        
        # get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        # check password match
        if password == password2:
            # username check
            if User.objects.filter(username=username).exists():
                messages.error(request, 'the username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'the email you entered is being used')
                    return redirect('register')
                else:
                    # looks good
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,email=email, password=password)
                    user.save()
                    messages.success(request, 'You are registered and can login')
                    return redirect('login')
        else:
            messages.error(request, 'passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def dashboard(request):
    return render(request, "accounts/dashboard.html")


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You logged out')
        return redirect('index')
        
        
    
