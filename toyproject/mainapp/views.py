from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .models import Question, Answer
from .forms import QuestionForm
from django.core.paginator import Paginator

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

def qna_main(request):
    page = request.GET.get('page', '1') # 페이지 값 가져오기 (default=1)
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    return render(request, 'mainapp/qna_main.html', {'question_list':page_obj})

def qna_detail(request, pk):
    question = get_object_or_404(Question, pk=pk) # Post.objects.filter(), Post.objects.get()
    return render(request, 'mainapp/qna_detail.html', {'question':question})    

def answer_create(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('mainapp:qna_detail', pk=pk)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('mainapp:qna_main')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'mainapp/qna_question.html', context)