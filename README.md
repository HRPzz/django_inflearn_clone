<div align='center'>
    <h1>[Django] 장고로 인프런 따라만들기</h1>
</div>

<div align="right">
    <a href="https://github.com/HRPzz/django_inflearn_clone"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FHRPzz%2Fdjango_inflearn_clone&count_bg=%23000000&title_bg=%23000000&icon=github.svg&icon_color=%23E7E7E7&title=django_inflearn_clone&edge_flat=false"/></a>
</div>

|                          Thumbnail                           | Contents                                                     |
| :----------------------------------------------------------: | ------------------------------------------------------------ |
| [![Thumnail](https://cdn.inflearn.com/public/course-326045-cover/101c0b65-770a-454e-a959-14a7fdd99f8f)][Thumnail] | 1. 강의에서 만드는 기능<br/>&emsp;- 강의 업로드 / 수정<br/>&emsp;- 수강평 쓰기 / 삭제<br/>&emsp;- 회원가입 / 로그인 / 로그아웃<br/>&emsp;- 이밖에 간단한 HTML, CSS, JS(jQuery)를 이용해 레이아웃 약간 꾸미기<br/>2. 선수 지식<br/>&emsp;- [Python][Python]<br/>&emsp;- [HTML/CSS, Javascript(jQuery)][HTML/CSS, Javascript(jQuery)]<br/>3. CRUD (Create, Read, Update, Delete) 중심<br/>4. [코드 완성본 다운로드](https://drive.google.com/file/d/1xaKWeWct04BaEkEC1B4iQhfyYPKJlJD3/view?usp=sharing)<br/>5. 참고 자료<br/>&emsp;- [장고 문서][장고 문서]<br/>&emsp;- [장고걸스 튜토리얼][장고걸스 튜토리얼]<br/>&emsp;- [Django REST API 만들기][Django REST API 만들기]<br/>&emsp;- [Django 자습][Django 자습] |

[Thumnail]: https://github.com/HRPzz/django_inflearn_clone
[Python]: https://www.youtube.com/watch?v=kWiCuklohdY
[HTML/CSS, Javascript(jQuery)]: https://www.inflearn.com/course/%EC%9B%B9-%EA%B0%9C%EB%B0%9C-%EA%B8%B0%EC%B4%88-%EC%9E%85%EB%AC%B8
[장고 문서]: https://docs.djangoproject.com/ko/3.1/intro/tutorial01/
[장고걸스 튜토리얼]: https://tutorial.djangogirls.org/ko/
[Django REST API 만들기]: https://www.django-rest-framework.org/
[Django 자습]: https://wikidocs.net/book/837

- '[[Django] 장고로 인프런 따라만들기][django_inflearn_clone]' 강의 난이도는 입문, 초급, 중급 이상 중에서 **초급**이다.
  - Database 는 장고에서 기본으로 세팅된 **sqlite3** 사용
  - 프로젝트 규모가 작아서 1개 앱으로 진행
    - 프로젝트 규모가 커지면 여러 앱(강의 관련, 유저 관련 등)으로 관리해야 url 관리하기 편함
    - 1개 앱으로만 진행하면 url 이 점점 복잡해지기 때문

  - 명칭: 장고 프로젝트 'inflearn', 앱 'inflearn_lecture'

- 기존 강의에서 사용하는 Django 개발 프로그램은 PyCharm 2019.3 Community 이고 MacOS 환경에서 작업한다.
- 알아보니 PyCharm 은 Professional 버전에서만 Docker Container 에 연결할 수 있고 Community 버전에서는 불가능하다.
- 따라서, 나는 Docker Container 에 연결해서 개발하기 위해 **VS Code** 를 사용하기로 결정했다.
- **Windows 11 에서 Docker 를 설치** 하고 Docker image 중에서 **python:3.7** 을 다운받은 다음에 해당 Container 를 만들어서 사용할 것이다.

[django_inflearn_clone]: https://www.inflearn.com/course/%EC%9E%A5%EA%B3%A0-%EC%9D%B8%ED%94%84%EB%9F%B0

### 최종 폴더 트리 참고

```console
django_inflearn_clone
├── LICENSE
├── README.md
├── direc_tree.txt
├── inflearn
│   ├── db.sqlite3
│   ├── inflearn
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── inflearn_lecture
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── inflearn_lecture
│   │   │       ├── base.html
│   │   │       ├── create_lecture.html
│   │   │       ├── edit_lecture.html
│   │   │       ├── home_list.html
│   │   │       ├── join.html
│   │   │       ├── lecture_list.html
│   │   │       ├── lecture_list_info.html
│   │   │       ├── login.html
│   │   │       ├── my_lecture.html
│   │   │       └── show_lecture.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

---

## 📌 TABLE OF CONTENTS

| N  | Title              |  Link  |  Commit History  |  Code  |
| :--: | ------------------ | :----: | ------ | ------ |
|  1   | 장고 프로젝트 세팅 | [✏️](#1-장고-프로젝트-세팅) | django setting | [➡️][commit_1] |
| 2 | 장고 앱 세팅 | [✏️](#2-장고-앱-세팅) | app setting | [➡️][commit_2] |
| 3 | 장고 앱 url 연결 | [✏️](#3-장고-앱-url-연결) | app url | [➡️][commit_3] |
| 4 | admin 게시글 작성 | [✏️](#4-admin-게시글-작성) | dmin myText model | [➡️][commit_4] |
| 5 | ckeditor | [✏️](#5-ckeditor) | ckeditor | [➡️][commit_5] |
| 6 | 장고 쿼리 | [✏️](#6-장고-쿼리) | query | [➡️][commit_6] |
| 7 | 장고 템플릿 | [✏️](#7-장고-템플릿) | templates | [➡️][commit_7] |
| 8 | django template language | [✏️](#8-django-template-language) | django template language | [➡️][commit_8] |
| 9 | 부트스트랩으로 꾸미기 | [✏️](#9-부트스트랩으로-꾸미기) | bootstrap | [➡️][commit_9] |
| 10 | 강의 리스트 꾸미기 | [✏️](#10-강의-리스트-꾸미기) | lecture list | [➡️][commit_10] |
| 11 | 로그인, 회원가입 폼 만들기 | [✏️](#11-로그인,-회원가입-폼-만들기) | login, join form | [➡️][commit_11] |
| 12 | 회원가입 기능 구현 | [✏️](#12-회원가입-기능-구현) | join function | [➡️][commit_12] |
| 13 | 로그인/로그아웃 기능 구현 | [✏️](#13-로그인로그아웃-기능-구현) | login, logout function | [➡️][commit_13] |
| 14 | 강의 상세 페이지 | [✏️](#14-강의-상세-페이지) | lecture list info | [➡️][commit_14] |
| 15 | 댓글 폼 만들기 | [✏️](#15-댓글-폼-만들기) | comment form | [➡️][commit_15] |
| 16 | 댓글 기능 구현 | [✏️](#16-댓글-기능-구현) | comment function | [➡️][commit_16] |
| 17 | 댓글 보이기 (in HTML) | [✏️](#17-댓글-보이기-in-html) | comment in html | [➡️][commit_17] |
| 18 | 댓글 삭제 | [✏️](#18-댓글-삭제) | comment delete function | [➡️][commit_18] |
| 19 | 강의보기 리스트 만들기 | [✏️](#19-강의보기-리스트-만들기) | lecture section list | [➡️][commit_19] |
| 20 | 강의보기 페이지 만들기 | [✏️](#20-강의보기-페이지-만들기) | show lecture | [➡️][commit_20] |
| 21 | jQuery 로 탭 만들기 | [✏️](#21-jqeury로-탭-만들기) | show lecture tab | [➡️][commit_21] |
| 22 | 사용자 강의 만들기 | [✏️](#22-사용자-강의-만들기) | create lecture html form | [➡️][commit_22] |
| 23 | 사용자 강의 만들기 기능 구현 | [✏️](#23-사용자-강의-만들기-기능-구현) | create lecture function | [➡️][commit_23] |
| 24 | 내 강의 보기 | [✏️](#24-내-강의-보기) | my lecture | [➡️][commit_24] |
| 25 | 내 강의 수정하기 | [✏️](#25-내-강의-수정하기) | edit my lecture function | [➡️][commit_25] |
| + | REST API | [✏️](#추가-rest-api) | - | - |

[commit_1]: https://github.com/HRPzz/django_inflearn_clone/tree/adbd15bc152ed84708b3d42a513e2a50ccd4eda4
[commit_2]: https://github.com/HRPzz/django_inflearn_clone/tree/c16177ba3662ae7db377b9b96471cd6e1c14dfc0
[commit_3]: https://github.com/HRPzz/django_inflearn_clone/tree/94b8f01b35a6a2be9672048879979599caeda8c6
[commit_4]: https://github.com/HRPzz/django_inflearn_clone/tree/04cf9e4727da940fdddc888fa6e8810a4116ccb7
[commit_5]: https://github.com/HRPzz/django_inflearn_clone/tree/5bd392c48c198738b4e6376fb04c38ea063b42e2
[commit_6]: https://github.com/HRPzz/django_inflearn_clone/tree/85ba2cb7146dae22bac2a55e8aee9dd6357fff37
[commit_7]: https://github.com/HRPzz/django_inflearn_clone/tree/2881d1d621e31c6e1baf2dfc24948a670f1d8dbd
[commit_8]: https://github.com/HRPzz/django_inflearn_clone/tree/666af3c13cfc0178e7d16c493b06065ef48d3ce4
[commit_9]: https://github.com/HRPzz/django_inflearn_clone/tree/e2c9ef7ddf0368431a8cf653f822b7bd1adc7035
[commit_10]: https://github.com/HRPzz/django_inflearn_clone/tree/7546f8826aa615e4788fab323d92500fc4e28a38
[commit_11]: https://github.com/HRPzz/django_inflearn_clone/tree/a74cb3ca9587637925978e56887d12c705dfe545
[commit_12]: https://github.com/HRPzz/django_inflearn_clone/tree/71108e65807671c1c4624c22e3afc8c224d96076
[commit_13]: https://github.com/HRPzz/django_inflearn_clone/tree/525b9ba8300102a2c606a5278ed70bf321a93fcb
[commit_14]: https://github.com/HRPzz/django_inflearn_clone/tree/d61184ddf7be3cd86a9158417692bc42a0ce38b4
[commit_15]: https://github.com/HRPzz/django_inflearn_clone/tree/c963e6aa223b23f89e7d5cd2089e30becd90eadd
[commit_16]: https://github.com/HRPzz/django_inflearn_clone/tree/def53559da42dff16990e95b87ad0c4a2977cf46
[commit_17]: https://github.com/HRPzz/django_inflearn_clone/tree/084536c86bcb1fcf05e01963ff79b16f44a721be
[commit_18]: https://github.com/HRPzz/django_inflearn_clone/tree/82fe907f9fa61d06c853a4f7f69908fff726d493
[commit_19]: https://github.com/HRPzz/django_inflearn_clone/tree/d93dacdc611d46cf639b7e6e7652802cf26573c2
[commit_20]: https://github.com/HRPzz/django_inflearn_clone/tree/d822e677c7447211a84d149846f5da8f3a55737b
[commit_21]: https://github.com/HRPzz/django_inflearn_clone/tree/4d9c99849c7b5220bdcb7405d1a5931d8da44201
[commit_22]: https://github.com/HRPzz/django_inflearn_clone/tree/4e4b50a0e1acc134b632c0f3a93ff5bdcc02160f
[commit_23]: https://github.com/HRPzz/django_inflearn_clone/tree/ef8dfa7f2599f7259e5d4f7ecd9aced1a1aa0f36
[commit_24]: https://github.com/HRPzz/django_inflearn_clone/tree/3bc0c1090bcecb877738f194a06d9194fa9a1e3c
[commit_25]: https://github.com/HRPzz/django_inflearn_clone/tree/63c45a5f985d6970b850083fe0b51dc59fc68b23

---

## [1] 장고 프로젝트 세팅

### 장고 프로젝트 시작

- 도커 컨테이너 생성

```bash
docker pull python:3.7 # 도커 이미지 python 3.7 다운로드
docker run --name django_inflearn_clone python:3.7 # 도커 컨테이너 django_inflearn_clone 생성
docker start django_inflearn_clone # 컨테이너 시작
docker exec -it django_inflearn_clone /bin/bash # 컨테이너 bash shell 접속
```

- 도커 컨테이너 내부 환경 세팅

```bash
apt-get update
apt-get upgrade

dpkg-reconfigure tzdata  # timezone 으로 Asia/Seoul 설정

apt install nano
apt install vim
apt install virtualenv
apt install tree
```

- 작업 폴더 생성

```bash
mkdir django_inflearn_clone # 폴더 생성
cd django_inflearn_clone # 이동
pwd # 현재 위치 확인
```

- 파이썬 가상환경 세팅

```bash
virtualenv venv # 가상환경 세팅
source venv/bin/activate # 가상환경 실행
pip install django # django 설치
```

- 장고 프로젝트 생성

```bash
django-admin startproject inflearn # 장고 프로젝트 inflearn 생성
cd inflearn # pycharm 에서 inflearn 폴더 열기
python manage.py runserver # 장고 서버 실행
```

- 장고 기본 웹 페이지 접속: http://127.0.0.1:8000/

### 폴더 트리 참고

```bash
tree -L 5 -o direc_tree.txt
```

```console
django_inflearn_clone
├── .gitignore
├── LICENSE
├── README.md
├── inflearn
│   ├── db.sqlite3
│   ├── inflearn
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── manage.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

**[⬆ back to top](#-table-of-contents)**

---

## [2] 장고 앱 세팅

### 장고 프로젝트 안에 여러 앱(기능) 만들 수 있음

- 장고 앱 생성

```bash
django-admin startapp inflearn_lecture # 장고 앱 inflearn_lecture 생성
```

- inflearn/settings.py 에 앱 생성한 것을 표시해줘야 함

```python
...
INSTALLED_APPS = [
    ...
    'inflearn_lecture',
]
...
```

- db 처리를 해줘야 관리자 페이지(127.0.0.1:8000/admin) 접속 가능

```bash
python manage.py makemigrations
python manage.py migrate
```

- admin 계정 생성

```bash
python manage.py createsuperuser  # id, email, pw 설정
```

### 폴더 트리 참고

```bash
tree -L 5 -o direc_tree.txt
```

```console
django_inflearn_clone
├── .gitignore
├── LICENSE
├── README.md
├── inflearn
│   ├── db.sqlite3
│   ├── inflearn
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── inflearn_lecture
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   └── manage.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

**[⬆ back to top](#-table-of-contents)**

---

## [3] 장고 앱 url 연결

### url 연결 순서

```console
1. 프로젝트(inflearn/urls.py) 와 앱(inflearn_lecture/urls.py) 연결
2. 앱(inflearn_lecture/urls.py) 과 뷰(inflearn_lecture/views.py) 연결
3. 뷰(inflearn_lecture/views.py) 와 페이지(inflearn_lecture/templates/inflearn_lecture/home_list.html) 연결
```

- inflearn/urls.py 수정
  - 프로젝트(inflearn/urls.py) 와 앱(inflearn_lecture/urls.py) 연결


```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('inflearn_lecture.urls')),  # 앱 inflearn_lecture 의 urls.py 와 연결
]
```

- inflearn_lecture/urls.py 생성
  - 앱(inflearn_lecture/urls.py) 과 뷰(inflearn_lecture/views.py) 연결


```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_list, name='home_list'),  # views.py 와 연결
]
```

- inflearn_lecture/views.py 수정
  - 뷰(inflearn_lecture/views.py) 와 페이지(inflearn_lecture/templates/inflearn_lecture/home_list.html) 연결


```python
from django.shortcuts import render

