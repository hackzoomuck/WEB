from django.contrib import admin
from .models import Student, Comment
# Register your models here.

class CommentInline(admin.StackedInline):
    model = Comment

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'created_at', 
    'updated_at')
    inlines = [
        CommentInline,
    ]
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'content', 'created_at', 
#     'updated_at')
admin.site.register(Student,StudentAdmin) #두번째 인자: 커스터마이징한 studentadmin으로 관리할 것
# admin.site.register(Comment)
