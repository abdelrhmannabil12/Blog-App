from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='blogs'),
    path('blog_detail/<int:id>',views.blog_detalis,name='blog_details'),
    path('my_blogs/',views.user_blogs,name="my_blogs")
]   