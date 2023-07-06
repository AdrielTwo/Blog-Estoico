from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
import datetime



class User(AbstractUser):
    profile_picture = models.ImageField(null=True, blank=True, default='default.png')

    def __str__(self):
        return self.username

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    # publish_date = models.DateTimeField(default=datetime.datetime.now)
    last_updated = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()


    def get_absolute_url(self): #retorna obtener el slug para detail
        return reverse("detail", kwargs={'slug': self.slug})
    
    @property
    def comments(self):
        return self.comment_set.all()
    
    @property
    def get_comment_count(self):
        return self.comment_set.all().count()
    @property
    def get_view_count(self):
        return self.postview_set.all().count()
    
    def __str__(self):
        return self.title
    
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.user.username
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username

