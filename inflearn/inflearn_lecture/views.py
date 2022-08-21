from django.shortcuts import render
from .models import myText

# Create your views here.
def home_list(request):
    texts = myText.objects.filter(category="HTML")  # db 에 있는 카테고리가 HTML 인 myText 데이터를 모두 가져옴
    return render(request, 'inflearn_lecture/home_list.html', {'texts': texts})  # templates/inflearn_lecture/home_list.html 와 연결, texts 라는 변수에 담아서 myText 데이터를 보냄