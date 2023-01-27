from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import *
from accounts.models import *
import datetime
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.
def index(request, category_slug=None):
    categories = None
    blogs = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        blogs = Blog.objects.filter(category=categories)
        paginator = Paginator(blogs, 10)
        page = request.GET.get('page')
        paged_blogs = paginator.get_page(page)
        blog_count = blogs.count()
    else:
        blogs = Blog.objects.all().order_by('id')
        paginator = Paginator(blogs, 10)
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

@login_required(login_url='login')
def create_blog(request):
    if request.method == 'POST':
        print("DONE DONEDONEDONEDONEDONE")
        blog_form=BlogForm(request.POST,request.FILES)
        if blog_form.is_valid():
            title=blog_form.cleaned_data['title']
            description=blog_form.cleaned_data['description']
            category=blog_form.cleaned_data['category']
            img=blog_form.cleaned_data['img']
            blog=Blog.objects.create(user=request.user,title=title,description=description,category=category,img=img)
            blog.save()
            return redirect('my_blogs')
    else:
        blog_form=BlogForm()
    categories=Category.objects.all()
    return render(request,"create_blog.html",{'categories':categories,'form':blog_form})
    

def edit_blog(request,id):
    blog=get_object_or_404(Blog,id=id)
    if request.method == 'POST':
        blog_form=BlogForm(request.POST,request.FILES,instance=blog)
        if blog_form.is_valid():
            blog_form.save()
            return redirect('my_blogs')
    else:
        blog_form=BlogForm()
    categories=Category.objects.all()
    return render(request,'edit_blog.html',{'blog':blog,'categories':categories,'form':blog_form})


def delete_blog(request,id):
    blog=Blog.objects.get(id=id)
    blog.delete()
    return redirect('my_blogs')