from django.contrib import admin
from blog.models import Post, Comments

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    # list_display = ['title','slug','author','body', 'publish', 'created', 'updated', 'status']
    list_display = ['title', 'slug', 'author', 'publish', 'created', 'updated', 'status']
    list_filter = ('updated','status','author',)
    search_fields = ('title','body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    prepopulated_fields = {'slug' : ('title',)}

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name','email','post','body','created','updated','activate')
    list_filter = ('activate','created','updated')
    search_fields = ('name','email','body')

admin.site.register(Post , PostAdmin)
admin.site.register(Comments , CommentsAdmin)