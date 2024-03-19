from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.views import Response

from crud.models import ClassRoom, Student, User, UserProfile
from .serializers import ClassRoomSerializer, ClassRoomModelSerializer

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
    
    
class SimpleClassRoomListView(APIView):
    def get(self, *args, **kwargs):
        classrooms = ClassRoom.objects.all()
        response = []
        for classroom in classrooms:
            response.append({
                "id": classroom.id,
                "name": classroom.name
            })
        return Response(response)
    
    def post(self, *args, **kwargs):
        data = self.request.data
        name = data.get("name")
        classroom, _ = ClassRoom.objects.get_or_create(name=name)
        return Response({
            "message": "Success",
            "id": classroom.id,
            "name": classroom.name
        })
        
        
class ClassRoomRetrieveView(APIView):
    def get(self, *args, **kwargs):
        id = kwargs.get("id")
        try:
            classroom = ClassRoom.objects.get(id=id)
        except ClassRoom.DoesNotExist:
            return Response({
                "detail": "Not Found"
            })
        serializer = ClassRoomSerializer(classroom)
        return Response(serializer.data)
    
class ClassRoomView(APIView):
    def get(self, *args, **kwargs):
        queryset = ClassRoom.objects.all()
        # serializer = ClassRoomSerializer(queryset, many=True)
        serializer = ClassRoomSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
    # def post(self, *args, **kwargs):
    #     data = self.request.data
    #     serializer = ClassRoomSerializer(data=data) # Deserialization
    #     if serializer.is_valid():
    #         name = serializer.validated_data["name"]
    #         classroom = ClassRoom.objects.get_or_create(name=name)
    #         return Response({
    #             "message": "Success",
    #             "id": classroom.id,
    #             "name": classroom.name
    #         })
    #     else:
    #         return Response(serializer.errors)
        
        
    def post(self, *args, **kwargs):
        
        serializer = ClassRoomSerializer(data=data) # Deserialization
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
        
class ClassRoomUpdateDeleteView(APIView):
    def patch(self, *args, **kwargs):
        serializer = ClassRoomModelSerializer(data=self.request.data)
        if serializer.is_valid():
            name = serializer.validated_data["name"]
            classroom = ClassRoom.objects.get(id=kwargs["id"])
            classroom.name = name
            classroom.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        
        
    def delete(self, *args, **kwargs):
        id = kwargs.get("id")
        classroom = ClassRoom.objects.get(id=id)
        classroom.delete()
        return Response({
            "message": "ClassRoom deleted succesfully!"
        })
 
 
       