from rest_framework import serializers
from crud.models import ClassRoom



class ClassRoomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=5)
    
    
class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ["id", "name"]
        
        
    
    