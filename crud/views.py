from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from .models import ClassRoom, Student, UserProfile
from .forms import ClassRoomForm, ClassRoomModelForm


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

def crud_student(request):
    students = Student.objects.all()
    return render(request, template_name='crud/student.html', context={'students': students})


def add_student(request):
    if request.method == "POST":
        profile_id = request.POST.get('profile_id')
        classroom_id = request.POST.get('classroom_id')
        Student.objects.get_or_create(user_id=profile_id, classroom_id=classroom_id)
        return redirect('crud_student')
    profiles = UserProfile.objects.all()
    classrooms = ClassRoom.objects.all()
    return render(request, template_name='crud/add_student.html', context={"profiles": profiles, "classrooms": classrooms})

@login_required
def user_profile(request):
    user = request.user
    return render(request, template_name="crud/user_profile.html", context={"user": user})


@login_required
def update_profile(request):
    user = request.user
    if request.method == "POST":
        user.first_name = request.POST.get("fn")
        user.last_name = request.POST.get("ln")
        user.save()
        
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        up, _ = UserProfile.objects.update_or_create(user=user, defaults={"address": address, "phone": phone})
        
        pp = request.FILES.get("pp")
        print(pp)
        if pp:
            up.profile_picture = pp
            up.save()
        
        return redirect("user_profile")
    return render(request, template_name="crud/update_profile.html", context={"user": user})



def form_classroom(request):
    if request.method == "POST":
        # form = ClassRoomForm(request.POST)
        form = ClassRoomModelForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data.get("name")
            # ClassRoom.objects.create(name=name)
            form.save()
            return redirect('crud_classroom')
            
    # form = ClassRoomForm()      
    form = ClassRoomModelForm()
    return render(request, template_name="crud/form_classroom.html", context={"form": form})

