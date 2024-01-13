from django.db import models
from django.contrib.auth.models import User

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
    
# Q&A 페이지 모델
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question') # 특정 사용자가 작성한 질문 접근 : userkey.author_question.all()
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True) # 수정한 경우에만 생성되는 데이터이므로, 값이 없어도 됨.
    voter = models.ManyToManyField(User, related_name='voter_question') # 추천인/ # 특정 사용자가 추천한 질문 접근 : userkey.voter_question.all()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True) # 수정한 경우에만 생성되는 데이터이므로, 값이 없어도 됨.
    voter=models.ManyToManyField(User, related_name='voter_answer')