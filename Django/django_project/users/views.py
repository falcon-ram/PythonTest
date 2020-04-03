from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=True) # this saves the data to the database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created. You are now able to log in!')
            #return redirect('blog-home')
            return redirect('login')
    else:
        #form = UserCreationForm()
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# below is a decorator that adds functionality to an existing function
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

def profile_summary(request, pk):
    user = User.objects.filter(id=pk).first()
    context = {
        'user_name' : user.username,
        'user_email' : user.email,
        'user_img' : user.profile.image.url
    }
    
    return render(request, 'users/profile_summary.html', context)
