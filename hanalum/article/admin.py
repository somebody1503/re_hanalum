from django.contrib import admin

from .models import Article
"""from .models import Like"""
from .models import Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'pub_user', 'pub_date']
    list_filter = ['pub_user', 'pub_date', ]


admin.site.register(Article, ArticleAdmin)

"""class LikeAdmin(admin.ModelAdmin):
    list_display = ['user','num_good', 'article_type',]

admin.site.register(Like, LikeAdmin)"""


class CommentAdmin(admin.ModelAdmin):
    list_display = ['writer', 'content', 'article', 'created_at', 'updated_at', "authority"]


admin.site.register(Comment, CommentAdmin)