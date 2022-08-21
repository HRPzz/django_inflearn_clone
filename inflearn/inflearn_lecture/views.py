from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import myText


# Create your views here.
def home_list(request):
    texts = myText.objects.filter()  # db 에 있는 myText 데이터를 모두 가져옴
    return render(request, 'inflearn_lecture/home_list.html', {'texts': texts})  # templates/inflearn_lecture/home_list.html 와 연결, texts 라는 변수에 담아서 myText 데이터를 보냄

def lecture_list(request):
    texts = myText.objects.filter()
    hot_lecture = myText.objects.filter(category="인기")
    return render(request, 'inflearn_lecture/lecture_list.html',
                {'texts': texts, 'hot_lecture': hot_lecture}
                )

def login(request):
    return render(request, 'inflearn_lecture/login.html')

def join(request):
    print('join 실행!')
    if request.method == 'POST':  # POST 요청이 들어오면 회원가입 진행
        print('여기는 포스팅요청')

        email = request.POST['email']
        pwd = request.POST['pwd']
        
        User.objects.create_user(username=email, password=pwd)

        return redirect('/')  # 회원가입 끝나고 홈으로 돌아감

    print('join 마지막 부분')
    return render(request, 'inflearn_lecture/join.html')