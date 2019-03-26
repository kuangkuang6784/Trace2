# Total的二级目录设置

# from django.urls import path
from django.conf.urls import url
from Total import views

urlpatterns = [
    # submit其实就是将数据提交到管理子系统，涉及到数据库的添加,submit提交的是post请求
    url(r'^product/submit', views.product_submit),
    # inquiry提交的是get请求
    url(r'^product/inquiry/$', views.product_inquiry),  # 这里的$是一个通配符
    # path('admin/', admin.site.urls),
    # 销售人员相关
    # 增加销售人员信息
    url(r'^add_seller', views.add_seller),

]