from django.conf.urls import url
from process import views


urlpatterns = [
    # 人员-添加
#    url(r'^person_add', views.Processor_Add),
    # 人员-查询
    url(r'^processor_inquiry/$', views.Processor_Inquiry),
    # 人员-更改
    url(r'^processor_update/$',views.Processor_Update),
    # 人员-删除
#    url(r'^processor_delete/$',views.Processor_Delete),

    # 结果-提交
    url(r'^processtion_add',views.ProcessData_Add),
    # 结果-查询
    url(r'^processtion_inquiry/$',views.ProcessData_Inquiry),  #一对多

]
