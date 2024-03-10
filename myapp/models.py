from django.db import models


class ClassRoom(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name='classroom_students')

    def __str__(self):
        return self.name




