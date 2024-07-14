from django.contrib import admin
from .models import Book,Newuser,Login,BookCategory


# Register your models here.
admin.site.register(Newuser)
admin.site.register(Book)
admin.site.register(Login)
admin.site.register(BookCategory)

