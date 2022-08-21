from django.shortcuts import render, redirect, get_object_or_404
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

    print('login 실행!')
    if request.method == 'POST':  # POST 요청이 들어오면 로그인 진행
        print('login post')

        email = request.POST['email']
        pwd = request.POST['pwd']

        user = auth.authenticate(request, username=email, password=pwd)  # 유저 정보 찾아오기

        if user is None:  # 유저 정보가 없는 경우
            print('회원가입된 사람이 아님')
            return redirect('/join')  # 회원가입 페이지로 이동
        else:  # 유저 정보가 있는 경우
            auth.login(request, user)  # 로그인
            return redirect('/')  # 로그인 끝나고 홈으로 돌아감

    return render(request, 'inflearn_lecture/login.html')

def join(request):
    print('join 실행!')
    if request.method == 'POST':  # POST 요청이 들어오면 회원가입 진행
        print('여기는 포스팅요청')

        email = request.POST['email']
        pwd = request.POST['pwd']
        
        User.objects.create_user(username=email, password=pwd)  # 회원가입

        return redirect('/')  # 회원가입 끝나고 홈으로 돌아감

    print('join 마지막 부분')
    return render(request, 'inflearn_lecture/join.html')

def logout(request):
    auth.logout(request)  # 로그아웃
    return redirect('/')  # 로그아웃 끝나고 홈으로 돌아감

def lecture_list_info(request, pk):  # pk: 게시글 id 값
    board_contents = get_object_or_404(myText, pk=pk)
    return render(request, 'inflearn_lecture/lecture_list_info.html', {'board_contents': board_contents})  # templates/inflearn_lecture/lecture_list_info.html 와 연결, board_contents 라는 변수에 담아서 board_contents (myText, pk) 데이터를 보냄