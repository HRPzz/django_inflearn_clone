from django.contrib import admin
from .models import myText, Comment

# Register your models here.
class MyTestAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')  # admin 페이지의 myText 리스트(http://127.0.0.1:8000/admin/inflearn_lecture/mytext/)의 어떤 속성을 보여줄 것인가

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'comment')

admin.site.register(myText, MyTestAdmin)  # myText 와 MyTestAdmin 설정을 추가
admin.site.register(Comment, CommentAdmin)