from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm

# Create your views here.
def home(request):
    blog = Blog.objects.all()
    return render(request, 'home.html', {'blog':blog})

def blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post =form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'blog.html',{'form':form})
