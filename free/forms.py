from django import forms
from free.models import Free, p_comment
from django_summernote.widgets import SummernoteWidget

class FreeForm(forms.ModelForm):
    class Meta:
        model = Free 
        fields = ['p_title', 'p_body', 'p_photo', 'hashtags'] 
        widgets = {
            'p_body': SummernoteWidget(),
        }


class p_commentForm(forms.ModelForm):
    class Meta:
        model = p_comment
        fields = ['text']