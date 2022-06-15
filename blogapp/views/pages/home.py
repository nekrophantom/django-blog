from django.shortcuts import render
from blogapp.models.blog.blog import Blog

# Create your views here.

def homePage(request):
    title = 'Blog Django'

    blogs = Blog.objects.all()

    context = {
        'title': title,
        'blogs': blogs,
        
    }

    return render(request, 'pages/home.html', context)

