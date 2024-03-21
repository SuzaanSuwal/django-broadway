from django.contrib.auth.models import User
from django.urls import path
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, UpdateAPIView, \
    RetrieveUpdateDestroyAPIView

from rest_framework.viewsets import ModelViewSet
from crud.models import ClassRoom, UserProfile

from .serializers import ClassRoomModelSerializer, UserProfileModelSerializer, UserSerializer, StudentModelSerializer


class ClassRoomGenericView(ListAPIView):
    serializer_class = ClassRoomModelSerializer
    queryset = ClassRoom.objects.all()
    
    

class ClassRoomGenericCreateView(CreateAPIView):
    serializer_class = ClassRoomModelSerializer
    queryset = ClassRoom.objects.all()
    
class ClassRoomListCreateView(ListCreateAPIView):
    serializer_class = ClassRoomModelSerializer
    queryset = ClassRoom.objects.all()
    
class ClassRoomUpdateView(UpdateAPIView):
    serializer_class = ClassRoomModelSerializer
    queryset = ClassRoom.objects.all()
      
    
class ClassRoomRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = ClassRoomModelSerializer
    queryset = ClassRoom.objects.all()
    
    
    
class CLassRoomViewSet(ModelViewSet):
    serializer_class = ClassRoomModelSerializer
    queryset = ClassRoom.objects.all()
    
    
class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileModelSerializer
    queryset = UserProfile.objects.all()
    
    
class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all() 
    
class StudentViewSet(ModelViewSet):
    serializer_class = StudentModelSerializer
    queryset = User.objects.all() 
    