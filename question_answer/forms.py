from django.forms import ModelForm, CharField
from .models import Question

class QuestionForm(ModelForm):

    class Meta:
        model = Question
        fields = ['question_name', 'question_text', 'tags']
   #     widgets = {'tags': CharField}
