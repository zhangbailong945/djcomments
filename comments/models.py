from django.db import models
#from django.contrib.auth.models import User

from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models


# Create your models here.
class Comments(models.Model):

    user=models.ForeignKey(User,verbose_name='评论人',on_delete=models.CASCADE)
    content=models.TextField(verbose_name='评论内容')
    parent=models.ForeignKey('self', verbose_name='评论',null=True, blank=True, related_name='child',on_delete=models.CASCADE)
    post=models.ForeignKey('blog.Post',on_delete=models.CASCADE)
    created_time=models.DateTimeField(auto_now_add=True,verbose_name='评论时间')

    objects=models.Manager()


    def __str__(self):
        return str(self.content)
    
    def get_absolute_url(self):
        return reverse('comment:reply',kwargs={'pk':self.pk})
