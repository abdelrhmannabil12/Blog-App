from django.shortcuts import render
from .models import Blog
# Create your views here.
def index(request):
    blogs=Blog.objects.all()
    return render(request,'index.html',{'blogs':blogs})


def blog_detalis(request,id):
    blog=Blog.objects.get(id=id)
    return render(request,"post_details.html",{'blog':blog})