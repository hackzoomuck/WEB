from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def signup(request):
    #로그인 유뮤 판별 & 로그인 된 경우 redirect
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        #실제 회원 생성
        #1.넘어온 데이터를 Form Class에 입력하기
        form = UserCreationForm(request.POST)
        #2.유효한 값인지 검증
        if form.is_valid():
            #3.회원생성!
            user = form.save()
            #3-1.로그인!
            auth_login(request, user)
            #4. redirect -> 메인페이지 (articles index)
            return redirect('articles:index')

    else:
        #회원 가입 양식 보여줌
        form = UserCreationForm()


    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    #로그인 유뮤 판별 & 로그인 된 경우 redirect
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        #로그인
        #1. post 요청으로 넘어돈 데이터를 FORM에 입력
        form = AuthenticationForm(request, request.POST)
        #2. 검증
        if form.is_valid():
            #3. 로그인 수행
            auth_login(request, form.get_user())
            #4. redirect -> 메인 페이지(articles index)
            #4-1. next 값 가져오기
            next = request.GET.get('next')
            #값이 존재하면 앞의 것이 실행 
            #none이면 뒤의 것으로 redirect
            return redirect(next or 'articles:index')
    else:
        #로그인 창 보여줌
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html',context)

def logout(request):
    #logout logic
    if request.method == 'POST':
        #로그아웃 수행
        auth_logout(request)
        return redirect('articles:index')

def edit(request):
    if request.method == 'POST':
        #회원 정보 수정
        #1.POST로 넘어온 데이터 FORM에 입력
        form = CustomUserChangeForm(request.POST,instance=request.user)
        #2.검증
        if form.is_valid():
            #3.저장
            form.save()
            #4.redirect -> 메인 (articles.index)
            return redirect('articles:index')
    else:
        #회원 정보 수정 Form 보여줌
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/edit.html',context)

#post요청만 받음
def delete(request):
    if request.method == 'POST':
        #USER 삭제
        request.user.delete()
        return redirect('articles:index')

def password(request):
    if request.method == 'POST':
        #실제로 비밀번호 변경
        #1. 넘어온 데이터 form에 입력
        form = PasswordChangeForm(request.user, request.POST)
        #2. 검증
        if form.is_valid():
            #3. 비밀번호 저장
            user = form.save()
            #3-1. 세션 유지
            update_session_auth_hash(request, user)
            #4. redirect -> 메인 페이지
            return redirect('articles:index')
    else:
    #현재 유저의 비밀번호를 변경해야하기에 파라미터넣어줘야함.
    #비밀번호를 변경하는 양식 보여줌
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/password.html', context)