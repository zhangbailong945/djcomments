from django.contrib import admin
from .models import Categoy,Post,Tag
# Register your models here.

admin.site.register(Post)
admin.site.register(Categoy)
admin.site.register(Tag)

