from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.
# index.html 페이지를 부르는 index 함수
def index(request):
    return render(request, 'mainapp/index.html')
    # return HttpResponse("Hello, world!")

def blog(request):
    postlist = Post.objects.all()
    return render(request, 'mainapp/blog.html', {'postlist':postlist})