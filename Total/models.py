from __future__ import unicode_literals
from django.db import models

import json
import datetime
from datetime import date
# Create your models here.

class Product(models.Model):
    ID_Product=models.CharField(max_length=99)
    weight=models.FloatField()#单位是kg，输出时注意
    gender=models.CharField(max_length=10)
    def __unicode__(self):
        return self.ID_Product
    #model的内部写一个函数返回json
    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))


class Transport(models.Model):
    ID_Transport=models.ForeignKey("Product",on_delete=models.CASCADE,)
    status=models.BooleanField()#运输完成了没
    location=models.CharField(max_length=50)#运输到哪了
    delivery=models.CharField(max_length=15)
    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))


class Sell(models.Model):
    ID_Sell=models.ForeignKey("Product", on_delete=models.CASCADE,)
    location=models.CharField(max_length=50)#在哪里卖
    price=models.IntegerField()#单位是X元/斤，输出时注意
    part=models.CharField(max_length=15)#羊的哪个部位
    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))


class SellerRegistry(models.Model):
    SellerID = models.IntegerField()                        #销售人员注册ID(唯一的标识销售人员)
    SellName = models.CharField(max_length=10)              #姓名
    IDNo = models.BigIntegerField()                         #身份证号
    ContactNo = models.BigIntegerField()                    #联系方式
    RegisterTime = models.DateTimeField()                   #销售人员注册时间
    WorkPlaceID = models.CharField(max_length=50)           #工作单位ID(企业注册ID)
    PhotoSrc = models.CharField(max_length=100)             #销售人员证件照地址
    Password = models.CharField(max_length=30)              #登陆密码(需加密保存)
    def __str__(self):  # print的时候好看，类似于C++的重载<<
        return self.SellerID

    # model的内部写一个函数返回json
    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]),cls=DateEncoder)

class SellData(models.Model):
    SellID = models.BigIntegerField()                       #销售编号(销售点编号+销售/生产内容编号+销售点顺序号)
    ProductionID = models.BigIntegerField()                 #生产内容ID/生产内容再加工ID(销售内容ID)
    SellLocation = models.CharField(max_length=50)          #销售地
    SPReceiveTime = models.DateTimeField()                  #销售点接收时间
    SPSelloutTime = models.DateTimeField(default=None)      #销售点售出时间(为空则未销售)
    Price = models.IntegerField()                           #销售价格(避免销售点恶意抬价)
    APApprovalRes = models.IntegerField(default=0)          #被溯源次数
    AccountabilityFlag = models.IntegerField(default=0)     #追责标志位
    SellUCLLink = models.CharField(max_length=100)          #销售UCL索引

    def __str__(self):  # print的时候好看，类似于C++的重载<<
        return self.SellID

    # model的内部写一个函数返回json
    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]),cls=DateEncoder)

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)
