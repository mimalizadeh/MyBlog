from django.urls import path
from blog import views

# path ("/route" , "view" , name)
urlpatterns = [
    path("", views.home_blog, name="blog-home"),
    path("archive/<str:post_id>", views.archive_blog, name="blog-archive")
]
