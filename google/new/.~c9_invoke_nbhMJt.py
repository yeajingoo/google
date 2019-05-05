from django.shortcuts import render,redirect
from .forms import PostForm

from django.contrib.auth.models import User
from django.contrib import auth





def home(request):
    return render(request, 'home.html')
    
def login(request):
    if request.method == 'POST':
	    username = request.POST['username']
		password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
            if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def create(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new:list')
    return render(request, 'new/create.html', {'form': form})
    
def list(request):
    posts = Post.objects.all()
    return render(request, 'new/list.html', {'posts': posts})
    
def show(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'new/show.html', {'post': post})