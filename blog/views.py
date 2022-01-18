from urllib import request
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views.generic.edit import UpdateView

from users.forms import UserUpdateForm
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
from django.db.models import Q

# @login_required
# def home(request):
#     context = {
#         'posts': Post.objects.all(),
#     }
#     return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    login_required = True
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3


class PostDetailView(DetailView):
    login_required = True
    model = Post


    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['name', 'uid', 'section', 'semster', 
            'hostel_or_Home', 'hostel_number', 'native_language',
            'languages_known', 'hoddies', 'address', 'state', 'country',
             'instagram', 'linkdin', 'gmail' , 'whatsapp']
    def form_valid(self, form):
        form.instance.user_posted = self.request.user
        return super().form_valid(form)


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(user_posted=user).order_by('-date_posted')
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Post
    fields = ['name', 'uid', 'section', 'semster', 
            'hostel_or_Home', 'hostel_number', 'native_language',
            'languages_known', 'hoddies', 'address', 'state', 'country',
             'instagram', 'linkdin', 'whatsapp']
    def form_valid(self, form):
        form.instance.user_posted = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user_posted:
            return True 
        return False

        

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user_posted:
            return True 
        return False



def about(request):
    
    context = {
        
        'title': 'About',
    }

    
    return render(request, 'blog/about.html', context)


def UserPostPage(request):
    
    request_user = request.user
    posts = Post.objects.filter(user_posted=request_user)

    context = {
        'posts': posts,
        'req_user' : request_user,
        'title': 'About',
    }
    
    return render(request, 'blog/userpost_page.html', context)


@login_required
def search(request):
    posts = Post.objects.all()
    keyword = ''
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        keyword.lower()
        if keyword:
            posts = Post.objects.order_by('date_posted').filter(Q(name__contains=keyword) | Q(uid__contains=keyword)| 
                                        Q(section__contains=keyword)|Q(hostel_or_Home__contains=keyword)
                                        | Q(native_language__contains=keyword)| Q(languages_known__contains=keyword)| Q(hoddies__contains=keyword)
                                        | Q(address__contains=keyword)| Q(state__contains=keyword)| Q(country__contains=keyword))

        else:
            pass
    context = {
        'posts' : posts,
        'keyword' : keyword
    }
    return render(request, 'blog/search.html', context)