# Create your views here.
def home_list(request):
    return render(request, 'inflearn_lecture/home_list.html')  # templates/inflearn_lecture/home_list.html 와 연결
```

- inflearn_lecture/templates/inflearn_lecture/home_list.html 생성

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Title</title>
</head>
<body>
    여기는 홈!!!
</body>
</html>
```

- 장고 서버 실행

```bash
python manage.py runserver # 장고 서버 실행
```

- 장고 url 연결 확인: http://127.0.0.1:8000/

### 폴더 트리 참고

```bash
tree -L 5 -o direc_tree.txt
```

```console
django_inflearn_clone
├── LICENSE
├── README.md
├── direc_tree.txt
├── inflearn
│   ├── db.sqlite3
│   ├── inflearn
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── inflearn_lecture
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── inflearn_lecture
│   │   │       └── home_list.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

**[⬆ back to top](#-table-of-contents)**

---

## [4] admin 게시글 작성

- inflearn_lecture/models.py 수정
  - 어떤 데이터 형태가 들어갈 것인지 정함

```python
from django.db import models
from django.conf import settings

# Create your models here.
class myText(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    contents = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
```

- inflearn_lecture/admin.py 수정
  - model 제작한 걸 관리자 페이지에 알려줘야 함

```python
from django.contrib import admin
from .models import myText

admin.site.register(myText)
# Register your models here.
```

- db 처리
  - inflearn/settings.py 에서 DATABASES 를 보면 sqlite3 이 적용되어 있는 것을 볼 수 있음
  - 외부 db 사용 안 할 예정

```bash
python manage.py makemigrations
python manage.py migrate
```

- 장고 서버 실행

```bash
python manage.py runserver
```

- admin 로그인하고 mytext 1개 작성: http://127.0.0.1:8000/admin
- inflearn_lecture/views.py 수정
  - db 에 있는 myText 데이터를 모두 가져옴
  - html 과 연결, texts 라는 변수에 담아서 myText 데이터를 보냄


```python
from django.shortcuts import render
from .models import myText

# Create your views here.
def home_list(request):
    texts = myText.objects.filter()  # db 에 있는 myText 데이터를 모두 가져옴
    return render(request, 'inflearn_lecture/home_list.html', {'texts': texts})  # templates/inflearn_lecture/home_list.html 와 연결, texts 라는 변수에 담아서 myText 데이터를 보냄
```

- inflearn_lecture/templates/inflearn_lecture/home_list.html 수정
  - views 에서 받은 texts 변수 (db 에 있는 myText 데이터) 를 html 에 출력


```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Title</title>
</head>
<body>
    여기는 홈!!!
    {{ texts }}  <!-- db 에 있는 myText 데이터 -->
</body>
</html>
```

### 폴더 트리 참고

```bash
tree -L 5 -o direc_tree.txt
```

```console
django_inflearn_clone
├── LICENSE
├── README.md
├── direc_tree.txt
├── inflearn
│   ├── db.sqlite3
│   ├── inflearn
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── inflearn_lecture
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── inflearn_lecture
│   │   │       └── home_list.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

**[⬆ back to top](#-table-of-contents)**

---

## [5] ckeditor

- ckeditor 패키지 설치

```bash
pip install django-ckeditor
```

- inflearn/settings.py 수정
  - INSTALLED_APPS 에 ckeditor 관련 설정
  - CKEDITOR_UPLOAD_PATH, MEDIA_URL, MEDIA_ROOT 경로 설정

```python
...
INSTALLED_APPS = [
    ...
    'inflearn_lecture',
    'ckeditor',
    'ckeditor_uploader',
]

...

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

CKEDITOR_UPLOAD_PATH = 'uploads/'

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'
...
```

- inflearn/urls.py 수정
  - ckeditor 관련 경로 설정


```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('inflearn_lecture.urls')),  # 앱 inflearn_lecture 의 urls.py 와 연결
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- inflearn_lecture/models.py 수정
  - ckeditor - myText  추가/수정할 때 텍스트 에디터 칸(게시판 형태) 만들기 위함

```python
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class myText(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    contents = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)

    board_text = RichTextUploadingField(null=True)  # ckeditor

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
```

- db 처리

```bash
python manage.py makemigrations
python manage.py migrate
```

- 장고 서버 실행

```bash
python manage.py runserver
```

- admin 로그인하고 mytext 1개 작성할 때 board_text 칸 확인: http://127.0.0.1:8000/admin

### 폴더 트리 참고

```bash
tree -L 5 -o direc_tree.txt
```

```console
django_inflearn_clone
├── LICENSE
├── README.md
├── direc_tree.txt
├── inflearn
│   ├── db.sqlite3
│   ├── inflearn
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── inflearn_lecture
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── inflearn_lecture
│   │   │       └── home_list.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

**[⬆ back to top](#-table-of-contents)**

---

## [6] 장고 쿼리

- inflearn_lecture/models.py 수정
  - category 속성 추가

```python
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class myText(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    contents = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)

    category = models.CharField(max_length=200, null=True)  # 카테고리 설정

    board_text = RichTextUploadingField(null=True)  # ckeditor

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
```

- db 처리

```bash
python manage.py makemigrations
python manage.py migrate
```

- 장고 서버 실행

```bash
python manage.py runserver
```

- admin 로그인하고 mytext 데이터 수정 - category 에 HTML 작성: http://127.0.0.1:8000/admin
- inflearn_lecture/views.py 수정
  - myText 에서 category="HTML" 인 데이터만 가져오게 설정

```python
from django.shortcuts import render
from .models import myText

# Create your views here.
def home_list(request):
    texts = myText.objects.filter(category="HTML")  # db 에 있는 카테고리가 HTML 인 myText 데이터를 모두 가져옴
    return render(request, 'inflearn_lecture/home_list.html', {'texts': texts})  # templates/inflearn_lecture/home_list.html 와 연결, texts 라는 변수에 담아서 myText 데이터를 보냄
```

- 장고 기본 웹 페이지 접속해서 확인: http://127.0.0.1:8000/

### 폴더 트리 참고

```bash
tree -L 5 -o direc_tree.txt
```

```console
django_inflearn_clone
├── LICENSE
├── README.md
├── direc_tree.txt
├── inflearn
│   ├── db.sqlite3
│   ├── inflearn
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── inflearn_lecture
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── inflearn_lecture
│   │   │       └── home_list.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

**[⬆ back to top](#-table-of-contents)**

---

## [7] 장고 템플릿

- inflearn_lecture/templates/inflearn_lecture/base.html 생성

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Title</title>

    <!-- CSS -->
    <style>
        * {
            margin: 0px;
            padding: 0px;
        }

        #main {
            width: 100%;
            height:50vh;
            background-image: url("https://cdn.inflearn.com/public/main_sliders/e85e0c0a-c4ba-46bb-8e73-5c647b72db19/newsletter-infocus-03-main-521.png");
        }

        nav {
            width: 100%;
            height: 60px;
            background-color: white;
            line-height: 50px;
        }

        nav ul {
            float: right;
        }

        nav ul li {
            margin: 10px;
            list-style-type: none;
            display: inline-block;
        }
    </style>
</head>
<body>
    
    <div id="main">
        <nav>
            <img src="https://cdn.inflearn.com/assets/brand/chuseok_logo.png" width="150">
            <ul>
                <li>메뉴1</li>
                <li>메뉴2</li>
                <li>메뉴3</li>
                <li>메뉴4</li>
                <li>메뉴5</li>
            </ul>
        </nav>
    </div>

    {% block content %}
    {% endblock %}
    
</body>
</html>
```

- inflearn_lecture/templates/inflearn_lecture/home_list.html 수정

```html
{% extends 'inflearn_lecture/base.html' %}

{% block content %}
    여기는 홈!!!
    {{ texts }}  <!-- db 에 있는 myText 데이터 -->
{% endblock %}
```

### 폴더 트리 참고

```bash
tree -L 5 -o direc_tree.txt
```

```console
django_inflearn_clone
├── LICENSE
├── README.md
├── direc_tree.txt
├── inflearn
│   ├── db.sqlite3
│   ├── inflearn
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── inflearn_lecture
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── inflearn_lecture
│   │   │       ├── base.html
│   │   │       └── home_list.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

**[⬆ back to top](#-table-of-contents)**

---

## [8] django template language

### 게시글 내용을 html 에 불러오기

- django template language
  - **{{ }}** 와 같은 구문은 **단순 변수 출력**을 위해서 쓰는 태그
  - **{% %}** 와 같은 구문은 **if, for 등 임의의 로직을 실행**하기 위해 쓰이는 태그

- inflearn_lecture/views.py 수정

```python
from django.shortcuts import render
from .models import myText

# Create your views here.
def home_list(request):
    texts = myText.objects.filter()  # db 에 있는 myText 데이터를 모두 가져옴
    return render(request, 'inflearn_lecture/home_list.html', {'texts': texts})  # templates/inflearn_lecture/home_list.html 와 연결, texts 라는 변수에 담아서 myText 데이터를 보냄
```

- inflearn_lecture/templates/inflearn_lecture/home_list.html 수정

```html
{% extends 'inflearn_lecture/base.html' %}

{% block content %}

    <h2>인기 강의</h2>

    <!-- texts: db 에 있는 myText 데이터 -->
    {% for text in texts %}
        <img src="{{ text.img_url }}" width="100">
        <br>
        {{ text.title }}
        <br>

    {% endfor %}

{% endblock %}
```

### 폴더 트리 참고

```bash
tree -L 5 -o direc_tree.txt
```

```console
django_inflearn_clone
├── LICENSE
├── README.md
├── direc_tree.txt
├── inflearn
│   ├── db.sqlite3
│   ├── inflearn
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── inflearn_lecture
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── inflearn_lecture
│   │   │       ├── base.html
│   │   │       └── home_list.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

**[⬆ back to top](#-table-of-contents)**

---

## [9] 부트스트랩으로 꾸미기

- inflearn_lecture/models.py 수정
  - img_url 을 models.CharField 에서 models.FileField 로 변경

```python
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class myText(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    contents = models.CharField(max_length=200)
    img_url = models.FileField(null=True)

    category = models.CharField(max_length=200, null=True)  # 카테고리 설정

    board_text = RichTextUploadingField(null=True)  # ckeditor

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
```

- db 처리

```bash
python manage.py makemigrations
python manage.py migrate
```

- 장고 서버 실행

```bash
python manage.py runserver
```

- admin 로그인하고 mytext 데이터 수정 - img_url 에서 파일 선택 버튼 클릭 후 img file 업로드: http://127.0.0.1:8000/admin
- inflearn_lecture/templates/inflearn_lecture/base.html 수정
  - [부트스트랩 CDN](http://bootstrapk.com/getting-started/) 적용

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>인프런 따라만들기</title>

    <!-- 부트스트랩 적용하기 -->
    <!-- 합쳐지고 최소화된 최신 CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">

    <!-- 부가적인 테마 -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">

    <!-- 합쳐지고 최소화된 최신 자바스크립트 -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>

    <!-- CSS -->
    <style>
        * {
            margin: 0px;
            padding: 0px;
        }

        #main {
            width: 100%;
            height:50vh;
            background-image: url("https://cdn.inflearn.com/public/main_sliders/e85e0c0a-c4ba-46bb-8e73-5c647b72db19/newsletter-infocus-03-main-521.png");
        }

        nav {
            width: 100%;
            height: 60px;
            background-color: white;
            line-height: 50px;
        }

        nav ul {
            float: right;
        }

        nav ul li {
            margin: 10px;
            list-style-type: none;
            display: inline-block;
        }
    </style>
</head>
<body>
    
    <div id="main">
        <nav>
            <img src="https://cdn.inflearn.com/assets/brand/chuseok_logo.png" width="150">
            <ul>
                <li>메뉴1</li>
                <li>메뉴2</li>
                <li>메뉴3</li>
                <li>메뉴4</li>
                <li>메뉴5</li>
            </ul>
        </nav>
    </div>

    {% block content %}
    {% endblock %}
    
</body>
</html>
```

- inflearn_lecture/templates/inflearn_lecture/home_list.html 수정
  - [부트스트랩 콤포넌트 썸네일 기본예제](http://bootstrapk.com/components/#thumbnails) 적용

```html
{% extends 'inflearn_lecture/base.html' %}

{% block content %}

    <h2>인기 강의</h2>

    <!-- texts: db 에 있는 myText 데이터 -->
    <div class="row">
        {% for text in texts %}
            
                <div class="col-xs-6 col-md-3">
                <a href="#" class="thumbnail">
                    <img src="../../media/{{ text.img_url }}" alt="../../media/{{ text.img_url }}">
                    <div class="caption">
                        <h3>{{ text.title }}</h3>
                    </div>
                </a>
                </div>
                ...
            

        {% endfor %}
    </div>

{% endblock %}
```

### 폴더 트리 참고

```bash
tree -L 5 -o direc_tree.txt
```

```console
django_inflearn_clone
├── LICENSE
├── README.md
├── direc_tree.txt
├── inflearn
│   ├── db.sqlite3
│   ├── inflearn
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── inflearn_lecture
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── inflearn_lecture
│   │   │       ├── base.html
│   │   │       └── home_list.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

**[⬆ back to top](#-table-of-contents)**

---

## [10] 강의 리스트 꾸미기

- inflearn_lecture/urls.py 수정
  - lecture_list 추가

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_list, name='home_list'),  # views.py 와 연결

    path('lecture_list/', views.lecture_list, name='lecture_list'),
]
```

- inflearn_lecture/views.py 수정
  - lecture_list 추가

```python
from django.shortcuts import render
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
```

- inflearn_lecture/templates/inflearn_lecture/lecture_list.html 생성
  - 제이쿼리를 이용해서 탭(카테고리)을 누르면 해당되는 것만 보이게 설정

```html
{% extends 'inflearn_lecture/base.html' %}

{% block content %}

    <style>
        div {
            float: left
        }

        .left {
            width: 30%;
        }

        .left ul li {
            margin: 10px;
            padding: 10px;
            border: 1px solid gray;
        }

        .right {
            width: 70%;
        }
    </style>

    <div class="left">
        <ul>
            <li>HTML</li>
            <li>CSS</li>
            <li>JS</li>
            <li id="hot_lecture">인기</li>
            <li>추천</li>
        </ul>
    </div>

    <div class="right">
        <div class="row all">
            {% for text in texts %}
                
                    <div class="col-xs-6 col-md-3">
                    <a href="#" class="thumbnail">
                        <img src="../../media/{{ text.img_url }}" alt="../../media/{{ text.img_url }}">
                        <div class="caption">
                            <h3>{{ text.title }}</h3>
                        </div>
                    </a>
                    </div>
                    ...
                
        
            {% endfor %}
        </div>

        <div class="row hot">
            {% for text in hot_lecture %}
                
                    <div class="col-xs-6 col-md-3">
                    <a href="#" class="thumbnail">
                        <img src="../../media/{{ text.img_url }}" alt="../../media/{{ text.img_url }}">
                        <div class="caption">
                            <h3>{{ text.title }}</h3>
                        </div>
                    </a>
                    </div>
                    ...
                
        
            {% endfor %}
        </div>
    </div>

    <script>
        // 제이쿼리 사용
        $('#hot_lecture').click(function(){
            $('.row').hide();
            $('.hot').show();
        });
    </script>

{% endblock %}
```

- inflearn_lecture/templates/inflearn_lecture/base.html 수정
  - a 태그로 로고 이미지 클릭하면 홈으로 가도록 설정
  - [제이쿼리 CDN](https://www.w3schools.com/jquery/jquery_get_started.asp) 적용
  - 하단 바(footer) 작성

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>인프런 따라만들기</title>

    <!-- 제이쿼리 CDN -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>

    <!-- 부트스트랩 CDN -->
    <!-- 합쳐지고 최소화된 최신 CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">

    <!-- 부가적인 테마 -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">

    <!-- 합쳐지고 최소화된 최신 자바스크립트 -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>

    <!-- CSS -->
    <style>
        * {
            margin: 0px;
            padding: 0px;
        }

        #main {
            width: 100%;
            height:50vh;
            background-image: url("https://cdn.inflearn.com/public/main_sliders/e85e0c0a-c4ba-46bb-8e73-5c647b72db19/newsletter-infocus-03-main-521.png");
        }

        nav {
            width: 100%;
            height: 60px;
            background-color: white;
            line-height: 50px;
        }

        nav ul {
            float: right;
        }

        nav ul a {
            color: green;
        }

        nav ul li {
            margin: 10px;
            list-style-type: none;
            display: inline-block;
        }

        .footer {
            left: 0;
            bottom: 0;
            width: 100%;
            height: 50px;
            background-color: green;
            text-align: center;
            padding-top: 20px;
        }
    </style>
</head>
<body>
    
    <div id="main">
        <nav>
            <a href="/">
                <img src="https://cdn.inflearn.com/assets/brand/chuseok_logo.png" width="150">
            </a>
            <ul>
                <a href="/lecture_list"><li>강의보기</li></a>
                <li>메뉴2</li>
                <li>메뉴3</li>
                <li>메뉴4</li>
                <li>메뉴5</li>
            </ul>
        </nav>
    </div>

    {% block content %}
    {% endblock %}

    <div class="footer">
        contact : a@naver.com
    </div>
    
</body>
</html>
```

- 장고 서버 실행

```bash
python manage.py runserver
```

- lecture_list 페이지 동작 확인: http://127.0.0.1:8000/lecture_list

### 폴더 트리 참고

```bash
tree -L 5 -o direc_tree.txt
```

```console
django_inflearn_clone
├── LICENSE
├── README.md
├── direc_tree.txt
├── inflearn
│   ├── db.sqlite3
│   ├── inflearn
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── inflearn_lecture
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── inflearn_lecture
│   │   │       ├── base.html
│   │   │       ├── home_list.html
│   │   │       └── lecture_list.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

**[⬆ back to top](#-table-of-contents)**

---

## [11] 로그인, 회원가입 폼 만들기

- inflearn_lecture/views.py 수정
  - login, join 관련 html 연결

```python
from django.shortcuts import render
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
    return render(request, 'inflearn_lecture/join.html')
```

- inflearn_lecture/urls.py 수정
  - login, join 관련 view 연결

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_list, name='home_list'),  # views.py 와 연결

    path('lecture_list/', views.lecture_list, name='lecture_list'),
    path('login/', views.login, name='login'),
    path('join/', views.join, name='join'),
]
```

- inflearn_lecture/templates/inflearn_lecture/base.html 수정
  - a 태그로 로그인/회원가입 클릭하면 로그인/회원가입 페이지로 가도록 설정

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>인프런 따라만들기</title>

    <!-- 제이쿼리 CDN -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>

    <!-- 부트스트랩 CDN -->
    <!-- 합쳐지고 최소화된 최신 CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">

    <!-- 부가적인 테마 -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">

    <!-- 합쳐지고 최소화된 최신 자바스크립트 -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>

    <!-- CSS -->
    <style>
        * {
            margin: 0px;
            padding: 0px;
        }

        #main {
            width: 100%;
            height:50vh;
            background-image: url("https://cdn.inflearn.com/public/main_sliders/e85e0c0a-c4ba-46bb-8e73-5c647b72db19/newsletter-infocus-03-main-521.png");
        }

        nav {
            width: 100%;
            height: 60px;
            background-color: white;
            line-height: 50px;
        }

        nav ul {
            float: right;
        }

        nav ul a {
            color: green;
        }

        nav ul li {
            margin: 10px;
            list-style-type: none;
            display: inline-block;
        }

        .footer {
            left: 0;
            bottom: 0;
            width: 100%;
            height: 50px;
            background-color: green;
            text-align: center;
            padding-top: 20px;
        }
    </style>
</head>
<body>
    
    <div id="main">
        <nav>
            <a href="/">
                <img src="https://cdn.inflearn.com/assets/brand/chuseok_logo.png" width="150">
            </a>
            <ul>
                <a href="/lecture_list"><li>강의보기</li></a>
                <a href="/login"><li>로그인</li></a>
                <a href="/join"><li>회원가입</li></a>
                <li>메뉴4</li>
                <li>메뉴5</li>
            </ul>
        </nav>
    </div>

    {% block content %}
    {% endblock %}

    <div class="footer">
        contact : a@naver.com
    </div>
    
</body>
</html>
```

- inflearn_lecture/templates/inflearn_lecture/login.html, inflearn_lecture/templates/inflearn_lecture/join.html 생성
  - [부트스트랩 CSS 폼 기본예제](http://bootstrapk.com/css/#forms) 적용

```html
{% extends 'inflearn_lecture/base.html' %}

{% block content %}

    <div style="width: 500px; margin: auto; margin-top: 200px, margin-bottom: 200px;">
        <form>
            <div class="form-group">
                <label for="exampleInputEmail1">로그인 이메일</label>
                <input name="email" type="email" class="form-control" id="exampleInputEmail1" placeholder="이메일을 입력하세요"/>
            </div>
            <div class="form-group">
                <label for="exampleInputPassword1">암호</label>
                <input name="pwd" type="password" class="form-control" id="exampleInputPassword1" placeholder="암호"/>
            </div>

            <button type="submit" class="btn btn-default">제출</button>
        </form>
    </div>

{% endblock %}
```

- 장고 서버 실행

```bash
python manage.py runserver
```

- login, join 페이지 확인: http://127.0.0.1:8000/login, http://127.0.0.1:8000/join

### 폴더 트리 참고

```bash
tree -L 5 -o direc_tree.txt
```

```console
django_inflearn_clone
├── LICENSE
├── README.md
├── direc_tree.txt
├── inflearn
│   ├── db.sqlite3
│   ├── inflearn
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── inflearn_lecture
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── inflearn_lecture
│   │   │       ├── base.html
│   │   │       ├── home_list.html
│   │   │       ├── join.html
│   │   │       ├── lecture_list.html
│   │   │       └── login.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

**[⬆ back to top](#-table-of-contents)**

---

## [12] 회원가입 기능 구현

- inflearn_lecture/templates/inflearn_lecture/join.html 수정
  - html 에서 views 로 form 데이터 넘김
  - 보안을 위해 csrf_token 설정


```html
{% extends 'inflearn_lecture/base.html' %}

{% block content %}

    <div style="width: 500px; margin: auto; margin-top: 200px, margin-bottom: 200px;">
        <!-- inflearn_lecture/urls.py 의 path('join', ...) 에 form 데이터를 넘김 => inflearn_lecture/views.py 의 join 함수로 form 데이터가 넘어가게 됨 -->
        <form method="POST" action="{% url 'join' %}">
            {% csrf_token %}  <!-- 보안 설정 -->
            <div class="form-group">
                <label for="exampleInputEmail1">로그인 이메일</label>
                <input name="email" type="email" class="form-control" id="exampleInputEmail1" placeholder="이메일을 입력하세요"/>
            </div>
            <div class="form-group">
                <label for="exampleInputPassword1">암호</label>
                <input name="pwd" type="password" class="form-control" id="exampleInputPassword1" placeholder="암호"/>
            </div>

            <button type="submit" class="btn btn-default">제출</button>
        </form>
    </div>

{% endblock %}

```

- inflearn_lecture/views.py 수정
  - join 함수 수정, POST 요청 들어오면 회원가입 진행


```python
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
```

- 장고 서버 실행

```bash
python manage.py runserver
```

- join 페이지 동작 확인 - 회원가입 진행 (email, pwd 입력): http://127.0.0.1:8000/join
- admin 페이지에서 Users 확인 - 회원가입한 계정 확인 가능: http://127.0.0.1:8000/admin

### 폴더 트리 참고

```bash
tree -L 5 -o direc_tree.txt
```

```console
django_inflearn_clone
├── LICENSE
├── README.md
├── direc_tree.txt
├── inflearn
│   ├── db.sqlite3
│   ├── inflearn
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── inflearn_lecture
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── inflearn_lecture
│   │   │       ├── base.html
│   │   │       ├── home_list.html
│   │   │       ├── join.html
│   │   │       ├── lecture_list.html
│   │   │       └── login.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

**[⬆ back to top](#-table-of-contents)**

---

## [13] 로그인/로그아웃 기능 구현

- inflearn_lecture/templates/inflearn_lecture/login.html 수정
  - html 에서 views 로 form 데이터 넘김
  - 보안을 위해 csrf_token 설정

```html
{% extends 'inflearn_lecture/base.html' %}

{% block content %}

    <div style="width: 500px; margin: auto; margin-top: 200px, margin-bottom: 200px;">
        <!-- html 에서 views 로 form 데이터 넘김 -->
        <form method="POST" action="{% url 'login' %}">
            {% csrf_token %}  <!-- 보안 설정 -->
            <div class="form-group">
                <label for="exampleInputEmail1">로그인 이메일</label>
                <input name="email" type="email" class="form-control" id="exampleInputEmail1" placeholder="이메일을 입력하세요"/>
            </div>
            <div class="form-group">
                <label for="exampleInputPassword1">암호</label>
                <input name="pwd" type="password" class="form-control" id="exampleInputPassword1" placeholder="암호"/>
            </div>

            <button type="submit" class="btn btn-default">제출</button>
        </form>
    </div>

{% endblock %}
```

- inflearn_lecture/views.py 수정
  - login 함수 수정, POST 요청 들어오면 로그인 진행
  - logout 함수 작성, 로그아웃 진행

```python
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
```

- inflearn_lecture/urls.py 수정
  - logout 추가


```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_list, name='home_list'),  # views.py 와 연결

    path('lecture_list/', views.lecture_list, name='lecture_list'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('join/', views.join, name='join'),
]
```

- inflearn_lecture/templates/inflearn_lecture/base.html 수정
  - login 되어 있을 경우 로그아웃 메뉴가 보이게, login 되어 있지 않을 경우 로그인, 회원가입 메뉴가 보이도록 설정
  - a 태그로 로그아웃 클릭하면 홈으로 가도록 설정 (inflearn_lecture/views.py 의 logout 함수가 실행됨)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>인프런 따라만들기</title>

    <!-- 제이쿼리 CDN -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>

    <!-- 부트스트랩 CDN -->
    <!-- 합쳐지고 최소화된 최신 CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">

    <!-- 부가적인 테마 -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">

    <!-- 합쳐지고 최소화된 최신 자바스크립트 -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>

    <!-- CSS -->
    <style>
        * {
            margin: 0px;
            padding: 0px;
        }

        #main {
            width: 100%;
            height:50vh;
            background-image: url("https://cdn.inflearn.com/public/main_sliders/e85e0c0a-c4ba-46bb-8e73-5c647b72db19/newsletter-infocus-03-main-521.png");
        }

        nav {
            width: 100%;
            height: 60px;
            background-color: white;
            line-height: 50px;
        }

        nav ul {
            float: right;
        }

        nav ul a {
            color: green;
        }

        nav ul li {
            margin: 10px;
            list-style-type: none;
            display: inline-block;
        }

        .footer {
            left: 0;
            bottom: 0;
            width: 100%;
            height: 50px;
            background-color: green;
            text-align: center;
            padding-top: 20px;
        }
    </style>
</head>
<body>
    
    <div id="main">
        <nav>
            <a href="/">
                <img src="https://cdn.inflearn.com/assets/brand/chuseok_logo.png" width="150">
            </a>
            <ul>
                <!-- a 태그로 인해 inflearn_lecture/views.py 의 해당 함수가 실행됨 -->
                <a href="/lecture_list"><li>강의보기</li></a>
                {% if user.is_authenticated %} <!-- 유저가 로그인되어 있을 경우 -->
                    <a href="/logout"><li>로그아웃</li></a>
                {% else %} <!-- 유저가 로그인되어 있지 않을 경우 -->
                    <a href="/login"><li>로그인</li></a>
                    <a href="/join"><li>회원가입</li></a>
                {% endif %}
                <li>메뉴5</li>
            </ul>
        </nav>
    </div>

    {% block content %}
    {% endblock %}

    <div class="footer">
        contact : a@naver.com
    </div>
    
</body>
</html>
```

- 장고 서버 실행

```bash
python manage.py runserver
```

- login 페이지 동작 확인: http://127.0.0.1:8000/login
  - 로그인 진행 (email, pwd 입력) -> 메뉴에 로그아웃 버튼이 보임
  - 로그아웃 진행 -> 메뉴에 로그인, 회원가입 버튼이 보임


### 폴더 트리 참고

```bash
tree -L 5 -o direc_tree.txt
```

```console
django_inflearn_clone
├── LICENSE
├── README.md
├── direc_tree.txt
├── inflearn
│   ├── db.sqlite3
│   ├── inflearn
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── inflearn_lecture
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── inflearn_lecture
│   │   │       ├── base.html
│   │   │       ├── home_list.html
│   │   │       ├── join.html
│   │   │       ├── lecture_list.html
│   │   │       └── login.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

**[⬆ back to top](#-table-of-contents)**

---

## [14] 강의 상세 페이지

### 강의를 클릭했을 때 안 쪽으로 들어가게 제작

- inflearn_lecture/admin.py 수정
  - admin 페이지에서 myText 의 보여질 속성 설정

```python
from django.contrib import admin
from .models import myText

# Register your models here.
class MyTestAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')  # admin 페이지의 myText 리스트(http://127.0.0.1:8000/admin/inflearn_lecture/mytext/)의 어떤 속성을 보여줄 것인가

admin.site.register(myText, MyTestAdmin)  # myText 와 MyTestAdmin 설정을 추가
```

- inflearn_lecture/urls.py 수정
  - 게시글 정보 페이지 url 연결 (inflearn_lecture/views.py 의 lecture_list_info 함수로 연결됨)
  - pk (게시글 id 값) 이용

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_list, name='home_list'),  # views.py 와 연결

    path('lecture_list/', views.lecture_list, name='lecture_list'),
    path('lecture_list/<int:pk>', views.lecture_list_info, name='lecture_list_info'),  # pk: 게시글 id 값

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('join/', views.join, name='join'),
]
```

- inflearn_lecture/views.py 수정
  - templates/inflearn_lecture/lecture_list_info.html 와 연결
  - board_contents 라는 변수에 담아서 board_contents (myText, pk) 데이터를 보냄

```python
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
```

- inflearn_lecture/templates/inflearn_lecture/lecture_list_info.html 생성
  - 게시글 눌렀을 때 보여지는 lecture_list_info/[pk] 페이지
  - 게시글 데이터 출력


```html
{% extends 'inflearn_lecture/base.html' %}

{% block content%}

    <style>
        .contents {
            width: 1000px;
            margin: auto;
            padding: 100px;
        }
    </style>

    <div class="contents">

        {{ board_contents.board_text | safe }} <!-- 텍스트가 아니라 html 로 읽게 만듦 -->
    </div>

{% endblock %}
```

- inflearn_lecture/templates/inflearn_lecture/lecture_list.html 수정
  - 게시글 누르면 lecture_list_info/[pk] 페이지로 연결


```html
{% extends 'inflearn_lecture/base.html' %}

{% block content %}

    <style>
        div {
            float: left
        }

        .left {
            width: 30%;
        }

        .left ul li {
            margin: 10px;
            padding: 10px;
            border: 1px solid gray;
        }

        .right {
            width: 70%;
        }
    </style>

    <div class="left">
        <ul>
            <li>HTML</li>
            <li>CSS</li>
            <li>JS</li>
            <li id="hot_lecture">인기</li>
            <li>추천</li>
        </ul>
    </div>

    <div class="right">
        <div class="row all">
            {% for text in texts %}
                
                    <div class="col-xs-6 col-md-3">
                        <a href="{% url 'lecture_list_info' pk=text.pk %}" class="thumbnail"> <!-- lecture_list_info/[pk] 페이지로 연결 -->
                            <img src="../../media/{{ text.img_url }}" alt="../../media/{{ text.img_url }}">
                            <div class="caption">
                                <h3>{{ text.title }}</h3>
                            </div>
                        </a>
                    </div>
                
        
            {% endfor %}
        </div>

        <div class="row hot">
            {% for text in hot_lecture %}

                    <div class="col-xs-6 col-md-3">
                        <a href="{% url 'lecture_list_info' pk=text.pk %}" class="thumbnail"> <!-- lecture_list_info/[pk] 페이지로 연결 -->
                            <img src="../../media/{{ text.img_url }}" alt="../../media/{{ text.img_url }}">
                            <div class="caption">
                                <h3>{{ text.title }}</h3>
                            </div>
                        </a>
                    </div>
        
            {% endfor %}
        </div>
    </div>

    <script>
        // 제이쿼리 사용
        $('#hot_lecture').click(function(){
            $('.row').hide();
            $('.hot').show();
        });
    </script>

{% endblock %}
```

- inflearn_lecture/templates/inflearn_lecture/home_list.html 수정
  - 게시글 누르면 lecture_list_info/[pk] 페이지로 연결

```html
{% extends 'inflearn_lecture/base.html' %}

{% block content %}

    <h2>인기 강의</h2>

    <!-- texts: db 에 있는 myText 데이터 -->
    <div class="row">
        {% for text in texts %}
            
                <div class="col-xs-6 col-md-3">
                    <a href="{% url 'lecture_list_info' pk=text.pk %}" class="thumbnail"> <!-- lecture_list_info/[pk] 페이지로 연결 -->
                        <img src="../../media/{{ text.img_url }}" alt="../../media/{{ text.img_url }}">
                        <div class="caption">
                            <h3>{{ text.title }}</h3>
                        </div>
                    </a>
                </div>            

        {% endfor %}
    </div>

{% endblock %}
```

- 장고 서버 실행

```bash
python manage.py runserver
```

- 동작 확인: 홈(http://127.0.0.1:8000/), 강의보기(http://127.0.0.1:8000/lecture_list/), 게시글 정보(http://127.0.0.1:8000/lecture_list/[pk])
  - 홈 에서 게시글 누르면 게시글 정보 페이지로 넘어감
  - 강의보기 에서 게시글 누르면 게시글 정보 페이지로 넘어감


### 폴더 트리 참고

```bash
tree -L 5 -o direc_tree.txt
```

```console
django_inflearn_clone
├── LICENSE
├── README.md
├── direc_tree.txt
├── inflearn
│   ├── db.sqlite3
│   ├── inflearn
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── inflearn_lecture
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── inflearn_lecture
│   │   │       ├── base.html
│   │   │       ├── home_list.html
│   │   │       ├── join.html
│   │   │       ├── lecture_list.html
│   │   │       ├── lecture_list_info.html
│   │   │       └── login.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

**[⬆ back to top](#-table-of-contents)**

---

## [15] 댓글 폼 만들기

- inflearn_lecture/templates/inflearn_lecture/lecture_list_info.html 수정
  - login.html 재활용해서 댓글 html 틀 잡음


```html
{% extends 'inflearn_lecture/base.html' %}

{% block content%}

    <style>
        .contents {
            width: 1000px;
            margin: auto;
            padding: 100px;
        }
    </style>

    <div class="contents">

        {{ board_contents.board_text | safe }} <!-- 텍스트가 아니라 html 로 읽게 만듦 -->
    </div>

    <!-- login.html 재활용 -->
    <div style="width: 800px; margin: auto;">
        <form method="POST" action="{% url 'lecture_list_info' pk=board_contents.pk %}">
            {% csrf_token %}  <!-- 보안 설정 -->
            <div class="form-group">
                <label for="exampleInputEmail1">평점</label>
                <input name="rate" type="number" class="form-control" placeholder="평점"/>
            </div>
            <div class="form-group">
                <label for="exampleInputPassword1">글쓴이</label>
                <input name="writer" type="text" class="form-control" placeholder="글쓴이"/>
            </div>
            <div class="form-group">
                <label for="exampleInputPassword1">댓글</label>
                <input name="comment" type="text" class="form-control" placeholder="댓글"/>
            </div>

            <button type="submit" class="btn btn-default">제출</button>
        </form>
    </div>

{% endblock %}
```

- 장고 서버 실행

```bash
python manage.py runserver
```

- 게시글 정보 페이지 확인: http://127.0.0.1:8000/lecture_list/[pk]


### 폴더 트리 참고

```bash
tree -L 5 -o direc_tree.txt
```

```console
django_inflearn_clone
├── LICENSE
├── README.md
├── direc_tree.txt
├── inflearn
│   ├── db.sqlite3
│   ├── inflearn
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── inflearn_lecture
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── inflearn_lecture
│   │   │       ├── base.html
│   │   │       ├── home_list.html
│   │   │       ├── join.html
│   │   │       ├── lecture_list.html
│   │   │       ├── lecture_list_info.html
│   │   │       └── login.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

**[⬆ back to top](#-table-of-contents)**

---

## [16] 댓글 기능 구현

- inflearn_lecture/templates/inflearn_lecture/lecture_list_info.html 수정
  - html 에서 views 로 form 데이터 넘김


```html
{% extends 'inflearn_lecture/base.html' %}

{% block content%}

    <style>
        .contents {
            width: 1000px;
            margin: auto;
            padding: 100px;
        }
    </style>

    <div class="contents">

        {{ board_contents.board_text | safe }} <!-- 텍스트가 아니라 html 로 읽게 만듦 -->
    </div>

    <!-- login.html 재활용 -->
    <div style="width: 800px; margin: auto;">
        <!-- html 에서 views 로 form 데이터 넘김 -->
        <form method="POST" action="{% url 'lecture_list_info' pk=board_contents.pk %}">
            {% csrf_token %}  <!-- 보안 설정 -->
            <div class="form-group">
                <label for="exampleInputEmail1">평점</label>
                <input name="rate" type="number" class="form-control" placeholder="평점"/>
            </div>
            <div class="form-group">
                <label for="exampleInputPassword1">글쓴이</label>
                <input name="writer" type="text" class="form-control" placeholder="글쓴이"/>
            </div>
            <div class="form-group">
                <label for="exampleInputPassword1">댓글</label>
                <input name="comment" type="text" class="form-control" placeholder="댓글"/>
            </div>

            <button type="submit" class="btn btn-default">제출</button>
        </form>
    </div>

{% endblock %}
```

- inflearn_lecture/models.py 수정
  - 댓글 폼 만들었으니 모델 만들어야 함

```python
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class myText(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 게시글을 작성자로 구분 - 누가 이 강의를 작성했는가
    title = models.CharField(max_length=200)
    contents = models.CharField(max_length=200)
    img_url = models.FileField(null=True)

    category = models.CharField(max_length=200, null=True)  # 카테고리 설정

    board_text = RichTextUploadingField(null=True)  # ckeditor

    def publish(self):
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):    
    lecture = models.ForeignKey(myText, on_delete=models.CASCADE)  # 댓글을 게시글로 구분 - 어떤 강의에 댓글이 달렸는가
    
    writer = models.CharField(max_length=200, null=True)
    rate = models.CharField(max_length=200, null=True)
    comment = models.CharField(max_length=200, null=True)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.comment
```

- db 처리

```bash
python manage.py makemigrations
python manage.py migrate
```

- inflearn_lecture/views.py 수정
  - lecture_list_info 함수 수정해서 댓글 기능 구현

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import myText, Comment


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

    if request.method == 'POST':  # POST 요청이 들어오면 댓글 생성 진행
        rate = request.POST['rate']
        writer = request.POST['writer']
        comment = request.POST['comment']

        Comment.objects.create(lecture=board_contents,
                                writer=writer,
                                rate=rate,
                                comment=comment
                                )  # 댓글 생성
        
        return redirect('/lecture_list/' + str(pk))

    return render(request, 'inflearn_lecture/lecture_list_info.html', {'board_contents': board_contents})  # templates/inflearn_lecture/lecture_list_info.html 와 연결, board_contents 라는 변수에 담아서 board_contents (myText, pk) 데이터를 보냄
```

- inflearn_lecture/admin.py 수정
  - Comment 모델이 admin 페이지에서 보이도록 설정

```python
from django.contrib import admin
from .models import myText, Comment

# Register your models here.
class MyTestAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')  # admin 페이지의 myText 리스트(http://127.0.0.1:8000/admin/inflearn_lecture/mytext/)의 어떤 속성을 보여줄 것인가

admin.site.register(myText, MyTestAdmin)  # myText 와 MyTestAdmin 설정을 추가
admin.site.register(Comment)
```

- db 처리

```bash
python manage.py makemigrations
python manage.py migrate
```

- 장고 서버 실행

```bash
python manage.py runserver
```

- 게시글 정보 페이지에서 댓글 1개 작성: http://127.0.0.1:8000/lecture_list/[pk]
- 관리자 페이지에서 생성된 댓글 확인: http://127.0.0.1:8000/admin/inflearn_lecture/comment/


### 폴더 트리 참고

```bash
tree -L 5 -o direc_tree.txt
```

```console
django_inflearn_clone
├── LICENSE
├── README.md
├── direc_tree.txt
├── inflearn
│   ├── db.sqlite3
│   ├── inflearn
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── inflearn_lecture
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── inflearn_lecture
│   │   │       ├── base.html
│   │   │       ├── home_list.html
│   │   │       ├── join.html
│   │   │       ├── lecture_list.html
│   │   │       ├── lecture_list_info.html
│   │   │       └── login.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

**[⬆ back to top](#-table-of-contents)**

---

## [17] 댓글 보이기 (in HTML)

- inflearn_lecture/views.py 수정
  - 현재 로그인한 유저 이름, 댓글 확인
  - 댓글 데이터를 html 에 보냄

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import myText, Comment


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
    print('**** comment?',comment)

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
```

- inflearn_lecture/templates/inflearn_lecture/lecture_list_info.html 수정
  - views 에서 해당 게시글 댓글 데이터 받아와서 페이지에 댓글 출력


```html
{% extends 'inflearn_lecture/base.html' %}

{% block content %}

    <style>
        .contents {
            width: 1000px;
            margin: auto;
            padding: 100px;
        }
    </style>

    <div class="contents">

        {{ board_contents.board_text | safe }} <!-- 텍스트가 아니라 html 로 읽게 만듦 -->
    </div>

    <!-- login.html 재활용 -->
    <div style="width: 800px; margin: auto;">
        <!-- html 에서 views 로 form 데이터 넘김 -->
        <form method="POST" action="{% url 'lecture_list_info' pk=board_contents.pk %}">
            {% csrf_token %}  <!-- 보안 설정 -->
            <div class="form-group">
                <label for="exampleInputEmail1">평점</label>
                <input name="rate" type="number" class="form-control" placeholder="평점"/>
            </div>
            <div class="form-group">
                <label for="exampleInputPassword1">글쓴이</label>
                <input name="writer" type="text" class="form-control" placeholder="글쓴이"/>
            </div>
            <div class="form-group">
                <label for="exampleInputPassword1">댓글</label>
                <input name="comment" type="text" class="form-control" placeholder="댓글"/>
            </div>

            <button type="submit" class="btn btn-default">제출</button>
        </form>
    </div>

    <!-- 댓글 보여주기 -->
    <div style="width: 800px; margin: auto; padding: 10px;">
        {% for comment_item in comment %}
            <div style="border: 1px solid gray; border-radius: 10px;">

                <h2>writer: {{ comment_item.writer }}</h2>
                <h2>rate: {{ comment_item.rate }}</h2>
                <h2>comment: {{ comment_item.comment }}</h2>

            </div>
        {% endfor %}
    </div>

{% endblock %}
```

- 장고 서버 실행

```bash
python manage.py runserver
```

- 게시글 정보 페이지에서 댓글 확인: http://127.0.0.1:8000/lecture_list/[pk]


### 폴더 트리 참고

```bash
tree -L 5 -o direc_tree.txt
```

```console
django_inflearn_clone
├── LICENSE
├── README.md
├── direc_tree.txt
├── inflearn
│   ├── db.sqlite3
│   ├── inflearn
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── inflearn_lecture
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── inflearn_lecture
│   │   │       ├── base.html
│   │   │       ├── home_list.html
│   │   │       ├── join.html
│   │   │       ├── lecture_list.html
│   │   │       ├── lecture_list_info.html
│   │   │       └── login.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

**[⬆ back to top](#-table-of-contents)**

---

## [18] 댓글 삭제

- inflearn_lecture/admin.py 수정
  - admin 페이지에서 Coment 의 보여질 속성 설정

```python
from django.contrib import admin
from .models import myText, Comment

# Register your models here.
class MyTestAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')  # admin 페이지의 myText 리스트(http://127.0.0.1:8000/admin/inflearn_lecture/mytext/)의 어떤 속성을 보여줄 것인가

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'comment')

admin.site.register(myText, MyTestAdmin)  # myText 와 MyTestAdmin 설정을 추가
admin.site.register(Comment, CommentAdmin)
```

- inflearn_lecture/urls.py 수정
  - comment_remove 추가 (inflearn_lecture/views.py 의 comment_remove 함수로 연결됨)
  - pk (게시글 id 값) 이용

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_list, name='home_list'),  # views.py 와 연결

    path('lecture_list/', views.lecture_list, name='lecture_list'),
    path('lecture_list/<int:pk>', views.lecture_list_info, name='lecture_list_info'),  # pk: 게시글 id 값

    path('comment_remove/<int:pk>', views.comment_remove, name='comment_remove'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('join/', views.join, name='join'),
]
```

- inflearn_lecture/views.py 수정
  - comment_delete 함수 작성, POST 요청 들어오면 댓글 삭제 진행

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import myText, Comment


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
```

- inflearn_lecture/templates/inflearn_lecture/lecture_list_info.html 수정
  - html 에서 views 로 form 데이터 넘김
  - 보안을 위해 csrf_token 설정


```html
{% extends 'inflearn_lecture/base.html' %}

{% block content %}

    <style>
        .contents {
            width: 1000px;
            margin: auto;
            padding: 100px;
        }
    </style>

    <div class="contents">

        {{ board_contents.board_text | safe }} <!-- 텍스트가 아니라 html 로 읽게 만듦 -->
    </div>

    <!-- 댓글 작성 폼, login.html 재활용 -->
    <div style="width: 800px; margin: auto;">
        <!-- html 에서 views 로 form 데이터 넘김 -->
        <form method="POST" action="{% url 'lecture_list_info' pk=board_contents.pk %}">
            {% csrf_token %}  <!-- 보안 설정 -->
            <div class="form-group">
                <label for="exampleInputEmail1">평점</label>
                <input name="rate" type="number" class="form-control" placeholder="평점"/>
            </div>
            <div class="form-group">
                <label for="exampleInputPassword1">글쓴이</label>
                <input name="writer" type="text" class="form-control" placeholder="글쓴이"/>
            </div>
            <div class="form-group">
                <label for="exampleInputPassword1">댓글</label>
                <input name="comment" type="text" class="form-control" placeholder="댓글"/>
            </div>

            <button type="submit" class="btn btn-default">제출</button>
        </form>
    </div>

    <!-- 작성된 댓글 보여주기 -->
    <div style="width: 800px; margin: auto; padding: 10px;">
        {% for comment_item in comment %}
            <div style="border: 1px solid gray; border-radius: 10px;">

                <h2>writer: {{ comment_item.writer }}</h2>
                <h2>rate: {{ comment_item.rate }}</h2>
                <h2>comment: {{ comment_item.comment }}</h2>

                <!-- 댓글 삭제, html 에서 views 로 form 데이터 넘김 -->
                <form method="POST" action="{% url 'comment_remove' pk=comment_item.pk %}">
                    {% csrf_token %}
                    <button>삭제하기</button>
                </form>

            </div>
        {% endfor %}
    </div>

{% endblock %}
```

- 장고 서버 실행

```bash
python manage.py runserver
```

- 댓글 삭제 동작 확인
  - 게시글 정보 페이지에서 댓글 삭제 버튼 클릭: http://127.0.0.1:8000/lecture_list/[pk]
  - 관리자 페이지에서 진짜로 댓글이 삭제됐는지 확인: http://127.0.0.1:8000/admin/inflearn_lecture/comment/

### 폴더 트리 참고

```bash
tree -L 5 -o direc_tree.txt
```

```console
django_inflearn_clone
├── LICENSE
├── README.md
├── direc_tree.txt
├── inflearn
│   ├── db.sqlite3
│   ├── inflearn
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── inflearn_lecture
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── inflearn_lecture
│   │   │       ├── base.html
│   │   │       ├── home_list.html
│   │   │       ├── join.html
│   │   │       ├── lecture_list.html
│   │   │       ├── lecture_list_info.html
│   │   │       └── login.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

**[⬆ back to top](#-table-of-contents)**

---

## [19] 강의보기 리스트 만들기

- inflearn_lecture/models.py 수정
  - 강의 섹션 4개로 고정시키고 하드 코딩
  - 실제로는 강의 섹션이 점점 늘어나는 것까지 고려해서 리스트 형식(가변 데이터)으로 받아야 함 => 'django model list' 구글링

```python
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class myText(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 게시글을 작성자로 구분 - 누가 이 강의를 작성했는가
    title = models.CharField(max_length=200)
    contents = models.CharField(max_length=200)
    img_url = models.FileField(null=True)

    category = models.CharField(max_length=200, null=True)  # 카테고리 설정

    board_text = RichTextUploadingField(null=True)  # ckeditor

    # 강의 섹션 4개로 고정시키고 하드 코딩
    # - 실제로는 강의 섹션이 점점 늘어나는 것까지 고려해서 리스트 형식(가변 데이터)으로 받아야 함 => 'django model list' 구글링
    lecture_title1 = models.CharField(max_length=200, null=True)
    lecture_video1 = models.CharField(max_length=200, null=True)
    lecture_title2 = models.CharField(max_length=200, null=True)
    lecture_video2 = models.CharField(max_length=200, null=True)
    lecture_title3 = models.CharField(max_length=200, null=True)
    lecture_video3 = models.CharField(max_length=200, null=True)
    lecture_title4 = models.CharField(max_length=200, null=True)
    lecture_video4 = models.CharField(max_length=200, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):    
    lecture = models.ForeignKey(myText, on_delete=models.CASCADE)  # 댓글을 게시글로 구분 - 어떤 강의에 댓글이 달렸는가
    
    writer = models.CharField(max_length=200, null=True)
    rate = models.CharField(max_length=200, null=True)
    comment = models.CharField(max_length=200, null=True)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.comment
```

- db 처리

```bash
python manage.py makemigrations
python manage.py migrate
```

- 장고 서버 실행

```bash
python manage.py runserver
```

- 관리자 페이지에서 강의 섹션 값 추가해서 게시글 수정: http://127.0.0.1:8000/admin/inflearn_lecture/mytext/
  - lecture_title, lecture_video 값 추가
  - lecture_video 에는 유튜브 영상 iframe 코드 값 복붙 (유튜브 - 공유 - 퍼가기 - 코드복사)

- inflearn_lecture/templates/inflearn_lecture/lecture_list_info.html 수정
  - 강의 섹션 리스트 보이게 하드 코딩 진행
  - 반복문으로 고칠 수 있으면 고치는 것 추천


```html
{% extends 'inflearn_lecture/base.html' %}

{% block content %}

    <style>
        .contents {
            width: 1000px;
            margin: auto;
            padding: 100px;
        }
    </style>

    <div class="contents">

        {{ board_contents.board_text | safe }} <!-- 텍스트가 아니라 html 로 읽게 만듦 -->
    </div>

    <!-- 댓글 작성 폼, login.html 재활용 -->
    <div style="width: 800px; margin: auto;">
        <!-- html 에서 views 로 form 데이터 넘김 -->
        <form method="POST" action="{% url 'lecture_list_info' pk=board_contents.pk %}">
            {% csrf_token %}  <!-- 보안 설정 -->
            <div class="form-group">
                <label for="exampleInputEmail1">평점</label>
                <input name="rate" type="number" class="form-control" placeholder="평점"/>
            </div>
            <div class="form-group">
                <label for="exampleInputPassword1">글쓴이</label>
                <input name="writer" type="text" class="form-control" placeholder="글쓴이"/>
            </div>
            <div class="form-group">
                <label for="exampleInputPassword1">댓글</label>
                <input name="comment" type="text" class="form-control" placeholder="댓글"/>
            </div>

            <button type="submit" class="btn btn-default">제출</button>
        </form>
    </div>

    <!-- 강의 섹션 리스트 (하드 코딩이라 반복문으로 고칠 수 있으면 고치는 것 추천) -->
    <div>
        <style>
            tr {
                border: 1px solid gray;
                padding: 10px;
                background-color: lightgray;
            }
        </style>

        <table style="width: 500px; margin: auto;">
            <tr>
                {% if board_contents.lecture_title1 %}
                    <td>{{ board_contents.lecture_title1 }}</td>
                {% endif %}
            </tr>

            <tr>
                {% if board_contents.lecture_title2 %}
                    <td>{{ board_contents.lecture_title2 }}</td>
                {% endif %}
            </tr>

            <tr>
                {% if board_contents.lecture_title3 %}
                    <td>{{ board_contents.lecture_title3 }}</td>
                {% endif %}
            </tr>

            <tr>
                {% if board_contents.lecture_title4 %}
                    <td>{{ board_contents.lecture_title4 }}</td>
                {% endif %}
            </tr>
        </table>
    </div>

    <!-- 작성된 댓글 보여주기 -->
    <div style="width: 800px; margin: auto; padding: 10px;">
        {% for comment_item in comment %}
            <div style="border: 1px solid gray; border-radius: 10px;">

                <h2>writer: {{ comment_item.writer }}</h2>
                <h2>rate: {{ comment_item.rate }}</h2>
                <h2>comment: {{ comment_item.comment }}</h2>

                <!-- 댓글 삭제, html 에서 views 로 form 데이터 넘김 -->
                <form method="POST" action="{% url 'comment_remove' pk=comment_item.pk %}">
                    {% csrf_token %}
                    <button>삭제하기</button>
                </form>

            </div>
        {% endfor %}
    </div>

{% endblock %}
```

- 게시글 정보 페이지에서 강의 섹션 리스트 확인: http://127.0.0.1:8000/lecture_list/[pk]

### 폴더 트리 참고

```bash
tree -L 5 -o direc_tree.txt
```

```console
django_inflearn_clone
├── LICENSE
├── README.md
├── direc_tree.txt
├── inflearn
│   ├── db.sqlite3
│   ├── inflearn
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── inflearn_lecture
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── inflearn_lecture
│   │   │       ├── base.html
│   │   │       ├── home_list.html
│   │   │       ├── join.html
│   │   │       ├── lecture_list.html
│   │   │       ├── lecture_list_info.html
│   │   │       └── login.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

**[⬆ back to top](#-table-of-contents)**

---

## [20] 강의보기 페이지 만들기

- inflearn_lecture/models.py 수정
  - lecture_video 에서 max_length=500 으로 수정
  - 유튜브 영상 iframe 코드 값이 max_length=200 으로는 잘리기 때문 => 500 으로 늘려야 잘리지 않고 제대로 저장됨

```python
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class myText(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 게시글을 작성자로 구분 - 누가 이 강의를 작성했는가
    title = models.CharField(max_length=200)
    contents = models.CharField(max_length=200)
    img_url = models.FileField(null=True)

    category = models.CharField(max_length=200, null=True)  # 카테고리 설정

    board_text = RichTextUploadingField(null=True)  # ckeditor

    # 강의 섹션 4개로 고정시키고 하드 코딩
    # - 실제로는 강의 섹션이 점점 늘어나는 것까지 고려해서 리스트 형식(가변 데이터)으로 받아야 함 => 'django model list' 구글링
    lecture_title1 = models.CharField(max_length=200, null=True)
    lecture_video1 = models.CharField(max_length=500, null=True)
    lecture_title2 = models.CharField(max_length=200, null=True)
    lecture_video2 = models.CharField(max_length=500, null=True)
    lecture_title3 = models.CharField(max_length=200, null=True)
    lecture_video3 = models.CharField(max_length=500, null=True)
    lecture_title4 = models.CharField(max_length=200, null=True)
    lecture_video4 = models.CharField(max_length=500, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):    
    lecture = models.ForeignKey(myText, on_delete=models.CASCADE)  # 댓글을 게시글로 구분 - 어떤 강의에 댓글이 달렸는가
    
    writer = models.CharField(max_length=200, null=True)
    rate = models.CharField(max_length=200, null=True)
    comment = models.CharField(max_length=200, null=True)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.comment
```

- db 처리

```bash
python manage.py makemigrations
python manage.py migrate
```

- 장고 서버 실행

```bash
python manage.py runserver
```

- 관리자 페이지에서 강의 섹션 값 수정: http://127.0.0.1:8000/admin/inflearn_lecture/mytext/
  - lecture_video 값 수정
  - lecture_video 에는 유튜브 영상 iframe 코드 값 복붙 (유튜브 - 공유 - 퍼가기 - 코드복사)

- inflearn_lecture/urls.py
  - show_lecture 추가


```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_list, name='home_list'),  # views.py 와 연결

    path('lecture_list/', views.lecture_list, name='lecture_list'),
    path('lecture_list/<int:pk>', views.lecture_list_info, name='lecture_list_info'),  # pk: 게시글 id 값

    path('comment_remove/<int:pk>', views.comment_remove, name='comment_remove'),
    path('show_lecture/<int:pk>', views.show_lecture, name='show_lecture'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('join/', views.join, name='join'),
]
```

- inflearn_lecture/views.py
  - show_lecture 함수 작성, 강의보기 페이지로 이동

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import myText, Comment


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
```

- inflearn_lecture/templates/inflearn_lecture/show_lecture.html 생성
  - 강의 보기 페이지
  - 왼쪽에는 영상, 오른쪽에는 강의 섹션 리스트가 보이도록 설정
  - safe 옵션: Text -> HTML


```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div {
            float: left;
        }

        .left {
            width: 70%;
        }

        .right {
            width: 30%
        }

        ul li {
            list-style: none;
            margin: 10px;
            padding: 10px;
            border: 1px solid gray;
        }

        iframe {
            width: 100%;
            height: 600px;
        }
    </style>
</head>
<body>

    <div class="left">
        <!-- safe 옵션: Text -> HTML -->
        {{ board_contents.lecture_video1 | safe }}
    </div>

    <div class="right">
        <ul>
            <li>{{board_contents.lecture_title1}}</li>
            <li>{{board_contents.lecture_title2}}</li>
            <li>{{board_contents.lecture_title3}}</li>
            <li>{{board_contents.lecture_title4}}</li>
        </ul>
    </div>

</body>
</html>
```

- 강의 보기 페이지 확인: http://127.0.0.1:8000/show_lecture/[pk]
  - 유튜브 영상이 제대로 임베딩되어 보여지는지 확인
  - 강의 섹션 타이틀이 제대로 보이는지 확인


### 폴더 트리 참고

```bash
tree -L 5 -o direc_tree.txt
```

```console
django_inflearn_clone
├── LICENSE
├── README.md
├── direc_tree.txt
├── inflearn
│   ├── db.sqlite3
│   ├── inflearn
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── inflearn_lecture
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── inflearn_lecture
│   │   │       ├── base.html
│   │   │       ├── home_list.html
│   │   │       ├── join.html
│   │   │       ├── lecture_list.html
│   │   │       ├── lecture_list_info.html
│   │   │       ├── login.html
│   │   │       └── show_lecture.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

**[⬆ back to top](#-table-of-contents)**

---

## [21] jQeury로 탭 만들기

- inflearn_lecture/templates/inflearn_lecture/show_lecture.html 수정
  - 처음 페이지 접속하면 첫 번째 강의 영상만 보여지게 설정
  - 탭 전환 기능 jQuery 를 통해 구현 - 강의 섹션 타이틀 클릭하면 해당 강의 영상이 보여지게 설정


```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <!-- 제이쿼리 CDN -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>

    <style>
        div {
            float: left;
        }

        .left {
            width: 70%;
        }

        .right {
            width: 30%
        }

        ul li {
            list-style: none;
            margin: 10px;
            padding: 10px;
            border: 1px solid gray;
        }

        iframe {
            width: 100%;
            height: 600px;
        }
    </style>
</head>
<body>

    <!-- 영상 -->
    <div class="left lecture1">
        <!-- safe 옵션: Text -> HTML -->
        {{ board_contents.lecture_video1 | safe }}
    </div>

    <!-- style="display: none;" 옵션: 처음에는 보이지 않게 설정 -->
    <div class="left lecture2" style="display: none;">
        {{ board_contents.lecture_video2 | safe }}
    </div>

    <div class="left lecture3" style="display: none;">
        {{ board_contents.lecture_video3 | safe }}
    </div>

    <div class="left lecture4" style="display: none;">
        {{ board_contents.lecture_video4 | safe }}
    </div>

    <!-- 타이틀 -->
    <div class="right">
        <ul>
            <li class="menu" id="title1">{{board_contents.lecture_title1}}</li>
            <li class="menu" id="title2">{{board_contents.lecture_title2}}</li>
            <li class="menu" id="title3">{{board_contents.lecture_title3}}</li>
            <li class="menu" id="title4">{{board_contents.lecture_title4}}</li>
        </ul>
    </div>

    <!-- jQuery -->
    <script>
        $('#title1').click(function(){
            $('.left').hide();
            $('.lecture1').show();
            $('.menu').css('color', 'black');
            $('#title1').css('color', 'red');
        });

        $('#title2').click(function(){
            $('.left').hide();
            $('.lecture2').show();
            $('.menu').css('color', 'black');
            $('#title2').css('color', 'red');
        });

        $('#title3').click(function(){
            $('.left').hide();
            $('.lecture3').show();
            $('.menu').css('color', 'black');
            $('#title3').css('color', 'red');
        });

        $('#title4').click(function(){
            $('.left').hide();
            $('.lecture4').show();
            $('.menu').css('color', 'black');
            $('#title4').css('color', 'red');
        });
    </script>

</body>
</html>
```

- 강의 보기 페이지 탭 전환 동작 확인: http://127.0.0.1:8000/show_lecture/[pk]

### 폴더 트리 참고

```bash
tree -L 5 -o direc_tree.txt
```

```console
django_inflearn_clone
├── LICENSE
├── README.md
├── direc_tree.txt
├── inflearn
│   ├── db.sqlite3
│   ├── inflearn
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── inflearn_lecture
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── inflearn_lecture
│   │   │       ├── base.html
│   │   │       ├── home_list.html
│   │   │       ├── join.html
│   │   │       ├── lecture_list.html
│   │   │       ├── lecture_list_info.html
│   │   │       ├── login.html
│   │   │       └── show_lecture.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

**[⬆ back to top](#-table-of-contents)**

---

## [22] 사용자 강의 만들기

- inflearn_lecture/views.py 수정
  - create_lecture 함수 작성

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import myText, Comment


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
    return render(request, 'inflearn_lecture/create_lecture.html')
```

- inflearn_lecture/urls.py 수정
  - create_lecture 추가


```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_list, name='home_list'),  # views.py 와 연결

    path('lecture_list/', views.lecture_list, name='lecture_list'),
    path('lecture_list/<int:pk>', views.lecture_list_info, name='lecture_list_info'),  # pk: 게시글 id 값

    path('comment_remove/<int:pk>', views.comment_remove, name='comment_remove'),
    path('show_lecture/<int:pk>', views.show_lecture, name='show_lecture'),
    path('create_lecture/', views.create_lecture, name='create_lecture'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('join/', views.join, name='join'),
]
```

- inflearn_lecture/templates/inflearn_lecture/create_lecture.html 생성
  - 관리자 페이지가 아니라 사용자가 직접 강의를 추가/수정할 수 있게 작성
  - 사용자 강의 만들기 form 역할
  - 아직 코드 작성 안 함
- inflearn_lecture/templates/inflearn_lecture/base.html 수정
  - 홈에서 강의 만들기 메뉴 a 태그로 생성

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>인프런 따라만들기</title>

    <!-- 제이쿼리 CDN -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>

    <!-- 부트스트랩 CDN -->
    <!-- 합쳐지고 최소화된 최신 CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">

    <!-- 부가적인 테마 -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">

    <!-- 합쳐지고 최소화된 최신 자바스크립트 -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>

    <!-- CSS -->
    <style>
        * {
            margin: 0px;
            padding: 0px;
        }

        #main {
            width: 100%;
            height:50vh;
            background-image: url("https://cdn.inflearn.com/public/main_sliders/e85e0c0a-c4ba-46bb-8e73-5c647b72db19/newsletter-infocus-03-main-521.png");
        }

        nav {
            width: 100%;
            height: 60px;
            background-color: white;
            line-height: 50px;
        }

        nav ul {
            float: right;
        }

        nav ul a {
            color: green;
        }

        nav ul li {
            margin: 10px;
            list-style-type: none;
            display: inline-block;
        }

        .footer {
            left: 0;
            bottom: 0;
            width: 100%;
            height: 50px;
            background-color: green;
            text-align: center;
            padding-top: 20px;
        }
    </style>
</head>
<body>
    
    <div id="main">
        <nav>
            <a href="/">
                <img src="https://cdn.inflearn.com/assets/brand/chuseok_logo.png" width="150">
            </a>
            <ul>
                <!-- a 태그로 인해 inflearn_lecture/views.py 의 해당 함수가 실행됨 -->
                <a href="/lecture_list"><li>강의보기</li></a>
                {% if user.is_authenticated %} <!-- 유저가 로그인되어 있을 경우 -->
                    <a href="/logout"><li>로그아웃</li></a>
                    <a href="/create_lecture"><li>강의 만들기</li></a>
                {% else %} <!-- 유저가 로그인되어 있지 않을 경우 -->
                    <a href="/login"><li>로그인</li></a>
                    <a href="/join"><li>회원가입</li></a>
                {% endif %}
            </ul>
        </nav>
    </div>

    {% block content %}
    {% endblock %}

    <div class="footer">
        contact : a@naver.com
    </div>
    
</body>
</html>
```

### 폴더 트리 참고

```bash
tree -L 5 -o direc_tree.txt
```

```console
django_inflearn_clone
├── LICENSE
├── README.md
├── direc_tree.txt
├── inflearn
│   ├── db.sqlite3
│   ├── inflearn
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── inflearn_lecture
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── inflearn_lecture
│   │   │       ├── base.html
│   │   │       ├── create_lecture.html
│   │   │       ├── home_list.html
│   │   │       ├── join.html
│   │   │       ├── lecture_list.html
│   │   │       ├── lecture_list_info.html
│   │   │       ├── login.html
│   │   │       └── show_lecture.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

**[⬆ back to top](#-table-of-contents)**

---

## [23] 사용자 강의 만들기 기능 구현

- inflearn_lecture/forms.py 생성
  - 장고 폼 작성
    - 빈 form 이 있는 페이지 -> 사용자가 데이터를 입력하고 form 제출 -> 데이터 검증 -> 데이터가 유효할 경우 데이터를 통과시켜 그에 따른 action 을 취하고 성공 URL 로 redirect, 데이터가 유효하지 않을 경우 에러 메세지와 함께 form 이 있던 페이지로 보냄
    - [django forms.py 에 대한 글 참고](https://hwan-hobby.tistory.com/103)
  - 강의 생성을 위한 폼
  - 폼에 들어갈 모델(myText) 의 항목(fields) 설정
  - 만든 폼은 views.py 에서 사용됨

```python
from django import forms
from .models import myText


# 장고 폼 작성. 만든 폼은 views.py 에서 사용됨
class LectureForm(forms.ModelForm):
    # 폼에 들어갈 모델(myText) 의 항목(fields) 설정
    class Meta:
        model = myText
        fields = (
            # '__all__': 모든 항목
            'title',
            'contents',
            'img_url',
            'category',
            'board_text',
            'lecture_title1',
            'lecture_video1',
            'lecture_title2',
            'lecture_video2',
            'lecture_title3',
            'lecture_video3',
            'lecture_title4',
            'lecture_video4',
        )
```

- inflearn_lecture/views.py 수정
  - create_lecture 함수 수정해서 강의 만들기 기능 구현

```python
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
```

- inflearn_lecture/templates/inflearn_lecture/create_lecture.html 수정
  - html 에서 views 로 form 데이터 넘김
  - 파일이 포함된 폼을 서버로 전송하려면 form 태그 method="POST" enctype="multipart/form-data" 속성값을 지정해야만 오류가 발생하지 않음

```html
{% extends 'inflearn_lecture/base.html' %}

{% block content %}

    <div style="width: 700px; margin: auto; padding: 40px;">
        <!-- enctype 속성: 폼 데이터가 서버로 전송될 때 해당 데이터가 인코딩되는 방식, POST 에만 사용 가능 -->
        <!-- enctype="multipart/form-data": 파일/이미지가 포함된 폼을 전송할 때 사용 -->
        <form action="{% url 'create_lecture' %}" method="POST" enctype="multipart/form-data">
            {% csrf_token %} <!-- 보안 설정 -->
            {{ lecture_form.as_p }}
            <button type="submit">저장</button>
        </form>
    </div>

{% endblock %}
```

- 강의 만들기 페이지 동작 확인: http://127.0.0.1:8000/create_lecture/

### 폴더 트리 참고

```bash
tree -L 5 -o direc_tree.txt
```

```console
django_inflearn_clone
├── LICENSE
├── README.md
├── direc_tree.txt
├── inflearn
│   ├── db.sqlite3
│   ├── inflearn
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── inflearn_lecture
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── inflearn_lecture
│   │   │       ├── base.html
│   │   │       ├── create_lecture.html
│   │   │       ├── home_list.html
│   │   │       ├── join.html
│   │   │       ├── lecture_list.html
│   │   │       ├── lecture_list_info.html
│   │   │       ├── login.html
│   │   │       └── show_lecture.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

**[⬆ back to top](#-table-of-contents)**

---

## [24] 내 강의 보기

- inflearn_lecture/templates/inflearn_lecture/base.html 수정

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>인프런 따라만들기</title>

    <!-- 제이쿼리 CDN -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>

    <!-- 부트스트랩 CDN -->
    <!-- 합쳐지고 최소화된 최신 CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">

    <!-- 부가적인 테마 -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">

    <!-- 합쳐지고 최소화된 최신 자바스크립트 -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>

    <!-- CSS -->
    <style>
        * {
            margin: 0px;
            padding: 0px;
        }

        #main {
            width: 100%;
            height:50vh;
            background-image: url("https://cdn.inflearn.com/public/main_sliders/e85e0c0a-c4ba-46bb-8e73-5c647b72db19/newsletter-infocus-03-main-521.png");
        }

        nav {
            width: 100%;
            height: 60px;
            background-color: white;
            line-height: 50px;
        }

        nav ul {
            float: right;
        }

        nav ul a {
            color: green;
        }

        nav ul li {
            margin: 10px;
            list-style-type: none;
            display: inline-block;
        }

        .footer {
            left: 0;
            bottom: 0;
            width: 100%;
            height: 50px;
            background-color: green;
            text-align: center;
            padding-top: 20px;
        }
    </style>
</head>
<body>
    
    <div id="main">
        <nav>
            <a href="/">
                <img src="https://cdn.inflearn.com/assets/brand/chuseok_logo.png" width="150">
            </a>
            <ul>
                <!-- a 태그로 인해 inflearn_lecture/views.py 의 해당 함수가 실행됨 -->
                <a href="/lecture_list"><li>강의보기</li></a>
                {% if user.is_authenticated %} <!-- 유저가 로그인되어 있을 경우 -->
                    <a href="/logout"><li>로그아웃</li></a>
                    <a href="/create_lecture"><li>강의 만들기</li></a>
                    <a href="/my_lecture"><li>내 강의 보기</li></a>
                {% else %} <!-- 유저가 로그인되어 있지 않을 경우 -->
                    <a href="/login"><li>로그인</li></a>
                    <a href="/join"><li>회원가입</li></a>
                {% endif %}
            </ul>
        </nav>
    </div>

    {% block content %}
    {% endblock %}

    <div class="footer">
        contact : a@naver.com
    </div>
    
</body>
</html>
```

- inflearn_lecture/urls.py 수정

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_list, name='home_list'),  # views.py 와 연결

    path('lecture_list/', views.lecture_list, name='lecture_list'),
    path('lecture_list/<int:pk>', views.lecture_list_info, name='lecture_list_info'),  # pk: 게시글 id 값

    path('comment_remove/<int:pk>', views.comment_remove, name='comment_remove'),
    path('show_lecture/<int:pk>', views.show_lecture, name='show_lecture'),
    path('create_lecture/', views.create_lecture, name='create_lecture'),
    path('my_lecture/', views.my_lecture, name='my_lecture'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('join/', views.join, name='join'),
]
```

- inflearn_lecture/views.py 수정

```python
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
```

- inflearn_lecture/templates/inflearn_lecture/my_lecture.html 생성
  - home_list.html 복붙하고 for 문 texts 에서 lectures 로 수정함

```html
{% extends 'inflearn_lecture/base.html' %}

{% block content %}

    <!-- home_list.html 복붙하고 for 문 texts 에서 lectures 로 수정함 -->
    <!-- texts: db 에 있는 myText 데이터 -->
    <div class="row">
        {% for text in lectures %}
            
                <div class="col-xs-6 col-md-3">
                    <a href="{% url 'lecture_list_info' pk=text.pk %}" class="thumbnail"> <!-- lecture_list_info/[pk] 페이지로 연결 -->
                        <img src="../../media/{{ text.img_url }}" alt="../../media/{{ text.img_url }}">
                        <div class="caption">
                            <h3>{{ text.title }}</h3>
                        </div>
                    </a>
                </div>            

        {% endfor %}
    </div>

{% endblock %}
```

- 내 강의 보기 페이지 확인: http://127.0.0.1:8000/my_lecture/

### 폴더 트리 참고

```bash
tree -L 5 -o direc_tree.txt
```

```console
django_inflearn_clone
├── LICENSE
├── README.md
├── direc_tree.txt
├── inflearn
│   ├── db.sqlite3
│   ├── inflearn
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── inflearn_lecture
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── inflearn_lecture
│   │   │       ├── base.html
│   │   │       ├── create_lecture.html
│   │   │       ├── home_list.html
│   │   │       ├── join.html
│   │   │       ├── lecture_list.html
│   │   │       ├── lecture_list_info.html
│   │   │       ├── login.html
│   │   │       ├── my_lecture.html
│   │   │       └── show_lecture.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

**[⬆ back to top](#-table-of-contents)**

---

## [25] 내 강의 수정하기

- inflearn_lecture/urls.py 수정
  - edit_lecture 추가

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_list, name='home_list'),  # views.py 와 연결

    path('lecture_list/', views.lecture_list, name='lecture_list'),
    path('lecture_list/<int:pk>', views.lecture_list_info, name='lecture_list_info'),  # pk: 게시글 id 값

    path('comment_remove/<int:pk>', views.comment_remove, name='comment_remove'),
    path('show_lecture/<int:pk>', views.show_lecture, name='show_lecture'),
    path('create_lecture/', views.create_lecture, name='create_lecture'),
    path('my_lecture/', views.my_lecture, name='my_lecture'),
    path('edit_lecture/<int:pk>', views.edit_lecture, name='edit_lecture'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('join/', views.join, name='join'),
]
```

- inflearn_lecture/views.py 수정
  - edit_lecture 함수 생성해서 내 강의 수정 기능 구현

```python
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

```

- inflearn_lecture/templates/inflearn_lecture/edit_lecture.html 생성
  - create_lecture.html 복붙하고 url 수정
  - html 에서 views 로 form 데이터 넘김

```html
{% extends 'inflearn_lecture/base.html' %}

{% block content %}

    <!-- create_lecture.html 복붙하고 url 수정함 -->
    <div style="width: 700px; margin: auto; padding: 40px;">
        <!-- enctype 속성: 폼 데이터가 서버로 전송될 때 해당 데이터가 인코딩되는 방식, POST 에만 사용 가능 -->
        <!-- enctype="multipart/form-data": 파일/이미지가 포함된 폼을 전송할 때 사용 -->
        <form action="{% url 'edit_lecture' pk=pk %}" method="POST" enctype="multipart/form-data">
            {% csrf_token %} <!-- 보안 설정 -->
            {{ lecture_form.as_p }}
            <button type="submit">저장</button>
        </form>
    </div>

{% endblock %}
```

- 내 강의 보기에서 강의 수정 동작 확인: http://127.0.0.1:8000/edit_lecture/[pk]

### 폴더 트리 참고

```bash
tree -L 5 -o direc_tree.txt
```

```console
django_inflearn_clone
├── LICENSE
├── README.md
├── direc_tree.txt
├── inflearn
│   ├── db.sqlite3
│   ├── inflearn
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── inflearn_lecture
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── inflearn_lecture
│   │   │       ├── base.html
│   │   │       ├── create_lecture.html
│   │   │       ├── edit_lecture.html
│   │   │       ├── home_list.html
│   │   │       ├── join.html
│   │   │       ├── lecture_list.html
│   │   │       ├── lecture_list_info.html
│   │   │       ├── login.html
│   │   │       ├── my_lecture.html
│   │   │       └── show_lecture.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

**[⬆ back to top](#-table-of-contents)**

---

## [추가] REST API

- 배포 - [Django 로 Rest API 만들기 유튜브 참고][REST_API]

[REST_API]: https://youtube.com/playlist?list=PLfRvc71koCxgCNZl2OPWQ7RDUbXo7aqBb

**[⬆ back to top](#-table-of-contents)**

