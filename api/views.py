from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.views import Response

from crud.models import ClassRoom, Student, User, UserProfile

def home(request):
    return JsonResponse({
        "message": "I am learning APIs"
    })
    
class HomeView(APIView):
    def get(self, *args, **kwargs):
        return Response({
            "message": "This is from classbased APIview" 
        })
        
class StudentAPIView(APIView):
    def get(self, *args, **kwargs):
        return Response({
            "name" : "Jon",
            "age" : 30,
            "address": "KTM",
            "email": "jon@email.com"
        })      
        
class StudentListAPIView(APIView):
    def get(self, *args, **kwargs):
        student = [
    {"name": "Jon", "email": "jon@email.com", "address": "KTM", "age": 30},
    {"name": "Jane", "email": "jane@email.com", "address": "KTM", "age": 24},
    {"name": "Alex", "email": "alex@email.com", "address": "KTM", "age": 21},
    {"name": "Hary", "email": "hary@email.com", "address": "KTM", "age": 25},
]
        return Response(student)
        


class SimpleClassRoomView(APIView):
    def get(self, *args, **kwargs):
        classroom = ClassRoom.objects.get(id=1)
        response = {
            "id": classroom.id,
            "name": classroom.name
        }
        return Response(response)
    
    