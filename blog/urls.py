"""testing2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required, permission_required
from .views import (PostListView, 
                    PostDetailView, 
                    UserPostListView,
                    PostCreateView,         
                    PostUpdateView,
                    PostDeleteView)
urlpatterns = [
    path('', login_required(PostListView.as_view()), name='home'),
    path('user/<str:username>', login_required(UserPostListView.as_view()), name='user-posts'),
    path('post/<int:pk>/', login_required(PostDetailView.as_view()), name='post-detail'),
    path('post/<int:pk>/update/', login_required(PostUpdateView.as_view()), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('UserPostPage/', login_required(views.UserPostPage), name='userpostpage'),
]
