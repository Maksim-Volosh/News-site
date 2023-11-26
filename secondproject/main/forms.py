from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, User, AuthenticationForm

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = {'title', 'content', 'photo', 'is_published'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'cols': 90, 'rows': 6, 'class': 'form-content', 'placeholder': 'Content'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-publ form-check-input'}),
            'photo': forms.FileInput(attrs={'class': 'form-file', 'placeholder': 'Select a file', 'id': 'file-input'}),
            
        }
        
    def __init__(self, *args, **kwargs):
        super(AddPostForm, self).__init__(*args, **kwargs)
        self.fields['photo'].required = False
        
        
class RegisterUserForm(UserCreationForm):
    
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingUser', 'placeholder': 'Username', 'required': 'required'}))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'type': 'email', 'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'name@example.com', 'required': 'required'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control', 'id': 'floatingPassword', 'placeholder': 'Password', 'required': 'required'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control', 'id': 'floatingPassword2', 'placeholder': 'Password', 'required': 'required'}))
    
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Username', 'required': 'required'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'floatingPassword', 'placeholder': 'Password', 'required': 'required'}))

    