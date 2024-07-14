from django import forms
from .models import Login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

Newuser=get_user_model()
print(Newuser.__dict__)

class RegisterForm(forms.ModelForm):
    first_name=forms.CharField(max_length=20,required=True)
    last_name=forms.CharField(max_length=20,required=True)
    password=forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Newuser
        fields = ['first_name','last_name','username','email','password']
    
    def save(self,commit=True):
       user=super().save(commit=False)
       user.set_password(self.cleaned_data.get('password'))
       if commit:
           user.save()
       return user

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

        
