from django.shortcuts import render
from .models import Blog
from accounts.models import *
# Create your views here.
def index(request):
    blogs=Blog.objects.all()
    return render(request,'index.html',{'blogs':blogs})


def blog_detalis(request,id):
    blog=Blog.objects.get(id=id)
    return render(request,"post_details.html",{'blog':blog})

def user_blogs(request):
    user=Account.objects.get(id=request.user.id)
    user_blogs=Blog.objects.filter(user=request.user)
    return render(request,"my_blogs.html",{'user':user,"blogs":user_blogs})