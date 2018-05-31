from django.shortcuts import render,get_object_or_404
from django.views.decorators.csrf import csrf_exempt  
from django.http import HttpResponse
from .models import Post
from comments.forms import CommentsForm
import json

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

@csrf_exempt
def qaptacha(request):     
    if request.method=='POST':
        if(request.POST.get('qaptcha_key')):
            request.session['qaptcha_key']=False
            if(request.POST.get('action')=='qaptcha'):
                request.session['qaptcha_key']=request.POST.get('qaptcha_key')
                return_dict={'error':False}
                return HttpResponse(json.dumps(return_dict))
            else:
                return_dict={'error':True}
                return HttpResponse(json.dumps(return_dict))
        else:
            return_dict={'error':False}
            return HttpResponse(json.dumps(return_dict))
        
    else:
        return_dict={'error':False}
        return HttpResponse(json.dumps(return_dict))
            
    

