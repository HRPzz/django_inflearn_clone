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