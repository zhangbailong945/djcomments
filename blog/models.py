from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from comments.models import Comments

# Create your models here.
class Categoy(models.Model):
    name=models.CharField(max_length=100)

class Tag(models.Model):
    name=models.CharField(max_length=100)

class Post(models.Model):
    title=models.CharField(max_length=70)
    body=models.TextField()
    created_time=models.DateTimeField()
    modified_time=models.DateTimeField()
    categoy=models.ForeignKey(Categoy,on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tag,blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    objects=models.Manager()

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})
