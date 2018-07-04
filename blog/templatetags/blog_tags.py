from django.utils.safestring import mark_safe
from django import template



register = template.Library()

@register.simple_tag
def tree_comments(c_dict):
    html='<ul class="media-list">'
    for k,v in c_dict.items():
        html+='<li class="media">'
        html+='<a class="media-left" href="#" id="c'+str(k.id)+'">'
        html+='<img class="media-object" width="50px" height="50px" src="'+str(k.user.headimg)+'" alt="'+k.user.username+'" />'
        html+='</a>'
        html+='<div class="media-body">'
        html+='<h4 class="media-heading">'
        html+=''+k.user.username+''
        html+='</h4>'
        html+='<p>'
        html+=''+k.content+''
        html+='</p>'
        html+='<p>'
        html+='<font color="#777" >'+str(k.time)+'</font>之前·<a href="#">回复</a>'
        html+=tree_sub_comments(v)
        html+='</p>'
        html+='</div>'
        html+='</li>'
        html+='<hr style="height:1px;border:none;border-top:1px dashed #0066CC;" />'
    html+='</ul>'
    return mark_safe(html)

def tree_sub_comments(sub_comment_dict):
    html='<ul class="media-list">'
    
    for k,v in sub_comment_dict.items():
        html+='<li class="media">'
        html+='<a class="media-left" href="#" id="c'+str(k.id)+'">'
        html+='<img class="media-object" width="50px" height="50px" src="'+str(k.user.headimg)+'" alt="'+k.user.username+'" />'
        html+='</a>'
        html+='<div class="media-body">'
        html+='<h4 class="media-heading">'
        html+='<font color="#777" >'+k.user.username+'</font>'
        html+='<i class="fa fa-share" aria-hidden="true"></i>'
        html+='<font color="#777" >'+k.parent.user.username+'</font>'
        html+='</h4>'
        html+='<p>'
        html+=''+k.content+''
        html+='</p>'
        html+='<p>'
        html+='<font color="#777">'+str(k.time)+'</font>之前·<a href="#">回复</a>'
        if v:
            html+=tree_sub_comments(v)
        html+='</p>'
        html+='</div>'
        html+='</li>'
           
    html+='</ul>'
    return html

