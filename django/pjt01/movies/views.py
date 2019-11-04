from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    #db에서 모든 인스턴스 가져오기
    #1. 모든 movies 가져오기
    movies = Movie.objects.all()

    #2. context 생성
    context = {
        'movies': movies,
    }

    #2. context와 함께 render하기
    return render(request, 'movies/index.html', context)


def new(request):
    if request.method == 'POST':
    #db의 create(request라는 변수에 다 들음)
        title = request.POST.get('title')
        title_en = request.POST.get('title_en')
        audience = request.POST.get('audience')
        open_date = request.POST.get('open_date')
        genre = request.POST.get('genre')
        watch_grade = request.POST.get('watch_grade')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster_url')
        description = request.POST.get('description')

        movie = Moive.objects.create(
            title=title,
            title_en=title_en,
            audience=audience,
            open_date=open_date,
            genre=genre,
            watch_grade=watch_grade,
            score=score,
            poster_url=poster_url,
            description=description
        )

        return redirect('movide:detail', movie.pk)

    else:
        return render(request, 'movies/new.html')

def detail(request, pk):
    Moive.objects.get(pk=pk)
    context={
        'movie':movie,
    }
    return render(request, 'movies/detail.html')

def edit(request, pk): #수정하는 걸 보여주는 페이지랑, 수정하는 페이지
    movie=Movie.objects.get(pk=pk)

    if request.method =='POST':
        title = request.POST.get('title')
        title_en = request.POST.get('title_en')
        audience = request.POST.get('audience')
        open_date = request.POST.get('open_date')
        genre = request.POST.get('genre')
        watch_grade = request.POST.get('watch_grade')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster_url')
        description = request.POST.get('description')

        movie.title=title
        movie.title_en=title_en
        movie.audience=audience
        movie.open_date=open_date
        movie.genre=genre
        movie.watch_grade=watch_grade
        movie.title=title
        movie.score=score
        movie.poster_url=poster_url
        movie.description=description
        movie.save()

        return redirect('movies:detail',movie.pk)

    else :
        context ={
            'movie':movie,
        }
    return render(request,'movies/edit.html',context)


def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')