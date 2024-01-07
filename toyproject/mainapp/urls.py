from django.contrib import admin
from django.urls import path
from mainapp.views import * # from .views import *

# 이미지 업로드
from django.conf.urls.static import static
from django.conf import settings

app_name='mainapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    # 웹사이트의 첫화면은 index 페이지이다 + URL이름은 index (별칭)
    path('', index, name='index'),
    # URL:80/blog에 접속하면 blog 페이지 + URL이름은 blog 
    path('blog/', blog, name='blog'),
    # URL:80/blog/숫자로 접속하면 게시글-세부페이지(posting)
    path('blog/<int:pk>/', posting, name="posting"),
    # 글쓰기 페이지 추가
    path('blog/new_post/', new_post),
    # 삭제 페이지 추가
    path('blog/<int:pk>/remove/', remove_post),
    
    # 영화_로그인 페이지 추가
    path('movie_login/', movie_login, name='movie_login'),

    # Q&A 페이지 추가 
    path('qna_main/', qna_main, name='qna_main'),
    path('qna_main/<int:pk>/', qna_detail, name='qna_detail'),
    path('qna_main/answer/create/<int:pk>/', answer_create, name='answer_create'),
    path('qna_main/question/create/', question_create, name='question_create')
]

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)