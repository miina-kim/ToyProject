from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
# index.html 페이지를 부르는 index 함수
def index(request):
    return render(request, 'mainapp/index.html')
    # return HttpResponse("Hello, world!")

def blog(request):
    postlist = Post.objects.all()
    return render(request, 'mainapp/blog.html', {'postlist':postlist})

# blog의 게시글(posting)을 부르는 posting 함수
def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
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
    return render(request, 'mainapp/new_post.html') # 글쓰기 버튼 클릭 시

def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'mainapp/remove_post.html', {'Post': post})

# 영화 : 로그인 
def movie_login(request):
    return render(request, 'mainapp/movie_login.html')