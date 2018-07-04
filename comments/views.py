from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from .models import Comments
from .forms import CommentsForm
from django.views.generic import DetailView
from collections import OrderedDict
from django.forms.models import model_to_dict


# Create your views here.
def post_comments(request,post_pk):
    post=get_object_or_404(Post,pk=post_pk)
    post.type=1111111111111
    if request.method=='POST':
        form=CommentsForm(request.POST)
        #验证码
        #print('captcha_0:'+request.POST.get('captcha_0'))
        #print('captcha_1:'+request.POST.get('captcha_1'))

        if form.is_valid():
            comments=form.save(commit=False)
            comments.post=post
            comments.save()
            return redirect(post)
        else:
            comments=post.comments_set.all()
            
            comment_list=list(comments)
            comment_dict=tree_comments(comment_list)
            context={
                'post':post,
                'form':form,
                'comment_dict':comment_dict,
                'comment_list':'sssssssssss'.join(comment_list),
            }
            return render(request,'blog/detail.html',context=context)
    return redirect(post)


def reply_comments(request,comment_pk):
    comment=get_object_or_404(Comments,pk=comment_pk)
    context={
        'comment':comment,
    }
    return render(request,'blog/reply.html',context=context) 


def tree_sub(d_dict,comment_obj):
    for k,v_dict in d_dict.items():
        if k[0]==comment_obj.parent:
            d_dict[k][comment_obj]=OrderedDict()
            return
        else:
            tree_sub(d_dict[k],comment_obj)


def tree_comments(comment_list):
    comment_dict=OrderedDict()
    for comment_obj in comment_list:
        if comment_obj.parent is None:
            comment_dict[comment_obj]=OrderedDict()
        else:
            tree_sub(comment_dict,comment_obj)
    
    return comment_dict


    
    
        
