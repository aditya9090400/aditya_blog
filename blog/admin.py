from django.contrib import admin
from blog.models import Post, Comment


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'body', 'author', 'created', 'status', 'publish']
    list_filter = ('status', 'author')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'body',)
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'name', 'email', 'body', 'created', 'updated', 'active']
    search_fields = ('name', 'email', 'body')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment,CommentAdmin)
