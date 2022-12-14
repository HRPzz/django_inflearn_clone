from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import myText, Comment
from .forms import LectureForm


# Create your views here.
def home_list(request):
    texts = myText.objects.filter()  # 게시글(db 에 있는 myText 데이터)를 모두 가져옴
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
    comment = Comment.objects.filter(lecture=board_contents)
    print('**** comment?', comment)  # 댓글 확인

    if request.user.is_authenticated:
        print("**** 현재 로그인한 유저 이름?", request.user.username)  # 현재 로그인한 유저의 이름 # 굳이 아래의 'writer = request.POST['writer']' 코드처럼 입력받지 않아도 알 수 있음

    if request.method == 'POST':  # POST 요청이 들어오면 댓글 생성 진행
        rate = request.POST['rate']
        writer = request.POST['writer']  # 현재 로그인한 유저의 이름
        comment = request.POST['comment']

        Comment.objects.create(lecture=board_contents,
                                writer=writer,
                                rate=rate,
                                comment=comment
                                )  # 댓글 생성
        
        return redirect('/lecture_list/' + str(pk))

    return render(request, 'inflearn_lecture/lecture_list_info.html',
                {'board_contents': board_contents, 'comment': comment,}
                )  # templates/inflearn_lecture/lecture_list_info.html 와 연결, board_contents 라는 변수에 담아서 board_contents (myText, pk), comment 데이터를 보냄

def comment_remove(request, pk):
    if request.method == 'POST':  # POST 요청이 들어오면 댓글 삭제 진행
        Comment.objects.get(pk=pk).delete()  # 댓글 삭제
        
    return redirect('/lecture_list')

def show_lecture(request, pk):
    board_contents = get_object_or_404(myText, pk=pk)
    return render(request, 'inflearn_lecture/show_lecture.html', {'board_contents': board_contents})

def create_lecture(request):
    if request.method == 'POST':  # POST 요청이 들어오면 강의 만들기 진행
        form = LectureForm(request.POST, request.FILES)  # html 에서 폼 받아오기
        if form.is_valid():  # 값이 있는가
            myText = form.save(commit=False)  # 폼에 내용 저장
            myText.author = request.user  # 글 쓴 사람 == 로그인한 유저
            myText.save()  # 모델 저장
            return redirect('/')
    
    lecture_form = LectureForm()  # inflearn_lecture/forms.py 에서 생성한 폼

    return render(request, 'inflearn_lecture/create_lecture.html', {'lecture_form': lecture_form})

def my_lecture(request):
    lectures = myText.objects.filter(author=request.user)  # 로그인한 유저가 만든 강의만 가져옴
    return render(request, 'inflearn_lecture/my_lecture.html', {'lectures': lectures})

def edit_lecture(request, pk):
    lecture = get_object_or_404(myText, pk=pk)  # 이미 만들어진 폼(강의)을 그대로 가져옴
    
    if request.method == 'POST':  # POST 요청이 들어오면 강의 수정 진행
        lecture_form = LectureForm(request.POST, request.FILES, instance=lecture)

        if lecture_form.is_valid():  # 값이 있는가
            lecture = lecture_form.save(commit=False)  # 폼에 내용 저장
            lecture.author = request.user  # 글 쓴 사람 == 로그인한 유저
            lecture.save()  # 모델 저장

            return redirect('/my_lecture')
    else:
        lecture_form = LectureForm(instance=lecture)
    
    return render(request, 'inflearn_lecture/edit_lecture.html',
                {'lecture_form': lecture_form, 'pk': pk}
                )
