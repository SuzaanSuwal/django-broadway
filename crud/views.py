from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def signup(request):
    print(request.method)
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get("username")
        fn = request.POST.get("first_name")
        ln = request.POST.get("last_name")
        email = request.POST.get("email")
        pw1 = request.POST.get("password1")
        pw2 = request.POST.get("password2")
        
        if pw1 != pw2:
            messages.error(request, "Password didn't match!!")
            return redirect('signup')
        user = User.objects.create(username=username,first_name=fn, last_name=ln, email=email, is_active=True)
        user.set_password(pw1)
        user.save()
        messages.success(request, "user created succesfully!!")
        return redirect('signup')
            
    return render(request, template_name="crud/signup.html")

def user_login(request):
    return render(request, template_name="crud/login.html")


def classroom(request):
    return render(request, template_name='crud/classroom.html')
