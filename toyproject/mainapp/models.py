from django.db import models

# Create your models here.
# 게시글(Post) 클래스 - 제목(postname), 내용(contents)
# 일반적으로 models.py를 수정했다면 바로 migrate 해서 db에 저장
class Post(models.Model):
    postname = models.CharField(max_length=50)
    mainphoto = models.ImageField(blank=True, null=True) # blank=True : don't need input/ null=True : Nullable in db
    contents = models.TextField()

    # 게시글의 제목(postname)이 Post object 대신하기
    def __str__(self):
        return self.postname