from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all() #자료형 queryset
    context = {
        'articles' : articles,
    }
    return render(request, 'articles.index.html',context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title= request.GET.get('title')
    content=request.GET.get('content')

    #새로운 글을 쓰는 부분, article에는 뭐가 들어갈까? 게시글인스턴스
    # article.title
    # article.content
    article = Article.object.create(title=title, content=content)


    context={
        'title':title,
        'content':content,
    }
    return render(request, 'articles/create.html',context)