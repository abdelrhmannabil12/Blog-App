from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='blogs'),
    path('blog_detail/<int:id>',views.blog_detalis,name='blog_details'),
    path('my_blogs/',views.user_blogs,name="my_blogs"),
    path('category/<slug:category_slug>/', views.index, name='blogs_by_category'),
    path('create_blog/',views.create_blog,name='create_blog'),

    
]   