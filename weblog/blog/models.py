from django.db import models
class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
     return f"{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=35)

    def __str__(self):
        return f"{self.name}"


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    title = models.CharField(max_length=30)
    slug = models.CharField(max_length=50)
    body = models.TextField(max_length=500)
    author =models.ForeignKey(User,on_delete=models.CASCADE)
    category =models.ManyToManyField(Category)
    tags =models.ManyToManyField(Tag)
    published =models.BooleanField()
    created_at = models.DateTimeField(auto_now_add= True, editable=False)
    updated_at = models.DateTimeField(auto_now_add= True, editable=False)
    #image =
    #IMAGE test



class comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    auther = models.CharField(max_length=60)
    body = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add= True, editable=False)
    
# Create your models here.



