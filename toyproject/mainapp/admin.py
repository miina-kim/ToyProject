from django.contrib import admin
from .models import Post # 게시글(Post) Model을 import

# Register your models here.
# 관리자(admin)가 게시글(Post)에 접근 가능
admin.site.register(Post)