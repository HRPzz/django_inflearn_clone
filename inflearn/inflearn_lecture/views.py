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