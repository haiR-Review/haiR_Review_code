from django import forms
from .models import Question, Answer
from django_summernote.widgets import SummernoteWidget


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question','q_photo', 'hashtags']
        widgets = {
            'question': SummernoteWidget(),
        }
		

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'a_photo']
        widgets = {
            'text': forms.TextInput(attrs={'placeholder':'댓글을 입력하세요'})
        }

        
