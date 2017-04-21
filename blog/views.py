from django.shortcuts import render
from .models import Post

# Create your views here.

def main_page(request):
    return render(request, 'blog/main_page.html', {})

def about_page(request):
    return render(request, 'blog/about_page.html', {})

def scottie_page(request):
    return render(request, 'blog/scottie_page.html', {})

#def alex_page(request):
#    return render(request, 'blog/alex_page.html', {})

#def payton_page(request):
#    return render(request, 'blog/payton_page.html', {})