from django.urls import path
from . import views
urlpatterns = [
    path('',views.blogs,name='blogs'),
    path('blog_detail/<int:id>',views.blog_detalis,name='blog_details'),
    path('my_blogs/',views.user_blogs,name="my_blogs"),
    path('category/<slug:category_slug>/', views.blogs, name='blogs_by_category'),
    path('create_blog/',views.create_blog,name='create_blog'),
    path('my_blogs/edit_blog/<int:id>',views.edit_blog,name='edit_blog'),
    path('my_blogs/delete_blog/<int:id>',views.delete_blog,name='delete_blog'),
    path('my_blogs/category/<slug:category_slug>/', views.user_blogs, name='my_blogs_by_category'),
    
]   