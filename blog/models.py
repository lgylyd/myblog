# coding=utf-8
from django.db import models

# Create your models here.

class Category(models.Model):
	"""
    文章分类
    """
	title = models.CharField('名称', max_length=100)  # 分类名称
	alias = models.CharField('别名', max_length=100)  # 分类别名（用于 url 优化）
	sort = models.SmallIntegerField('排序')  # 排序

	class Meta:
		verbose_name = '分类'
		verbose_name_plural = '分类'
		ordering = ['sort']

	def __unicode__(self):
		return self.title


class Tag(models.Model):
	"""
    文章标签
    """
	tagname = models.CharField('标签名', max_length=60)  # 标签名
	post_ids = models.TextField(editable=False)  # 对应的文章 id 集合的序列

	class Meta:
		verbose_name = '标签'
		verbose_name_plural = '标签'

	def __unicode__(self):
		return self.tagname


class Post(models.Model):
	"""
    博客文章
    """
	# 文章发布状态
	CONTENT_STATUS_PUBLISHED = 1
	# 文章草稿箱状态
	CONTENT_STATUS_DRAFT = 2
	# 文章状态选项
	CONTENT_STATUS_CHOICES = (
		(CONTENT_STATUS_PUBLISHED, '发布'),
		(CONTENT_STATUS_DRAFT, '草稿箱'),
	)

	title = models.CharField('标题', max_length=100)  # 标题
	content = models.TextField('文章内容')  # 内容
	excerpt = models.TextField('摘要')  # 摘要
	publish_date = models.DateTimeField('发表时间')  # 发表时间
	status = models.IntegerField('状态',
								 choices=CONTENT_STATUS_CHOICES,
								 default=CONTENT_STATUS_PUBLISHED)  # 状态：1为正式发布，2为草稿箱
	comments_count = models.IntegerField(default=0, editable=False)  # 评论总数
	view_count = models.IntegerField(default=0, editable=False)  # 浏览总数

	alias = models.CharField('别名', max_length=100, blank=True)  # 别名（用于 url 优化）
	keywords = models.CharField('关键字', max_length=500, blank=True)  # 关键字
	description = models.TextField('描述', blank=True)  # 描述

	user = models.ForeignKey("auth.User",
							 verbose_name='作者',
							 related_name="%(class)ss")  # 作者
	categories = models.ManyToManyField(Category, blank=True,
										verbose_name='分类',
										related_name="posts")  # 分类

	class Meta:
		verbose_name = '文章'
		verbose_name_plural = '文章'
		ordering = ['publish_date']

	def __unicode__(self):
		return self.title