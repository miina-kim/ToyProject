from django.contrib import admin
from .models import Post # 게시글(Post) Model을 import
from .models import Question, Answer

# Register your models here.

# 제목으로 데이터 검색
class PostAdmin(admin.ModelAdmin):
    search_fields = ['postname']

# 관리자(admin)가 게시글(Post)에 접근 가능
admin.site.register(Post, PostAdmin)

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)

admin.site.register(Answer)
