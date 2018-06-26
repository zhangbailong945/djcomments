from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from .models import Comments
from .forms import CommentsForm
from django.views.generic import DetailView

# Create your views here.
def post_comments(request,post_pk):
    post=get_object_or_404(Post,pk=post_pk)
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
            comments_list=post.comments_set.all()
            context={
                'post':post,
                'form':form,
                'comments_list':comments_list
            }
            return render(request,'blog/detail.html',context=context)
    return redirect(post)


def reply_comments(request,comment_pk):
    comment=get_object_or_404(Comments,pk=comment_pk)
    context={
        'comment':comment,
    }
    return render(request,'blog/reply.html',context=context) 
        
    
    
        
