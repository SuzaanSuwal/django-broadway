from django.contrib.auth.models import User
from rest_framework import serializers
from crud.models import ClassRoom, UserProfile, Student




class ClassRoomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=5)
    
    
class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ["id", "name"]
        


        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "is_active", "username", "password"]
        extra_kwargs = {
            "password":{
                "write_only": True
            }
        }
    
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data) # User creation
        user.set_password(password) # hashed Password
        user.save()
        return user

class UserProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["id", "address", "phone", "user"]
    
    def get_fields(self):
        request = self.context.get("request")
        fields = super().get_fields()
        if request and request.method.lower() == "get":
            fields['user'] = UserSerializer()
        return fields
    
    
class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "address", "phone", "user"]
        