from django import forms
from .models import Article


class ArticleForm(forms.ModelForm): #특정 모델을 위한 폼
    class Meta: #mata라는 class의 의미 => class에 대한 정보가 담긴 class
        model = Article
        fields = ['title','content',]
# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=10,
#         label='제목',
#         widget=forms.TextInput(
#             attrs={
#                 'class':'title', #class="title"
#                 'placeholder':'제목을 입력하세요.', #placeholder="제목을 입력하세요"

#             }
#         )
#     )
#     content = forms.CharField(
#         label = "내용",
#         widget = forms.Textarea(
#             attrs={
#                 'class': 'content',
#                 'rows': 5,
#                 'cols': 10,
#                 'placeholder': '내용을 입력하세요.',
#             }
#         )
#     )



#Form Class의 용도
#1. Form tag 만들기
#2. DATABASE에 DATA 생성하기 위한 틀 제공   