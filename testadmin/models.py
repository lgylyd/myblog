#coding=utf-8
from django.db import models
import django.utils.timezone as timezone

class DatabaseInfo(models.Model):
    name = models.CharField('数据库名字',max_length=20)
    account = models.CharField('账号',max_length=20)
    password = models.CharField('密码',max_length=50)
    address = models.CharField('地址',max_length=50)
    create_user = models.CharField('创建人',max_length=10)
    create_time = models.DateTimeField('创建时间',default = timezone.now)
    modify_user = models.CharField('修改人',max_length=10,default="")
    modify_time = models.DateTimeField('创建时间', default=timezone.now)

class SystemInfo(models.Model):
    name = models.CharField('系统名字', max_length=20)
    address = models.URLField('地址', max_length=100)
    account = models.CharField('账号', max_length=20)
    password = models.CharField('密码', max_length=50)
    database_name = models.ManyToManyField(DatabaseInfo, blank=True,verbose_name='数据库')
    create_user = models.CharField('创建人', max_length=10)
    create_time = models.DateTimeField('创建时间', default=timezone.now)
    modify_user = models.CharField('修改人', max_length=10,default="")
    modify_time = models.DateTimeField('创建时间', default=timezone.now)
    remark = models.TextField('备注', blank=False)

class TestCase(models.Model):
    project_name = models.CharField('项目名',max_length=20,default="")
    number = models.CharField('用例编号',max_length=20)
    function_model = models.CharField('功能模块',max_length=200)
    title = models.CharField('标题',max_length=200)
    precondition = models.TextField('前置条件',)
    procedure = models.TextField('测试步骤',)
    ex_result = models.TextField('预期结果',)
    pr_result = models.TextField('实际结果',blank=False)
    test_result = models.CharField('测试结果',max_length=5,blank=False)
    grade = models.CharField('用例优先级',max_length=5)
    create_user = models.CharField('创建人', max_length=10,default="")
    create_time = models.DateTimeField('创建时间', default=timezone.now)
    modify_user = models.CharField('修改人', max_length=10, default="")
    modify_time = models.DateTimeField('创建时间', default=timezone.now)
    status = models.IntegerField('是否删除',default=1)
