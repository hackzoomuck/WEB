from django.db import models

# Create your models here.
class Article(models.Model):
    #3개의 colum 'title, content, created_at
    #id = models.AutoField(priary_key=True)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #데이터가 생긴 시간 옵션
    updated_at = models.DateTimeField(auto_now=True)#수정될때마다 시간추가

    def __str__(self): #매직 매서드(특수 목적 메소드)/스트링으로 리턴해야함.
        return f'{self.id}번 글 - {self.title} : {self.content}'
    # str(article), print(article),


    #1. models.py 작성/수정
    #2. 명령어 python manage.py makemigrations 
    #=> models.py 바탕으로 설계도 생성
    #3. python manage.py  migrate
    #=> 실제 DB(db.sqlite3)에 설계도를 적용

    #DB에 데이터를 생성하는 방법 3가지
    #1. article=Article()
    #   article.title='첫번째'
    #   article.content='내용'
    #   article.save()

    #생성자를 이용해서 (models.Model이 들고 있음)
    #2. article2=Article(title='2',content='_2_')
    #   article2.save()

    #3. article3 = 

    #READ
    #1. All - Article.objects.all() #여러개 나옴(queryset), 복수(쿼리스트링)
    
    #2. 1개 - Article.objects.get(id=1) get쓸때는 id로 검색하자.
    #get은 id가 무슨값인지, 단수(인스턴스) 
    #1)unique한 colum로 된 것으로 하는 것이 좋음.
    #2)not null인 컬럼으로 한다.
    
    #3. 조건 - Article.objects.filter(title='세번째') #복수로 리턴됨.
    # WHERE

    #4-1. QuerySet + .first(), .last() #단수
    #4-2. .order_by() 가져온 데이터를 정렬 할 수 있음.
    #   Article.objects.all().order_by('title') #오름차순
    #   Article.objects.all().order_by('-title') #내림차순
    #4-3. offset, limit (OFFSET, LIMIT) [offset:offset+limit]
    #   Article.objects.all()[1:2] #=> [2] [1:3] =>[2, 3]

    #UPDATE 수정하고자하는 데이터가 있어야함.
    #값을 할당하고 DB에 반영해줘야함. 
    #1.데이터를 가져오기: a = Article.objects.get(id=1)
    #2.수정할 값 할당하기: a.title='first!'
    #3.저장하기 (db에 반영하기): a.save()

    #DELETE
    #1. 데이터 가져오기 - a = Article.objects.get(id=1)
    #2. 삭제하기 (DB에 반영) - a.delete()
    