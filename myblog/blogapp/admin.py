from django.contrib import admin
from django.http import HttpResponse
# Register your models here.
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
	list_display=["author", "title", "updated", "created", "publish"]
	list_editable=["title", "publish"]
	list_display_links=["author","updated"]
	search_fields=["title", "content"]
	list_filter=["author", "updated"]
	ordering=["-updated"]
	list_per_page=3
admin.site.register(BlogPost, BlogPostAdmin)
