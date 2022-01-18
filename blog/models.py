from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    name        = models.CharField(max_length=100)
    user_posted = models.ForeignKey(User, on_delete=models.CASCADE)
    uid         = models.CharField(max_length=10, unique=True)
    section     = models.CharField(max_length=10, blank=True)
    semster     = models.IntegerField( blank=True)
    hostel_or_Home  = models.CharField(max_length=20, blank=True)
    hostel_number   = models.PositiveIntegerField(default=None, blank=True)
    native_language = models.CharField(max_length=10, default=None)
    languages_known = models.CharField(max_length=100, default=None) # add languages functionality for next update
    hoddies     = models.CharField(max_length=100, blank=True)
    address     = models.TextField(default=None, blank=True)
    state       = models.CharField(max_length=40, default=None)
    country     = models.CharField(max_length=20, default='India')

    
    instagram   = models.CharField(max_length=100, default=None, blank=True)
    gmail       = models.EmailField(max_length=100, blank=True) 
    linkdin     = models.CharField(max_length=100, default=User, blank=True)
    whatsapp    = models.CharField(max_length=100, default=User, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    # branch,  

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



