from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from .models import ClassRoom


def signup(request):
    print(request.method)
    if request.method == "POST":
        username = request.POST.get("username")
        fn = request.POST.get("first_name")
        ln = request.POST.get("last_name")
        email = request.POST.get("email")
        pw1 = request.POST.get('password1')
        pw2 = request.POST.get('password2')
        
        if pw1 != pw2:
            messages.error(request, "Password didn't match!!")
            return redirect('signup')
        user = User.objects.create(username=username,first_name=fn, last_name=ln, email=email, is_active=True)
        user.set_password(pw1)
        user.save()
        messages.success(request, "User created succesfully!!")
        return redirect('signup')
         # This is handling a get request    
    return render(request, template_name="crud/signup.html")


def user_login(request):
    if request.method == "POST":
        un = request.POST.get("username")
        pw = request.POST.get("password")
        user = authenticate(username=un, password=pw)
        if not user:
            messages.error(request, "Couldn't login with provided credentials !!")
            return redirect("user_login")
        login(request, user)
        messages.success(request, "User logged in succesfully !!")
        return redirect('crud_classroom')
    return render(request, template_name="crud/login.html")
    
        

@login_required
def classroom(request):
    classrooms = ClassRoom.objects.all()
    return render(request, template_name="crud/classroom.html", context={"classrooms": classrooms})


def user_logout(request):
    logout(request)
    return redirect('root_page')
    
    
def add_classroom(request):
    if request.method == "POST":
        classname = request.POST.get("name")
        ClassRoom.objects.create(name=classname)
        return redirect('crud_classroom')
    return render(request, template_name='crud/add_classroom.html')


def update_classroom(request, id):
    c = ClassRoom.objects.get(id=id)
    if request.method == "POST":
        c.name = request.POST.get("name")
        c.save()
        return redirect('crud_classroom')
    return render(request, template_name="crud/update_classroom.html", context={"classroom": c})


def delete_classroom(request, id):
    c = ClassRoom.objects.get(id=id)
    if request.method == "POST":
        c.delete()
        return redirect("crud_classroom")
    return render(request, template_name="crud/delete_classroom.html", context={"classroom": c})