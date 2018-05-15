from django.shortcuts import render,get_object_or_404
from .models import Post
from comments.forms import CommentsForm
# Create your views here.

def index(request):
    post_list=Post.objects.all().order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

def detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    form=CommentsForm()
    comments_list=post.comments_set.all()
    return render(request,'blog/detail.html',context={'post':post,'form':form,'comments_list':comments_list})

def login(request):
    return render(request,'accounts/')

