from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel,TreeForeignKey

# Create your models here.
class Comments(MPTTModel):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    parent=TreeForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='children',db_index=True)
    post=models.ForeignKey('blog.Post',on_delete=models.CASCADE)
    created_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class MPTTMeat:
        order_insertion_by=['-created_time']