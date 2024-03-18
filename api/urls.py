from django.urls import path
from .views import home, HomeView, StudentAPIView, StudentListAPIView, SimpleClassRoomView, SimpleClassRoomListView, \
    ClassRoomRetrieveView, ClassRoomView, ClassRoomUpdateDeleteView
    


urlpatterns = [
    path("home/", home),
    path("cb-apiview/", HomeView.as_view()),
    path("student-apiview/", StudentAPIView.as_view()),
    path("student-list-apiview/", StudentListAPIView.as_view()),
    path("simple-classroom/", SimpleClassRoomView.as_view()),
    path("simple-classroom-list/", SimpleClassRoomListView.as_view()),
    
    path("classroom/<int:id>/", ClassRoomRetrieveView.as_view()),
    path("classroom-update-delete/<int:id>/", ClassRoomUpdateDeleteView.as_view()),
    path("classroom/", ClassRoomView.as_view())
]