from django.shortcuts import render
from django.http import HttpResponse


def home_blog(request):
    return HttpResponse("welcome to my blog ")


def archive_blog(request, post_id):
    return HttpResponse(f"welcome to my archive --- {post_id}")
