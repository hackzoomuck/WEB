from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# def new(request):
#     if request.method == 'POST':
#         #데이터베이스에 데이터 생성(form class)
#         #1. 넘어온 데이터를 받기
#         article_form = ArticleForm(request.POST)
#         # title = request.POST.get('title')
#         # content = request.POST.get('content')
#         #2. 넘어온 데이터 검증(New)
#         if article_form.is_valid():
#             title = article_form.cleaned_data.get('title')
#             content = article_form.cleaned_data.get('content')
#             #3. 데이터베이스에 article 만들기!
#             article = Article.objects.create(title=title, content=content)
#             #4. redirect -> detail 
#             return redirect('articles:detail',article.pk)
#     else:
#         article_form = ArticleForm()
#         context={
#             'article_form':article_form,
#         }
#          return render(request, 'artlcles/new.html')

@login_required
def new(request):
    if request.method == 'POST':
        #데이터베이스에 데이터 생성(Model form)
        #1. 넘어온 데이터를 받기
        article_form = ArticleForm(request.POST)
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        #2. 넘어온 데이터 검증(New)
        if article_form.is_valid():
            #3. 데이터베이스에 article 만들기
            article = article_form.save(commit=False)
            #3-1. user정보 끼워 넣기
            article.user = request.user
            article.save()

            #4. redirect -> detail 
            return redirect('articles:detail',article.pk)
    else:
        article_form = ArticleForm()

    #폼을 보여줌 (유효성 검증 통과하지 못했을시에 원래로 돌아옴)   
    context={
        'article_form':article_form,
    }
    return render(request, 'articles/new.html', context)

def detail(request, pk):
    #1. pk번째 데이터를 가져오기
    article = Article.objects.get(pk=pk)
    #2. context로 넘겨주기
    context = {
        'article': article,
    }
    #3. render와 함께 html로 넘겨주기
    return render(request, 'articles/detail.html', context)

# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     if request.method = 'POST':
#         #Article 수정
#         #1. 넘어온 데이터받기
#         article_form = ArticleForm(request.POST)
#         #2. 데이터 검증
#         if article_form.is_vaild():
#             #3. 검증된 데이터로 수정 & 저장
#             article.title = article_form.cleaned_data.get('title')
#             article.content = article_form.cleaned_data.get('content')
#             article.save()
#             #4. redirect -> detail
#             return redirect('articles:detail',article.pk)
#     else:
#         #Article 수정하는 form 보여주기
#         article_form = ArticleForm(
#             {
#                 'title': article.title,
#                 'content': article.content,
#             }
#         )
#         context = {
#             'article_form':article_form,
#         }
#         return render(request, 'articles/new.html')

@login_required
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    # article의 주인인지 인증
    if request.user != article.user:
        return redirect('articles:index')
    if request.method == 'POST':
        #Article 수정
        #1. 넘어온 데이터받기 
        article_form = ArticleForm(request.POST, instance=article)
        #2. 데이터 검증
        if article_form.is_valid():
            #3. 검증된 데이터로 수정 & 저장
            article_form.save()
            #4. redirect -> detail
            return redirect('articles:detail',article.pk)
    else:
        #Article 수정하는 form 보여주기
        article_form = ArticleForm(instance=article)
    
    #이 세줄을 else에 넣지 않은 것은 
    # 1. else(곧 post요청이 아닐때), 
    # 2. 옳은 데이터가 아닐때 실행되는 데 
    # 2.가 실행 되었을 때 HttpRespons객체를 return 하지 못함.
    context = {
        'article_form':article_form,
    }
    return render(request, 'articles/new.html', context)
