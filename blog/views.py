from django.shortcuts import render,get_object_or_404
from django.views.decorators.csrf import csrf_exempt  
from django.http import HttpResponse
from .models import Post
from comments.forms import CommentsForm
from collections import OrderedDict
import json
from django.utils.timesince import timesince

# Create your views here.

def index(request):
    post_list=Post.objects.all().order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

def detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    form=CommentsForm()
    comments_list=post.comments_set.all()
    comment_list=list(comments_list)
    comment_dict=tree_comments(comment_list)
    return render(request,'blog/detail.html',context={'post':post,'form':form,'comment_dict':comment_dict})

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



def tree_sub(d_dict,comment_obj):
    for k,v_dict in d_dict.items():
        k.time=timesince(k.created_time)
        if k.user.socialaccount_set.exists():
            k.user.headimg=k.user.socialaccount_set.first().get_avatar_url()
        else:
            k.user.headimg='/static/blog/images/author.svg'
        if k.id==comment_obj.parent.id:
            d_dict[k][comment_obj]=OrderedDict()
            return
        else:
            tree_sub(d_dict[k],comment_obj)


def tree_comments(comment_list):
    comment_dict=OrderedDict()
    for comment_obj in comment_list:
        comment_obj.time=timesince(comment_obj.created_time)
        if comment_obj.user.socialaccount_set.exists():
            comment_obj.user.headimg=comment_obj.user.socialaccount_set.first().get_avatar_url()
        else:
            comment_obj.user.headimg='/static/blog/images/author.svg'

        if comment_obj.parent is None:
            comment_dict[comment_obj]=OrderedDict()
        else:
            tree_sub(comment_dict,comment_obj)
    
    return comment_dict
            
    

