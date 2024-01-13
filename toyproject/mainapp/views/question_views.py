from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question

@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user # author 속성에 로그인 계정 저장
            question.create_date = timezone.now()
            question.save()
            return redirect('mainapp:qna_main')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'mainapp/qna_question.html', context)

@login_required(login_url='common:login')
def question_modify(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('mainapp:qna_detail', pk=question.id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.save()
            return redirect('mainapp:qna_detail', pk=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form':form}
    return render(request, 'mainapp/qna_question.html', context)

@login_required(login_url='common:login')
def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('mainapp:question_detail', pk=question.id)
    question.delete()
    return redirect('mainapp:qna_main')

@login_required(login_url='common:login')
def question_vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 질문은 추천할 수 없습니다.')
    else:
        question.voter.add(request.user)
    return redirect('mainapp:qna_detail', pk=question.id)