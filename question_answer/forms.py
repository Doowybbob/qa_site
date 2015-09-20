from django.forms import ModelForm, CharField
from .models import Question
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit

class QuestionForm(ModelForm):

    class Meta:
        model = Question
        fields = ['question_name', 'question_text', 'tags']
   #     widgets = {'tags': CharField}

class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CreateUserForm,self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
                'username',
                'password1',
                'password2',
                Submit('register', 'Register', css_class='btn-default'),
            )

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm,self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
                'username',
                'password',
                Submit('login', 'Login', css_class='btn-default'),
            )

