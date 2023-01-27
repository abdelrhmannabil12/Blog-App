from django.db import models
from django.urls import reverse
from accounts.models import *
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50,blank=True,null=True, unique=True)
    slug = models.SlugField(max_length=100, blank=True,null=True,unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='images/categories', blank=True)
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
            return reverse('blogs_by_category', args=[self.slug])
    

    def __str__(self):
        return self.category_name
class Blog(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    img=models.ImageField(upload_to='images/blog/')
    description=models.TextField(unique=True)
    category        = models.ForeignKey(Category,blank=True,null=True, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True) 

    def get_url(self):
        return reverse('blog_details', kwargs={"id":self.id})
    def edit_blog_url(self):
        return reverse('edit_blog', kwargs={"id":self.id})    
    
    def delete_url(self):
        return reverse('delete_blog',kwargs={"id":self.id})
