from django.db import models

# Create your models here. ORM
class Student(models.Model):
    #Student(name, age, created_at, updated_at)
    name = models.CharField(max_length=10)
    age = models.IntegerField() #parameter로 안넣어줘도 되고 defalut=0이런거 지정가능
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)#변경이 생길때마다..

   # def __str__(self):
   #     return f'{self.id}번 학생의 이름: {self.name}  나이: {self.age} '

#Student : Comment = 1 : N
class Comment(models.Model):
    content  = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #관계를 형성하고자하는 모델명을 주로 사용
    #orm에서 제공하는 key 외래키
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

#1. 1번 학생(1) 가져오기
# student = Student.objects.get(pk=1)

#2.댓글(N) 생성
#comment = Comment()
#comment.content = 'First Comment'
#comment.student = student
#(comment.student_id = student.pk)
#comment.save()

#3.댓글(n)로 부터 학생(1) 불러오기
# comment.student #=> student 인스턴스자체
# comment.student.name #=> 학생 이름
# comment.student.age #=> 학생 나이
 
#4. 학생(1)으로부터 댓글(n) 불러오기
# student.comment_set.all() #=> comment QuerySet
