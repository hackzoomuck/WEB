from django.db import models

# Create your models here. ORM
class Student(models.Model):
    #Student(name, age, created_at, updated_at)
    name = models.CharField(max_length=10)
    age = models.IntegerField() #parameter로 안넣어줘도 되고 defalut=0이런거 지정가능
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)#변경이 생길때마다..

    def __str__(self):
        return f'{self.id}번 학생의 이름: {self.name}  나이: {self.age} '