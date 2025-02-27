from django.shortcuts import render, redirect
from blog.models import Post
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def frontpage(request):
  posts = Post.objects.all()
  return render(request, 'core/frontpage.html', {'posts': posts})

def about(request):
  return render(request, 'core/about.html')

def register(request):
  if request.method == "POST":
      form = UserCreationForm(request.POST)
      if form.is_valid():
          
          user = form.save()
          
          messages.success(request, "Registration successful!")
          return redirect('login')  
      else:
          messages.error(request, "Error in form. Please try again.")
  else:
      form = UserCreationForm()
  return render(request, 'core/register.html', {'form': form})