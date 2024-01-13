from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from common.forms import UserForm

def logout_view(request):
    logout(request)
    return redirect('mainapp:qna_main')

def signup(request):
    if request.method == "POST": # 화면에서 입려갛ㄴ 데이ㅓㅌ로 사용자를 생성
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('mainapp:qna_main')
    else: # 회원가입 화면 보여줌
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})