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

'''
    url(r'^trans_submit',views.list),
    url(r'^trans_inquiry',views.list),
    url(r'^sell_submit',views.list),
    url(r'^sell_inquiry',views.list),
    
    
    #信息核对
    url(r'^Transport/ProductInfoVerify/$', views.product_inquiry),
    # 运输数据填写
    #url(r'^Transport/dataShow/$', views.trans_info_show),
    url(r'^Transport/dataWrite2', views.data_write2),
    url(r'^Transport/dataWrite', views.data_write),
    
    # 多级url
    # 指向Total的urls文件
    url(r'^Total/',include('Total.urls')),
    # 指向TestSell的urls文件
    url(r'^TestSell/',include('TestSell.urls')),
    # 指向Sell的urls文件
    url(r'^Sell/',include('Sell.urls')),
    # 指向Sell2的urls文件
    url(r'^Sell2/',include('Sell2.urls')),
    url(r'^process/', include('process.urls'))
    # 未指定路径，匹配TestSell的url
    # url(r'^',include('TestSell.urls')),
'''

'''
    
urlpatterns = [
    url(r'^register',views.register),
    url(r'^login',views.login),
    url(r'^fulfil',views.fulfil),
    url(r'^producer_alter_personal',views.producer_alter_personal),
    url(r'^producer_alter_farm',views.producer_alter_farm),
    url(r'^sheep_state',views.sheep_state),
    url(r'^fully_grown',views.fully_grown),
    url(r'^fulfil_img',views.fulfil_img),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''