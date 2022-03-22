from django.contrib import admin
from .models import Post, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    list_editable = ('status',)
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    
    
admin.site.register(Comment)