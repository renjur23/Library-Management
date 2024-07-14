from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser



class BookCategory(models.Model):
    book_cat = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250, unique=True, default=1)
    cat_image = models.ImageField(upload_to='category', blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.book_cat)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return '{}'.format(self.book_cat)

class Book(models.Model):
    book_cat = models.ForeignKey(BookCategory,on_delete=models.CASCADE,default=1)
    slug=models.SlugField(max_length=250,unique=True,default=1)
    book_image = models.ImageField(upload_to='books', blank=True)
    book_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    rating = models.FloatField(default=1,max_length=5)
    updated_on = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
   
    
    def __str__(self):
        return self.book_name
   
class Newuser(models.Model):
    f_name=models.CharField(max_length=255)
    l_name=models.CharField(max_length=255)
    mob=models.CharField(max_length=10)
    email=models.EmailField()
  

    def __str__(self):
        return self.f_name
    
class Login(models.Model):
     email=models.EmailField()
     pswd=models.TextField(max_length=20)
     
     def __str__(self):
        return self.email
