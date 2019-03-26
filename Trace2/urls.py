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
#from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
#from Total import views
#from TestSell import views

'''
    url(r'^trans_submit',views.list),
    url(r'^trans_inquiry',views.list),
    url(r'^sell_submit',views.list),
    url(r'^sell_inquiry',views.list),
'''

'''
urlpatterns = [
    #submit其实就是将数据提交到管理子系统，涉及到数据库的添加,submit提交的是post请求
    url(r'^product/submit',views.product_submit),
    #inquiry提交的是get请求
    url(r'^product/inquiry/$',views.product_inquiry),#这里的$是一个通配符
    #path('admin/', admin.site.urls),
    # 销售人员相关
    # 增加销售人员信息
    url(r'^add_seller',views.add_seller),
    # 查询销售人员信息
    url(r'^inquiry_seller/$',views.inquiry_seller),
    
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
    # 未指定路径，匹配TestSell的url
    # url(r'^',include('TestSell.urls')),
]