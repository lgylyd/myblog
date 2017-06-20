#coding=utf-8
from django.contrib import admin

# Register your models here.
from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category','author']
    search_fields = ('title',)  # 列表包含根据指定字段搜索
    list_filter = ('created_time',)  # 右侧过滤选项

# 把新增的 PostAdmin 也注册进来
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)