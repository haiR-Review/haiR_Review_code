from django import forms
from .models import Review, r_comment 
from django_summernote.widgets import SummernoteWidget

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['r_title','r_body', 'r_location', 'r_photo', 'r_receipt', 'hashtags' ]
        widgets = {
            'r_body': SummernoteWidget(),
        }

class r_commentForm(forms.ModelForm) :
    class Meta :
        model = r_comment
        fields = ['text']