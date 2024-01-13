from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import AnswerForm
from ..models import Question, Answer

@login_required(login_url='common:login')
def answer_create(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('{}#answer_{}'.format(resolve_url('mainapp:qna_detail', pk=question.id), answer.id))
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'mainapp/qna_detail.html', {'question':question})   

@login_required(login_url='common:login')
def answer_modify(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('mainapp:qna_detail', pk=answer.question.id)
    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('{}#answer_{}'.format(resolve_url('mainapp:qna_detail', pk=answer.question.id), answer.id))
    else:
        form = AnswerForm(instance=answer)
    context = {'answer':answer, 'form':form}
    return render(request, 'mainapp/qna_answer.html', context)

@login_required(login_url='common:login')
def answer_delete(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다.')
    else:
        answer.delete()
    return redirect('mainapp:qna_detail', pk=answer.question.id)

@login_required(login_url='common:login')
def answer_vote(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 답변은 추천할 수 없습니다.')
    else:
        answer.voter.add(request.user)
    return redirect('{}#answer_{}'.format(resolve_url('mainapp:qna_detail', pk=answer.question.id), answer.id))