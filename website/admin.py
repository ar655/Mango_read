from django.contrib import admin
from .models import *

admin.site.register(Genre)
admin.site.register(Card)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('username', 'email', 'body')

admin.site.register(Comment, CommentAdmin)