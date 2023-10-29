from django.shortcuts import render


def home(request):
    
    return render(request, 'home/index.html')


def logout(request):

    return render(request, 'account/logout.html')
