from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    slug = models.SlugField()
    thumbnail = models.ImageField()


    def __str__(self):
        return self.title




class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    views = models.IntegerField(default=0)


    def update_views(self, *args, **kwargs):
        self.views = self.views + 1
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Info(models.Model):
    email = models.EmailField()
    phone = models.BigIntegerField()
    about = models.TextField(max_length=200)
    name = models.CharField(max_length=50)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.name

