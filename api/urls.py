from django.urls import path
from .views import home, HomeView, StudentAPIView, StudentListAPIView, SimpleClassRoomView


urlpatterns = [
    path("home/", home),
    path("cb-apiview/", HomeView.as_view()),
    path("student-apiview/", StudentAPIView.as_view()),
    path("student-list-apiview/", StudentListAPIView.as_view()),
    path("simple-classroom/", SimpleClassRoomView.as_view())
]