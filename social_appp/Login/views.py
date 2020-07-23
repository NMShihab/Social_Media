from django.shortcuts import render,HttpResponseRedirect
from Login.forms import CreateUser, EditProfile
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse,reverse_lazy
from Login.models import UserProfile
from django.contrib.auth.decorators import login_required


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
            user_profile.save()
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
                return HttpResponseRedirect(reverse('Social:home'))

    return render(request,'Login/login.html',context={'title':'Log In','form':form})

# Edit profile
@login_required

def edit_profile(request):
    current_user = request.user
    #current_user = UserProfile.objects.get(user=request.user)
    form = EditProfile(instance=current_user)

    if request.method == 'POST':
        form = EditProfile(request.POST,request.FILES,instance=current_user)

        if form.is_valid():
            form.save(commit=True)
            form = EditProfile(instance=current_user)

    return render(request,'Login/profile.html',context={'form':form,'title':'Edit profile'})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login:login'))
