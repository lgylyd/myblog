#coding=utf-8
from django.contrib import admin

# Register your models here.
from .models import Post, Category, Tag
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'excerpt', 'category','tags','author','created_time','modified_time')  # 列表显示的字段
    search_fields = ('title',)  # 列表包含根据指定字段搜索
    list_filter = ('publish_date',)  # 右侧过滤选项

    # 分组表单
    fieldsets = (
        ('基本信息', {'fields': ('title', 'content', 'excerpt', 'publish_date', 'status', 'user', 'categories')}),
        ('Meta Data', {'fields': ('alias', 'keywords', 'description')}),
    )


# admin.site.register(Post)
# admin.site.register(Category)
# admin.site.register(Tag)