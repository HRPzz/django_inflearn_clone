from django.shortcuts import render

# Create your views here.
def home_list(request):
    return render(request, 'inflearn_lecture/home_list.html')  # templates/inflearn_lecture/home_list.html 와 연결