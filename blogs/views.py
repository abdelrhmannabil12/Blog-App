from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import *
from accounts.models import *
# Create your views here.
def index(request, category_slug=None):
    categories = None
    blogs = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        blogs = Blog.objects.filter(category=categories)
        paginator = Paginator(blogs, 3)
        page = request.GET.get('page')
        paged_blogs = paginator.get_page(page)
        blog_count = blogs.count()
    else:
        blogs = Blog.objects.all().order_by('id')
        paginator = Paginator(blogs, 3)
        page = request.GET.get('page')
        paged_blogs = paginator.get_page(page)
        blog_count = blogs.count()
    all_categories=Category.objects.all()
    context = {
        'blogs': paged_blogs,
        'blog_count': blog_count,
        'categories':all_categories,
    }
    return render(request,'index.html', context)

def blog_detalis(request,id):
    blog=Blog.objects.get(id=id)
    return render(request,"post_details.html",{'blog':blog})

def user_blogs(request):
    user=Account.objects.get(id=request.user.id)
    user_blogs=Blog.objects.filter(user=request.user)
    return render(request,"my_blogs.html",{'user':user,"blogs":user_blogs})



    

