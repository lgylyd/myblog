#coding=utf-8
"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from users import views as users_views
from newblog import views as newblog_views
from testadmin import views as testadmin_views

urlpatterns = [
    url(r'admin/', include(admin.site.urls)),
    url(r'^myblog/register/$', users_views.register),
    url(r'^newblog/index$',newblog_views.index,name="newblog_list"),
    url(r'post/(?P<pk>[0-9]+)/$',newblog_views.detail,name='newblog_detail'),
    url(r'^testadmin/index$',testadmin_views.index,name='testadmin_index'),
    url(r'^testadmin/login$',testadmin_views.logins,name='testadmin_logins'),
    url(r'^testadmin/logout$',testadmin_views.logouts,name='testadmin_logouts'),
    url(r'^testadmin/index_v1/$',testadmin_views.index_v1,name='testadmin_index_v1'),
    url(r'^testadmin/test_case_upload$',testadmin_views.test_case_upload,name='testadmin_test_case_upload'),
    url(r'^testadmin/userInfo$',testadmin_views.userInfo,name='testadmin_userInfo'),
    url(r'^testadmin/databaseInfo$',testadmin_views.databaseInfo,name='testadmin_databaseInfo'),
    url(r'^testadmin/createDatabaseInfo$',testadmin_views.createDatabaseInfo,name='testadmin_createDatabaseInfo'),
    url(r'^testadmin/searchDatabaseInfo$',testadmin_views.searchDatabaseInfo,name='testadmin_searchDatabaseInfo'),
    url(r'^testadmin/systemInfo$',testadmin_views.systemInfo,name='testadmin_systemInfo'),
    url(r'^testadmin/createSystemInfo$',testadmin_views.createSystemInfo,name='testadmin_createSystemInfo'),
    url(r'^testadmin/searchSystemInfo$',testadmin_views.searchSystemInfo,name='testadmin_searchSystemInfo'),
    url(r'^testadmin/querySystemInfo/(\d+)$',testadmin_views.querySystemInfo,name='testadmin_querySystemInfo'),
    url(r'^testadmin/modifySystemInfo$',testadmin_views.modifySystemInfo,name='testadmin_modifySystemInfo'),
    url(r'^testadmin/testCase$',testadmin_views.testCase,name='testadmin_testCase'),
    url(r'^testadmin/createTestCase$',testadmin_views.createTestCase,name='testadmin_createTestCase'),
    url(r'^testadmin/testCaseFileDownload$',testadmin_views.testCaseFileDownload,name='testadmin_testCaseFileDownload'),
    url(r'^testadmin/searchTestCase$',testadmin_views.searchTestCase,name='testadmin_searchTestCase'),
    url(r'^testadmin/queryTestCase/(\d+)$',testadmin_views.queryTestCase,name='testadmin_queryTestCase'),
    url(r'^testadmin/modifyTestCase$',testadmin_views.modifyTestCase,name='testadmin_modifyTestCase'),
    url(r'^testadmin/deleteTestCase/(\d+)$',testadmin_views.deleteTestCase,name='testadmin_deleteTestCase'),
    url(r'^testadmin/testCaseUpload$',testadmin_views.testCaseUpload,name='testadmin_testCaseUpload'),
    #测试浏览器访问自动化脚本的可行性
    url(r'^testadmin/csErpPurchase/$',testadmin_views.csErpPurchase,name='testadmin_csErpPurchase'),



]
