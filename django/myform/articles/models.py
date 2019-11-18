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
    # article을 작성한 user -> article.user
    # user가 작성한 모든 article -> user.article_set.all()
    # M:N [LIKE] - USER:ARTICLE
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    # article에 좋아요 누른 모든 user -> article.like_users.all()
    # user가 좋아요 누른 모든 article ->user.article_set.all()
    #-> user.like_article.all()