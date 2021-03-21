from django.forms import ModelForm, TextInput, PasswordInput, Textarea
from django.contrib.auth.models import User
from .models import Exam

class ExamCreateForm(ModelForm):
    class Meta:
        model = Exam
        fields = [
            'title',
            'des',
            'question1',
            'question2',
            'question3',
            'answer1',
            'answer2',
            'answer3'
        ] 
        widgets = {
            'title' : TextInput(attrs={
                'class':"input100",
                'type':"text",
                'name':"title",
                'placeholder':"Title"
            }),
            'des' : Textarea(attrs={
                'class':"input100",
                'type':"text",
                'name':"des",
                'placeholder':"description"
            }),
            'question1' : TextInput(attrs={
                'class':"input100",
                'type':"text",
                'name':"question1",
                'placeholder':"question 1"
            }),
            'question2' : TextInput(attrs={
                'class':"input100",
                'type':"text",
                'name':"question2",
                'placeholder':"question 2"
            }),
            'question3' : TextInput(attrs={
                'class':"input100",
                'type':"text",
                'name':"question3",
                'placeholder':"question 3"
            }),
            'answer1' : TextInput(attrs={
                'class':"input100",
                'type':"text",
                'name':"answer1",
                'placeholder':"answer 1"
            }),
            'answer2' : TextInput(attrs={
                'class':"input100",
                'type':"text",
                'name':"answer2",
                'placeholder':"answer 2"
            }),
            'answer3' : TextInput(attrs={
                'class':"input100",
                'type':"text",
                'name':"answer3",
                'placeholder':"answer 3"
            }),
        }