from django.db import models
from django.urls import reverse
from accounts.models import *
# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    img=models.ImageField(upload_to=f'images/blog/')
    description=models.TextField(unique=True)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True) 

    def get_url(self):
        return reverse('blog_details', kwargs={"id":self.id})