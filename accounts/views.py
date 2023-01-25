from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
import requests
from .models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user= auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"You Are Now Looged In")
            url=request.META.get('HTTP_REFERER')
            try:
                query=requests.utils.urlparse(url).query
                params=dict(x.split('=')for x in query.split('&'))
                if 'next' in params:
                    nextpage=params['next']
                    return redirect(nextpage)
              
            except:
                return redirect('blogs')
        else:
            messages.error(request,"wrong password or username , please try again")
            return redirect('login')
    return render(request,'login.html')

@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request,"You are Logged out")
    return redirect('login')

def register(request):
    if request.method == 'POST':
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            email=request.POST['email']
            password=request.POST['password']
            username=email.split('@')[0]
            user=Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            user.is_active=True
            user.save()
           # current_site=get_current_site(request)
           # mail_subject="Please Active Your account"
           # message=render_to_string('verification_email.html',{
           #     'user':user,
            #    'domain':current_site,
            #    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            #    'token':default_token_generator.make_token(user),
          #  })
           # to_email=email 
           # send_email=EmailMessage(mail_subject,message,to=[to_email])
           # send_email.send()
           # messages.success(request,'Registeration Successful , Please Verify Your Account')
            return redirect('login')
    return render(request,'register.html')