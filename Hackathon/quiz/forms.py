from django import forms
from .models import Question
class Questions(forms.ModelForm):
    class Meta:
        model=Question
        fields=['Question_text']