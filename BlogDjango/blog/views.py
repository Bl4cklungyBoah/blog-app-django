from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm
from .models import Post, Category

def post_detail(request, category_slug, slug):
    post = Post.objects.get(slug=slug, category__slug=category_slug)
    comments = post.comments.all()  
    comment_form = CommentForm(request.POST or None)

    if request.method == 'POST':
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post  
            comment.user = request.user  
            comment.save() 
            return redirect('post_detail', category_slug=category_slug, slug=slug)  

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    })

def category(request, slug):
  category = get_object_or_404(Category, slug=slug)

  return render(request, 'blog/category.html', {'category': category})

def search(request):
  query = request.GET.get('query', '')

  posts = Post.objects.filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))

  return render(request, 'blog/search.html', {'posts': posts, 'query': query})