from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('-id') #자료형 queryset
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html',context)

def new(request):
    return render(request, 'articles/new.html')

def create(request): #post 요청을 받음
    #넘어온 데이터 받기
    #이유2번 - POST(http body)라는 것을 통해 넘어옴
    #title=request.GET.get('title')
    #content=request.GET.get('content')
    title=request.POST.get('title')
    content=request.POST.get('content')

    #새로운 글을 쓰는 부분, article에는 뭐가 들어갈까? 게시글인스턴스
    # article.title
    # article.content
    article = Article.objects.create(title=title, content=content)

    #return render(request, 'articles/create.html',context)
    #다른 곳으로 요청을 한다. 다른 곳으로 연결을 한다. get요청을 받는 페이지로 돌려 보내야함.
    return redirect(f'/articles/{article.pk}/')

def detail(request, pk): #parameter 적어줘야함.
    #1개만 찾아 올 것임.
    #Article.objects.get(id=pk)
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request,'articles/detail.html',context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('/articles/')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, '/articles/edit.html', context)

def update(request, pk):
    #1. pk에 해당하는 article 가져오기
    article = Article.objects.get(pk=pk)
    #2. update로 데이터를 넘기는 것.
    title = request.POST.get('title')
    content = request.POST.get('content')

    #3. edit로부터 넘어온 데이터 가져오기
    article.title=title
    article.content=content
    article.save()

    return redirect(f'/articles/{article.pk}/') #detail페이지로 리다이렉트

     