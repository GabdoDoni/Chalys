from django.forms import ModelForm, TextInput, PasswordInput
from django.contrib.auth.models import User

class RegForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password'
        ] 
        widgets = {
            'username' : TextInput(attrs={
                'class':"input100",
                'type':"text",
                'name':"username",
                'placeholder':"Username"
            }),
            'first_name' : TextInput(attrs={
                'class':"input100",
                'type':"text",
                'name':"first_name",
                'placeholder':"Name"
            }),
            'last_name' : TextInput(attrs={
                'class':"input100",
                'type':"text",
                'name':"last_name",
                'placeholder':"Surname"
            }),
            'password' : TextInput(attrs={
                'class':"input100",
                'type':"password",
                'name':"password",
                'placeholder':"Password"
            }),
        }