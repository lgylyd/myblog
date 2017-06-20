from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from models import Post

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request,'newblog/index.html',context={'post_list':post_list})

def detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.increase_views()
    return render(request,'newblog/detail.html',context={'post':post})




