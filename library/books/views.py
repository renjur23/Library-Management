from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegisterForm, LoginForm
from .models import Book,BookCategory
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy



class CustomLoginView(LoginView):
    template_name='login.html'
    authentication_form=LoginForm 
    
    def get_success_url(self):
         return  reverse_lazy('home')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            for error in form.errors:
                print(error)
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def home(request):
       cat_dict={
        'categories':Book.objects.all()
    }
       return render(request,'home.html',cat_dict)
  
def bookcategory(request):
        cat_dict={
        'categories':BookCategory.objects.all()
    }
        return render(request,'bookcat.html',cat_dict)
    
def book(request,category_slug=None):
    categories=BookCategory.objects.all()
    books = Book.objects.all()
    
    if category_slug:
        category=get_object_or_404(BookCategory,slug=category_slug)
        books=books.filter(book_cat=category)
    else:
        category=None
        
    context={
        'category':category,
        'categories':categories,
        'book':books,
    }
    
    return render(request,'books.html',context)
    
   



