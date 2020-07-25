from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import  User
from Login.models import UserProfile
from django.contrib.auth.forms import AuthenticationForm


class CreateUser(UserCreationForm):
    email = forms.EmailField(required=True,label="",widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1 = forms.CharField(required=True,label="",widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(required=True,label="",widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields =('username','email','password1','password2')

class SignIn(AuthenticationForm):
    username = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(required=True,label="",widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

class EditProfile(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type':'date',}))
    class Meta:
        model = UserProfile
        exclude = ('user',)

