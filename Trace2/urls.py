"""Trace2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib import admin
from django.conf.urls import url
from app import views

'''
    url(r'^trans_submit',views.list),
    url(r'^trans_inquiry',views.list),
    url(r'^sell_submit',views.list),
    url(r'^sell_inquiry',views.list),
'''

'''
urlpatterns = [
    #信息核对
    url(r'^Transport/ProductInfoVerify/$', views.product_inquiry),
    # 运输数据填写
    #url(r'^Transport/dataShow/$', views.trans_info_show),
    url(r'^Transport/dataWrite2', views.data_write2),
    url(r'^Transport/dataWrite', views.data_write),

]
'''
urlpatterns = [
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
]