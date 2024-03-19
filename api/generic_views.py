from django.urls import path
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, UpdateAPIView, \
    RetrieveUpdateDestroyAPIView

from rest_framework.viewsets import ModelViewSet
from crud.models import ClassRoom, UserProfile

from .serializers import ClassRoomModelSerializer, UserProfileModelSerializer


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
    serializer_class = ClassRoomModelSerializer
    queryset = UserProfile.objects.all()