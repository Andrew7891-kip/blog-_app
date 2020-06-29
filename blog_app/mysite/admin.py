from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display=('title','author','status','created_on')
    prepopulated_fields={'slug':('title',)}

admin.site.register(Post,PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display=('name','body','post',"active",'created_on')
    actions=['approve_comments']

    def approve_comments(self,request,queryset):
        queryset.update(active=True)

admin.site.register(Comment,CommentAdmin)

# Register your models here.
