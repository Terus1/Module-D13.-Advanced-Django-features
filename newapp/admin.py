from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):

    def post_category(self, post):
        return ', '.join(category.name_category for category in post.category.all())

    list_display = ['author', 'title', "text_post", 'categoryType', 'post_category', 'time_in']
    list_filter = ['time_in']
    search_fields = ['title', 'text_post', 'categoryType', 'category__name_category']

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
