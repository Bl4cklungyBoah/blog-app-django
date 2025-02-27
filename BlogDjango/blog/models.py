from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
  title = models.CharField(max_length=255)
  slug = models.SlugField()

  class Meta:
    ordering = ('title', )
    verbose_name_plural = "Categories"

  def __str__(self):
    return self.title

class Post(models.Model):
  category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  slug = models.SlugField()
  intro = models.TextField()
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('-created_at', )

  def __str__(self):
    return self.title

class Comment(models.Model):
  post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Comment by {self.user.username} on {self.post.title}"