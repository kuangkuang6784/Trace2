from __future__ import unicode_literals
from django.shortcuts import HttpResponse, render, redirect
from Total import models
from django.shortcuts import render_to_response
from django.template import Context
#from django.utils import simplejson
import json

# Create your views here.

'''这里面的暂时用不上
class Account:
    def __init__(self,sheep_id,weight,gender,trans_status,trans_location,delivery,sell_location,price,part):
        self.sheep_id=sheep_id
        self.weight=weight
        self.gender=gender
        self.trans_status=trans_status
        self.trans_location=trans_location
        self.delivery=delivery
        self.sell_location=sell_location
        self.price=price
        self.part=part

class Account_product:
    def __init__(self,sheep_id,weight,gender):
        self.sheep_id = sheep_id
        self.weight = weight
        self.gender = gender

class Account_trans:
    def __init__(self,sheep_id,trans_status,trans_location,delivery):
        self.sheep_id = sheep_id
        self.trans_status = trans_status
        self.trans_location = trans_location
        self.delivery = delivery

class Account_sell:
    def __init__(self,sheep_id,sell_location,price,part):
        self.sheep_id = sheep_id
        self.sell_location = sell_location
        self.price = price
        self.part = part


def object2dict(obj):
    # convert object to a dict
    d = {}
    d['__class__'] = obj.__class__.__name__
    d['__module__'] = obj.__module__
    d.update(obj.__dict__)
    return d


def dict2object(d):
    # convert dict to object
    if '__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        class_ = getattr(module, class_name)
        args = dict((key.encode('ascii'), value) for key, value in d.items())  # get args
        inst = class_(**args)  # create new instance
    else:
        inst = d
    return inst

# 此函数是让json直接转成python对象
def handle(d):
    return Account(d["sheep_id"],d["weight"],d["gender"],d["trans_status"],d["trans_location"],
                   d["delivery"],d["sell_location"],d["price"],d["part"])

def handle_product(d):
    return Account_product(d["ID_Product"], d["weight"],d["gender"])
def handle_trans(d):
    return Account_trans(d["ID_Transport"],d["status"],d["location"],d["delivery"])
def handle_sell(d):
    return Account_sell(d["ID_Sell"],d["location"],d["price"],d["part"])
'''

def product_submit(request):
    if request.method=="POST":
        models.Product(**json.loads(request.body)).save()
        #ID_Product=json.loads(request.body.decode())["ID_Product"]不转化成model直接用字典形式访问,我们可以处理传过来的数据
        #weight=json.loads(request.body.decode())["ID_Product"]不转化成model直接用字典形式访问,我们可以处理传过来的数据
        #gender=json.loads(request.body.decode())["ID_Product"]不转化成model直接用字典形式访问,我们可以处理传过来的数据
        #models.Product.objects.create(ID_Product=ID_Product,weight=weight,gender=gender)这时候用save
        #print(ID,weight,gender)
        print("羊生产数据上传数据库成功!")
    return HttpResponse("羊生产数据上传数据库成功!")

def product_inquiry(request):
    if request.method=="GET":#这里用get比post方便，因为羊id直接就在URL里了
        #obj_1 = models.Product.objects.all()获取表里所有的表项
        #obj_2 = models.Product.objects.filter(ID_Product='001')#用filter和下面get的区别是filter传回的是Queryset类型
        sheep_id=request.GET.get("sheep_id")#这个sheep_id是要到数据库里去查询的，查询到之后用下面的return返回一个json
        temp=models.Product.objects.get(ID_Product=sheep_id)#temp是class Product对象
        print(temp.ID_Product,temp.weight,temp.gender)
    return HttpResponse(temp.toJSON(), content_type="application/json")

def add_seller(request):
    if request.method=="POST":
        models.SellerRegistry(**json.loads(request.body)).save()
        print("销售人员信息已上传数据库")
    return HttpResponse("销售人员信息已上传数据库")

def inquiry_seller(request):
    if request.method=="GET":
        seller_id=request.GET.get("SellerID")
        temp=models.SellerRegistry.objects.get(SellerID=seller_id)
    return HttpResponse(temp.toJSON(), content_type="application/json")