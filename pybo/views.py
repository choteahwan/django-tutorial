# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator

def index(request):
    """
    pybo 목록 출력
    """
    # 입력인자
    page = request.GET.get('page', '1') # 페이지

    # 조회
    question_list = Question.objects.order_by('-create_date')

    # 페이징 처리
    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여 주기
    page_obj = paginator.get_page(page) 

    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)
    
    #render 함수란?? 쉽게 생각하면 html 화면을 띄운다.
    #render(request, template_name, context=None, content_type=None, status=None, using=None)
    #render 매개변수 request, template_name는 필수!
    # 매개변수 
    # request == 동일하게 그냥 request로 작성
    # template_name == .html 불러오고 싶은 html 파일

    #redirect 함수란?? 
    #redirect(to, permanent=False, *args, **kwargs)
    # 매개변수
    # to == 어느 URL로 이동할지 정하게 된다. 상대url, 절대url 모두 가능
    # urls.py path 함수의 name을 정의 ===> pname='index'

    # render와 redirect 차이는..
    # render는 템플릿을 불러오는 것 
    # redirect는 url을 이동하는 것
    
def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    """
    pybo 답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question':question, 'form':form}
    return render(request, 'pybo/question_detail.html', context)
    
def question_create(request):
    """
    pybo 질문 등록
    """
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form':form}
    return render(request, 'pybo/question_form.html', context)
    
