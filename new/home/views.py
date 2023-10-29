from django.shortcuts import render

# Create your views here.

def home(request):
    
    return render(request, 'home/index.html')


def logout(request):

    return render(request, 'account/logout.html')