from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, \
    DeleteView, DetailView
from django.urls import reverse_lazy

from crud.models import ClassRoom
from crud.forms import ClassRoomModelForm
from django.contrib.auth.models import User

class PortfolioView(TemplateView):
    template_name = 'myapp/portfolio.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Hello World"
        print(context)
        return context
    
    
    def get(self, request, *args, **kwargs):
        # code to update counter
        return super().get(request, *args, **kwargs)

@method_decorator(login_required, name="dispatch")  
class ClassRoomView(ListView):
    queryset = ClassRoom.objects.all()
    template_name = 'classbased/classroom.html'
    context_object_name = "classrooms"
    

class ClassRoomCreateView(CreateView):
    template_name = 'classbased/add_classroom.html'
    form_class = ClassRoomModelForm
    success_url = reverse_lazy('classbased_classroom')


class UpdateClassRoomView(UpdateView):
    queryset = ClassRoom.objects.all()
    form_class = ClassRoomModelForm
    template_name = "classbased/update_classroom.html"
    success_url = reverse_lazy("classbased_classroom")
    context_object_name = "classroom"
    
    
class DeleteClassRoomView(DeleteView):
    queryset = ClassRoom.objects.all()
    template_name = "classbased/delete_classroom.html"
    success_url = reverse_lazy("classbased_classroom")
    context_object_name = "classroom"
    
@method_decorator(login_required, name="get")  
class UserProfileView(DetailView):
    queryset = User.objects.all()
    template_name = "classbased/user_profile.html"
    context_object_name = "user"
    