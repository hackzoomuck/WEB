# CRUD REVIEW

1.APP 등록
2.언어 & 시간대 설정
3.urls 파일 분리
4.template 폴더 구조 정리
5.base.html 설정
    1)base.html생성
    {% block body %}
    {% endblock %}
    2)settings.py>templates>dir(장고 프로젝트에게 알려주기)
            os.path.join(BASE_DIR, 'crud_review', 'templates'),
            os마다 다를 수 있기에. 
            # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

6.models.py 모델 생성
- Student(name, age, created_at, updated_at)
# 1.python manage.py makemigrations //db의 table을 생성하기 위한 설계도 생성
# 2.python manage.py migrate //설계도 가지고 실제 db에 테이블을 생성
7.CRUD
urls.py 에 views.py import하기 
#
-CREATE(new, create) 
//new.html에서 데이터를 받아서 create.html에서 student에 데이터 저장
//post로 요청을 받기에 return redirect()를 함. (render()는 흐름상 자연스럽지 않음.)
//db저장하는 코드.
//1. post 요청으로 넘어온 데이터 가져오기(name(html에서 뒤의 것),age)
//2. db에 저장(orm을 사용) , 모델 클래스를 이용해서 db에 저장.
//from .models import Student(Student라는 클래스를 import해옴.)
//student = Student(name=name, age=age)
//student.save()
//return redirect(f'/students/{student.pk}/')
//3. 생성된 학생의 상세 정보를 보는 페이지로 이용(Detail)

-READ(index, detail)
-Delete(delete)
//POST 요청만을 받음 -> redirect()
//1.pk에 해당하는 student를 db에서 가져오기
//2.student 삭제(DB에서 삭제하기)
//3.index 페이지로 이동
-Update(edit,update)