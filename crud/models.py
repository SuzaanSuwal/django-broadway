from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.FileField(upload_to='profile_picture', null=True, blank=True)
    address = models.CharField(max_length=20)
    phone = models.CharField(max_length=14)
    
    def __str__(self):
        return f'profile of {self.user.username}'
    
    
class ClassRoom(models.Model):
        name = models.CharField(max_length=10)
        
        
class Student(models.Model):
        user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_students')  
        classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name="classroom_students")  
