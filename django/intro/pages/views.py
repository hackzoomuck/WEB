from django.shortcuts import render #미리 render import해놓음.
import random
# Create your views here.
#하나의 페이지, request라 적은 이유는 사용자가 요청을 보낸다. 사용자가 보낸 요청이 request라는 parameter로 넘어옴.
def index(request): 

    context = {
        'name': 'leejieun94',
    }
    #넘어온 요청을 render로 다시 넘겨 줘야함. dict으로 넘겨줌. 3번째 인자 하나만 넘겨줄 수 있음.
    #context 변수를 사용해서 dict 넘겨줌. 
    #1개의 dict만 넘겨줌.
    return render(request, 'pages/index.html', context)

def dinner(request):
    foods = ['초밥', '카레', '등갈비']
    pick = random.choice(foods)
    context = {
        'pick': pick,
    }
    return render(request, 'pages/dinner.html', context)


#Variable Routing
def hello(request, name):#urls.py의 변수 이름이랑 같아야함.
    context = {
        'name': name, 
    }
    return render(request, 'pages/hello.html', context)

#실습
#1. '이름'과 '나이'를 Variable Routing을 통해 받아서 자기소개
def hello_intro(request, name, age):
    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'pages/hello_intro.html', context)

#2. 숫자 2개를 Variable Routing을 통해 받아 곱셈 결과 보여주기
def mul(request, x, y):
    context = {
        'x':x,
        'y':y,
        'z':x*y,
    }
    return render(request, 'pages/mul.html', context)

from datetime import datetime

def dtl(request):
    #template 으로 데이터 넘기고자함.
    foods = ['짜장면','냉면','라면','짬뽕']
    my_sentence = 'life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow =datetime.now()
    empty_list = []

    context = {
        'foods' : foods,
        'my_sentence' : my_sentence,
        'messages' : messages,
        'datetimenow' : datetimenow,
        'empty_list' : empty_list,
    }
    return render(request, 'pages/dtl.html',context)

#[실습]
# IS it your birthday
# 오늘이 자신의 생일이면 '예'를 아니면 '아니오'를 보여주는 페이지
def birthday(request):
    today = datetime.now()

    #if today.month == 3 and today.day == 8:
    #    result = True
    #else:
    #    reslut = false

    result = (today.month == 3 and today.day == 8)

    context ={
        'result' : result,
    }
    return render(request, 'pages/birthday.html', context)



   # return render(request, 'birthday.html')


def throw(request):
    return render(request,'pages/throw.html')
    
def catch(request): #url.py의 catch먼저 만나고 views.catch의 함수 호출
   #request.GET #=> {'message':'안녕', 'messge2':'잘가'} dcitionary 키를 가지고 값을 가져옴
    message = request.GET.get('message') #=> '안녕'
    message2 = request.GET.get('message2') #=> '잘가!'
    context = {
        'message' : message,
        'message2' : message2,
    }
    return render(request,'pages/catch.html', context)

# [실습] 로또 번호 생성기
# 사용자로부터 번호 몇개를 생성할지를 입력받고,
# 그 갯수 만큼 로또 번호를 보여주기
# ex) 5 -> 5줄의 로또 번호 세트

#urls -> views -> template
def lotto_throw(request):
    return render(request,'pages/lotto_throw.html')
def lotto_catch(request):
    m_lo = request.GET.get('m_lo') 
    #get을 통해서 받으면 문자로 받게 됨. 
    my_lottos = []
    ran_num = range(1,45)
    for i in range(int(m_lo)):
        my_lottos.append(random.sample(ran_num, 6))

    context={
        'my_lottos': my_lottos,
        'm_lo':m_lo,
    }
    return render(request, 'pages/lotto_catch.html',context)

#GET & POST requset
def article_new(request):
    return render(request, 'pages/article_new.html')

def article_create(request):
    #request.GET #=> {'title': 제목입니다, 'content':내용입니다,}
    title = request.POST.get('title') #=> '제목입니다'
    content = request.POST.get('content') #=>'내용입니다.'

    context ={
        'title': title,
        'content': content,
    }
    return render(request, 'pages/article_create.html', context)

#Static Files
#Images, css, html 통틀어 이야기하는 자원 or 파일
#html 단독 -> 파일과 같은 폴더에 넣고, 상대 경로
#{% load static %} 통해서 이미지 파일 가져올 수 있음. 폴더 만들어서 이미지 넣기 안됨, 장고에서는.
#이미지, static filed pages => static 폴더 만들기 이름 바꾸면 안됨.
def static_example(request):
    return render(request, 'pages/static_example.html')