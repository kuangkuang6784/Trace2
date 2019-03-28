from __future__ import unicode_literals
from django.shortcuts import HttpResponse, render, redirect
from app_ren import models

from django.shortcuts import render_to_response
from django.template import Context
#from django.utils import simplejson
import json
from datetime import date
from datetime import datetime
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)
def toJSON(self):
    return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]),cls=ComplexEncoder)

'''
20190325
商品信息查询，有对应商品则返回编号，
没有则返回提示信息。
'''
def product_inquiry(request):
    if request.method=="POST":
        dict_get = json.loads(request.body)  # 获得字典
        id_get=dict_get['ProductionID']
        if models.TransportData.objects.filter(ProductionID=id_get).exists():
            return HttpResponse(id_get)
        else:
            return HttpResponse("没有记录")

'''模拟上级填写运输数据表'''
def data_write(request):
    if request.method=="POST":
        dict_get = json.loads(request.body)  # 获得字典
        models.TransportData.objects.create(**dict_get)
    return HttpResponse("保存完毕")

'''
@运输数据 填写
1、首先由上游把运输数据的生产内容id和批次号填写好
2、前端送来其他运输数据（运输人员id、来源、去向、开始时间、结束时间）,根据From来确定当前的环节来决定填充把部分的表
3、生成环节标志（模糊查询）和流通编号（生产内容id 加上 环节标志）
4、填写下游运输数据、清空本层缓冲区
'''
def data_write2(request):
    if request.method=="POST":
        dict_get = json.loads(request.body)                              # 获得字典
        #id_get=dict_get['TransactionPersonID']

    maxbatch0 = models.produce_trans_data()                              #取出生产最大批次号
    maxbatch1 = models.quarantine_trans_data()                           #取出检疫最大批次号
    maxbatch2 = models.process_trans_data()                              #取出加工最大批次号

    if dict_get['From'].find("牧场") >= 0:                               #模糊查询 说明运输员在生产运输阶段
        print("开始更新前端推送的生产数据")
        models.TransportData.objects.filter(BatchNum=maxbatch0).update(  #更新前端推送内容到生产者写入的记录
            TransactionPersonID = dict_get['TransactionPersonID'],
            From = dict_get['From'],
            To=dict_get['To'],
            TransactionStartTime=dict_get['TransactionStartTime'],
            TransactionEndTime = dict_get['TransactionEndTime']
        )
        list1 = models.TransportData.objects.filter(BatchNum=maxbatch0)   #生成流通编号和环节标志字段->取出最新批次的全部记录
        for record in list1:
            models.TransportData.objects.filter(ProductionID=record.ProductionID).update(TransactionID=record.ProductionID + '03',Flag='03')
                                                                          #生成环节标志号码,并填写流通编号
        models.produce_id_get(maxbatch0)                                  #获取生产内容id列表
        models.write_quarantine()                                         #填写检疫表 清空缓冲区

    elif dict_get['From'].find("检疫") >= 0:                              #模糊查询 说明运输员在检疫运输阶段
        print("开始更新前端推送的检疫数据")
        models.TransportData.objects.filter(BatchNum=maxbatch1).update(   #更新前端推送内容到检疫者写入的记录
            TransactionPersonID = dict_get['TransactionPersonID'],
            From = dict_get['From'],
            To=dict_get['To'],
            TransactionStartTime=dict_get['TransactionStartTime'],
            TransactionEndTime = dict_get['TransactionEndTime']
        )
        list1 = models.TransportData.objects.filter(BatchNum=maxbatch1)   #取出最新检疫批次的全部记录
        for record in list1:
            models.TransportData.objects.filter(ProductionID=record.ProductionID).update(TransactionID=record.ProductionID + '13',Flag='13')
                                                                          #生成环节标志号码,并填写流通编号
        models.quarantine_id_get(maxbatch1)                               #获取最新批次检疫id列表
        models.write_process()                                            #填写加工表 清空检疫缓冲区

    elif dict_get['From'].find("加工") >= 0:                              #模糊查询 说明运输员在加工运输阶段，默认终点是某个超市，所以环节结束
        print("开始更新前端推送的加工数据")
        models.TransportData.objects.filter(BatchNum=maxbatch2).update(   #更新前端推送内容到加工者写入的记录
            TransactionPersonID = dict_get['TransactionPersonID'],
            From = dict_get['From'],
            To=dict_get['To'],
            TransactionStartTime=dict_get['TransactionStartTime'],
            TransactionEndTime = dict_get['TransactionEndTime']
        )
        list1 = models.TransportData.objects.filter(BatchNum=maxbatch2)   #取出最新加工批次的全部记录
        for record in list1:
            models.TransportData.objects.filter(ProductionID=record.ProductionID).update(TransactionID=record.ProductionID + '23',Flag='23')
                                                                          #生成环节标志号码,并填写流通编号
        models.process_id_get(maxbatch2)
        models.write_sell()                                               #填写销售表 清空加工缓冲区
    return HttpResponse("填写完毕")































'''
    #a = list1.filter(From__contains="牧场")                              #模糊查询From关键字是否含有 牧场

def trans_info_show(request):
    if request.method == "GET":
        id_get = request.GET.get("id")
        if models.TransportData.objects.filter(TransactionPersonID=id_get).exists():
            temp = models.TransportData.objects.get(TransactionPersonID=id_get)
            trans_dict = temp.info_dict()                                                   #获取运输数据字典
            return HttpResponse(json.dumps(trans_dict,cls=ComplexEncoder), content_type="application/json")
        else:
            return HttpResponse("没有记录")

def data_write(request):
    if request.method=="POST":
        dict_get = json.loads(request.body)  # 获得字典
        id_get=dict_get['TransactionPersonID']
        if models.TransportData.objects.filter(TransactionPersonID=id_get).exists():
            models.TransportData.objects.filter(TransactionPersonID=id_get).delete()
            models.TransportData(**dict_get).save()
            return HttpResponse("修改完毕")
        else:
            models.TransportData(**dict_get).save()
            return HttpResponse("第一次写入完毕")

def trans_info_show(request):
    if request.method == "GET":
        id_get = request.GET.get("id")
        if models.TransportData.objects.filter(TransactionPersonID=id_get).exists():
            temp = models.TransportData.objects.get(TransactionPersonID=id_get)
            trans_dict = temp.info_dict()                                                   #获取运输数据字典
            temp2 = models.TransporterRegistry.objects.get(ConsumerId=id_get)               #查找运输员姓名
            name = temp2.ConsumerName
            trans_dict['TransportName'] = name                                              #添加运输员姓名
            return HttpResponse(json.dumps(trans_dict,cls=ComplexEncoder), content_type="application/json")
        else:
            return HttpResponse("没有记录")
'''