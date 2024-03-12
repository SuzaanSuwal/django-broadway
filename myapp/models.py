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


class Publication(models.Model):
    title = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title
    

class Article(models.Model):
    headline = models.CharField(max_length=20)
    publication = models.ManyToManyField(Publication)
    
    def __str__(self):
        return self.headline
