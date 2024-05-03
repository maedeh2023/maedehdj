from django import forms
from django.contrib.auth.models import User

from accounts.models import Profile


class UserRegisterForm(forms.Form):
    user_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'please enter your username'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'please enter your email'}))
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    password_1=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'please enter your password'}))
    password_2=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'please renter your password'}))


    def clean_user_name(self):
        user=self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('user exists')
        return user
    def clean_email(self):
        email= self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('email exists')
        return email
    def clean_password_2(self):
        password1=self.cleaned_data['password_1']
        password2 = self.cleaned_data['password_2']
        if password1 !=password2:
            raise forms.ValidationError('password not match ')
        elif len(password2)<8:
            raise forms.ValidationError('password is too short')
        elif not any (x.isupper() for x in password2):
            raise forms.ValidationError('password should has at least one uppercase charachtor')
        return password1

class UserLoginForm(forms.Form):
    user=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['email','first_name','last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['phone','address']