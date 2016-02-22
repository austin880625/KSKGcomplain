from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth

def Login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    username=request.POST.get('username')
    password=request.POST.get('password')

    if username==None and password==None:
        return render(request,'login.html',{'error_message':None})
    if username=='' or password=='':
        return render(request,'login.html',{
            'error_message':"Usename or Password field can't be empty",
        })
    user = auth.authenticate(username=username,password=password)

    if user is not None and user.is_active:
        auth.login(request,user)
        return HttpResponseRedirect('/manage/')
    else:
        return render(request,'login.html',{
            'error_message':'Login Failed! Username or password is incorrect.',
        })

def Logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
