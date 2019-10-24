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
    return render(request, 'index.html', context)

def dinner(request):
    foods = ['초밥', '카레', '등갈비']
    pick = random.choice(foods)
    context = {
        'pick': pick,
    }
    return render(request, 'dinner.html', context)


#Variable Routing
def hello(request, name):#urls.py의 변수 이름이랑 같아야함.
    context = {
        'name': name, 
    }
    return render(request, 'hello.html', context)

#실습
#1. '이름'과 '나이'를 Variable Routing을 통해 받아서 자기소개
def hello_intro(request, name, age):
    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'hello_intro.html', context)

#2. 숫자 2개를 Variable Routing을 통해 받아 곱셈 결과 보여주기
def mul(request, x, y):
    context = {
        'x':x,
        'y':y,
        'z':x*y,
    }
    return render(request, 'mul.html', context)

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
    return render(request, 'dtl.html',context)

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
    return render(request, 'birthday.html', context)



    return redner(request, 'birthday.html')
