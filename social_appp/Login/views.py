from django.shortcuts import render,HttpResponseRedirect
from Login.forms import CreateUser
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse,reverse_lazy
from Login.models import UserProfile


# For User registration

def SignUp(request):
    form = CreateUser()
    registered = False
    if request.method == 'POST':
        form = CreateUser(data = request.POST)

        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user)
            return HttpResponseRedirect(reverse('Login:login'))

    return render(request,'Login/signup.html',context={'title':'Sign Up','form':form})

# for login

def Login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')


            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('Login:login'))

    return render(request,'Login/login.html',context={'title':'Log In','form':form})
