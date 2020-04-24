from django.shortcuts import render, redirect

# Create your views here.

def home_view(request):
    print(request.headers)
    return render(request, 'user_site/home.html', {})
