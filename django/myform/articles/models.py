from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #1:n(USER:ARTICLES)
    #어떤 모델과 관계할것인지.
    user= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

