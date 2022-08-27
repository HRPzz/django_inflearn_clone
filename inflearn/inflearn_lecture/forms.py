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
