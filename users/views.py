from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Please Log in now.')
            return redirect('login') 
    else:    
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    request_user = request.user
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,   instance=request.user)

        if u_form.is_valid():
            messages.success(request, 'Your Profile has been Updated')
            u_form.save()

            return redirect('profile')
    else: 
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form' : u_form,

        'posts' : Post.objects.filter(user_posted=request_user),
    }
    return render(request, 'users/profile.html', context)


@login_required
def profile_view(request):
    request_user = request.user
    posts = Post.objects.filter(user_posted=request_user)

    context = {
        'posts': posts,
        'req_user' : request_user,
        'title': 'My Profile',
    }
    return render(request, 'users/profile_view.html', context)