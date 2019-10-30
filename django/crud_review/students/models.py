from django.db import models

# Create your models here.
class Student(models.Model):
    #Student(name, age, created_at, updated_at)
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번 학생의 이름: {self.name}  나이: {self.age} '