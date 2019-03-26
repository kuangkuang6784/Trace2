# Sell2的二级目录设置

# from django.urls import path
from django.conf.urls import url
from Sell2 import views


urlpatterns = [

    # 增加销售人员信息，仅测试时使用
    url(r'^add_seller/', views.add_seller),
    # 查询销售人员信息
    url(r'^inquiry_seller/$', views.inquiry_seller),
    # 修改销售人员信息
    url(r'^alter_seller/$', views.alter_seller),
    # 完善销售人员信息
    # url(r'^complete_seller/', views.complete_seller),
    # 增加超市信息，仅测试时使用
    url(r'^add_supermarket/', views.add_supermarket),
    # 查询销售人员信息
    url(r'^inquiry_supermarket/$', views.inquiry_supermarket),
    # 修改超市信息
    url(r'^alter_supermarket/$', views.alter_supermarket),
    # 完善超市信息
    # url(r'^complete_supermarket/', views.complete_supermarket),
    # 录入商品信息
    url(r'^register_commodity/',views.register_commodity),
    # 查询商品信息
    url(r'^sell_state/$', views.sell_state),
    # 按产地查询，测试
    url(r'^sell_state_bylocation/$', views.sell_state_bylocation),
    # 修改商品信息
    url(r'^alter_sell_state/', views.alter_sell_state)
]