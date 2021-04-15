from django.shortcuts import render

def Index(request):
    return render(request, 'index.html')

def Signin(request):
    return render(request, 'signin.html')

def Signout(request):
    return render(request, 'signout.html')
