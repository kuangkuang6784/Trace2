"""Trace_quar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib import admin
from django.conf.urls import url
from quarantineTest import views

urlpatterns = [
    # submit其实就是将数据提交到管理子系统，涉及到数据库的添加,submit提交的是post请求
    url(r'^quarantineTest/quarantine/submit', views.quarantine_submit),
    # inquiry提交的是get请求
    url(r'^quarantineTest/quarantine/inquiry$', views.quarantine_inquiry),
    url(r'^quarantineTest/quarantiner/inquiry$', views.quarantiner_inquiry),
    url(r'^quarantineTest/quarantine/registry', views.quarantiner_registry),
    url(r'^quarantineTest/quarantiner/alter', views.quarantiner_alter),
    url(r'^quarantineTest/quarantiner/application$', views.qurarantiner_application)

]
