from django import forms
from Social.models import  Post

class Post_form(forms.ModelForm):

    class  Meta:
        model = Post
        fields = ['image','caption']