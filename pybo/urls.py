from django.urls import path
from . import views

app_name='pybo'

urlpatterns = [
    path('', views.index, name='index'), # pybo/ 게시판 리스트 
    path('<int:question_id>/', views.detail, name='detail'), # detail/ 게시판 글보기
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'), # answer/create/ 답변달기?
    path('question/create/', views.question_create, name='question_create'), # question/create/ 게시판 글쓰기
]