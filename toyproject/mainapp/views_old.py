from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .models import Question, Answer
from django.http import HttpResponseNotAllowed
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
# index.html 페이지를 부르는 index 함수
def index(request):
    return render(request, 'mainapp/index.html')
    # return HttpResponse("Hello, world!")

def blog(request):
    postlist = Post.objects.all() # Post.objects : Post 모델의 데이터 조회
    return render(request, 'mainapp/blog.html', {'postlist':postlist})

# blog의 게시글(posting)을 부르는 posting 함수
def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = get_object_or_404(Post, pk=pk) # Post.objects.filter(), Post.objects.get()
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'mainapp/posting.html', {'post':post})

def new_post(request):
    if request.method == 'POST':
        if request.POST['mainphoto']: 
            new_article=Post.objects.create( # Post 모델 생성
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        else:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        return redirect('/blog/')
    return render(request, 'mainapp/new_post.html') # 글쓰기 버튼 클릭 시 (링크를 통해 페이지를 요청할 경우에는 무조건 GET 방식)

def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'mainapp/remove_post.html', {'Post': post})

# 영화 : 로그인 
def movie_login(request):
    return render(request, 'mainapp/movie_login.html')

# def qna_main(request):
#     page = request.GET.get('page', '1') # 페이지 값 가져오기 (default=1)
#     question_list = Question.objects.order_by('-create_date')
#     paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기
#     page_obj = paginator.get_page(page)
#     return render(request, 'mainapp/qna_main.html', {'question_list':page_obj})

# def qna_detail(request, pk):
#     question = get_object_or_404(Question, pk=pk) # Post.objects.filter(), Post.objects.get()
#     return render(request, 'mainapp/qna_detail.html', {'question':question})    

# @login_required(login_url='common:login')
# def question_create(request):
#     if request.method == 'POST':
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             question = form.save(commit=False)
#             question.author = request.user # author 속성에 로그인 계정 저장
#             question.create_date = timezone.now()
#             question.save()
#             return redirect('mainapp:qna_main')
#     else:
#         form = QuestionForm()
#     context = {'form': form}
#     return render(request, 'mainapp/qna_question.html', context)

# @login_required(login_url='common:login')
# def question_modify(request, pk):
#     question = get_object_or_404(Question, pk=pk)
#     if request.user != question.author:
#         messages.error(request, '수정권한이 없습니다.')
#         return redirect('mainapp:qna_detail', pk=question.id)
#     if request.method == 'POST':
#         form = QuestionForm(request.POST, instance=question)
#         if form.is_valid():
#             question = form.save(commit=False)
#             question.modify_date = timezone.now()
#             question.save()
#             return redirect('mainapp:qna_detail', pk=question.id)
#     else:
#         form = QuestionForm(instance=question)
#     context = {'form':form}
#     return render(request, 'mainapp/qna_question.html', context)

# @login_required(login_url='common:login')
# def question_delete(request, pk):
#     question = get_object_or_404(Question, pk=pk)
#     if request.user != question.author:
#         messages.error(request, '삭제권한이 없습니다.')
#         return redirect('mainapp:question_detail', pk=question.id)
#     question.delete()
#     return redirect('mainapp:qna_main')


# @login_required(login_url='common:login')
# def answer_create(request, pk):
#     question = get_object_or_404(Question, pk=pk)
#     if request.method == 'POST':
#         form = AnswerForm(request.POST)
#         if form.is_valid():
#             answer = form.save(commit=False)
#             answer.author = request.user  # author 속성에 로그인 계정 저장
#             answer.create_date = timezone.now()
#             answer.question = question
#             answer.save()
#             return redirect('mainapp:qna_detail', pk=question.id)
#     else:
#         form = AnswerForm()
#     context = {'question': question, 'form': form}
#     return render(request, 'mainapp/qna_detail.html', {'question':question})   

# @login_required(login_url='common:login')
# def answer_modify(request, pk):
#     answer = get_object_or_404(Answer, pk=pk)
#     if request.user != answer.author:
#         messages.error(request, '수정권한이 없습니다.')
#         return redirect('mainapp:qna_detail', pk=answer.question.id)
#     if request.method == 'POST':
#         form = AnswerForm(request.POST, instance=answer)
#         if form.is_valid():
#             answer = form.save(commit=False)
#             answer.modify_date = timezone.now()
#             answer.save()
#             return redirect('mainapp:qna_detail', pk=answer.question.id)
#     else:
#         form = AnswerForm(instance=answer)
#     context = {'answer':answer, 'form':form}
#     return render(request, 'mainapp/qna_answer.html', context)

# @login_required(login_url='common:login')
# def answer_delete(request, pk):
#     answer = get_object_or_404(Answer, pk=pk)
#     if request.user != answer.author:
#         messages.error(request, '삭제권한이 없습니다.')
#     else:
#         answer.delete()
#     return redirect('mainapp:qna_detail', pk=answer.question.id)