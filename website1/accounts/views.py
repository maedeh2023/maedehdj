from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

def user_register(request):
    if request.method =='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            User.objects.create_user(username=data['user_name'],email=data['email'], first_name=data['first_name'],
                                     last_name=data['last_name'],password=data['password_2'])
            return redirect('home:home')
    else:
        form=UserRegisterForm()
    context={'form':form}
    return render(request,'accounts/register.html',context)

def user_login(request):
    global user
    if request.method=='POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            try:
              user=authenticate(request,username=User.objects.get(email=data['user']),password=data['password'])
            except:
                user = authenticate(request, username=data['user'], password=data['password'])

        if user is not None:
             login(request,user)
             messages.success(request,'welcome yo my site','primary')
             return redirect('home:home')
        else:
            messages.error(request, 'user or password is incorrect','danger')
    else:
        form=UserLoginForm()
    return render(request,'accounts/login.html',{'form':form})


def user_logout(request):
    logout(request)
    messages.success(request,'با موفقیت خارج شد ','warning')
    return redirect('home:home')

@login_required(login_url='accounts:login')
def user_profile(request):
    profile=Profile.objects.get(user_id=request.user.id)
    return render(request,'accounts/profile.html',{'profile':profile})


@login_required(login_url='accounts:login')
def user_update(request):
    if request.method=='POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,instance=request.user.profile)
        if user_form and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'update succesfully','success')
            return redirect('accounts:profile')
    else:

        user_form=UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdateForm(instance=request.user.profile)
    context={'user_form':user_form,'profile_form':profile_form}
    return render(request,'accounts/update.html',context)



def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,'پسورد با موفقیت تغییر کرد','success')
            return redirect('accounts:profile')
        else:
            messages.error(request,'پسورد درست انتخاب نشد','danger')
            return redirect('accounts:change')
    else:
        form=PasswordChangeForm(request.user,request.POST)

    return render(request,'accounts/change.html',{'form':form})









    return render(request,'accounts/change.html')