from django.shortcuts import render,HttpResponseRedirect
from Login.forms import CreateUser
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse,reverse_lazy


def SignUp(request):
    form = CreateUser()
    registered = False
    if request.method == 'POST':
        form = CreateUser(data = request.POST)

        if form.is_valid():
            user = form.save()
            registered = True

            pass

    return render(request,'Login/signup.html',context={'title':'Sign Up','form':form})
