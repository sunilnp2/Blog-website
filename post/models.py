from logging import makeLogRecord
from django.db import models
STATUS  = (('active', 'active'), ('inactive', 'inactive'))
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    discription = models.TextField()
    status = models.CharField(choices=STATUS, max_length=50)

    def __str__(self):
        return self.name




class Blog(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')
    writter = models.CharField(max_length=50)
    date = models.DateTimeField()
    description = models.TextField()
    slug = models.SlugField(unique=True)
    # comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    slug = models.SlugField(unique=True)
    # website = models.CharField(max_length=50)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)




