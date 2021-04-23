from django.db import models
# 모델이란? sql 디비의 정보들을 하나의 덩어리로 만들어서 views.py 쪽으로 보내고,
# views.py에서 .html 쪽으로 정보를 보내주고, if or for 문으로 정보들을 뿌려준다.

# 다시 정리하면, 웹브라우저 url => config/urls.py => pybo/urls.py => views.py (자바에서 컨트롤러의 역할)
#                                                                 =>   models.py (db)                      => xxx.html => 웹브라우저에서 보여지게 됨

class Question(models.Model):
    subject = models.CharField(max_length=200) # 글제목은 200자까지
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

