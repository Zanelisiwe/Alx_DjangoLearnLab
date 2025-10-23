from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()  # this is used for flexibility

class Post(models.Model):
    title = models.CharField(max_length=200)        # post title (short-text)
    content = models.TextField()                    # post content (long-text)
    published_date = models.DateTimeField(auto_now_add=True)  # timestamp automatically set
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, #if the user is deleted, delete their posts
        related_name='posts'      #access to user.posts.all() 
    )  # post link to user 

    class Meta:
        ordering = ['-published_date']  # posts sorting (new to old)

    def __str__(self):
        return self.title  # readability for debugging


