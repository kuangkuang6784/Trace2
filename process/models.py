from __future__ import unicode_literals
from django.db import models
import json
from django.db.models.base import ModelState
import decimal
import datetime
from  datetime import date

# Create your models here.

#消费者注册表
class ConsumerRegistry(models.Model):
    ConsumerId=models.CharField(max_length=15,unique=True, null=True, blank=True)      #消费者注册ID
    ConsumerName=models.CharField(max_length=10, null=True, blank=True)                #姓名
    ContactNo=models.CharField(max_length=11)                                          #联系方式
    RegisterTimeConsumer=models.DateField(default=date.today)                          #注册时间
    SearchCounts=models.IntegerField(default=0)                                        #查询次数
    VIP=models.BooleanField(default=False)                                             #是否为VIP
    Password=models.CharField(max_length=30, null=True, blank=True)                    #密码
    CharacterFlag = models.IntegerField(default=1)                                     #角色标志
    def __str__(self):  # print的时候好看，类似于C++的重载<<
        return self.ConsumerId
    # model的内部写一个函数返回json
    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]),cls=DateEncoder)

#加工员注册表
class ProcessorRegistry(ConsumerRegistry):
#    ProcessorId =models.CharField(max_length=15,null=True)
#    ProcessorId = ConsumerRegistry.ConsumerId                             #加工员注册ID
#    ProcessorId =models.ForeignKey('ConsumerRegistry',to_field='ConsumerId',on_delete=models.CASCADE)
#    ProcessorName = models.CharField(max_length=10,null=True)
#    ProcessorName = ConsumerRegistry.ConsumerName                         #姓名
    IDNo = models.CharField(max_length=18)                                #身份证号
#    ContactNo = models.BigIntegerField(null=True, blank=True)
#    ContactNo = ConsumerRegistry.ContactNo                                #联系方式
#    RegisterTime = models.DateField(default=date.today)
#    RegisterTime = ConsumerRegistry.RegisterTimeConsumer                  #注册时间
    WorkPlaceID = models.CharField(max_length=50)                          #工作单位ID
    PhotoSrc = models.CharField(max_length=100, null=True, blank=True)     #加工人员证件照地址
    HC4foodCertificationNo = models.BigIntegerField()                      #食品从业人员健康证明编号
    HC4foodCertificationSrc = models.CharField(max_length=50)              #食品从业人员健康证明图片地址
    ProcessorCounts = models.IntegerField(default=0)                       #加工操作次数
#    Password =models.CharField(max_length=30,null=True, blank=True)
#    Password = ConsumerRegistry.Password                                  #登录密码
    def __str__(self):  # print的时候好看，类似于C++的重载<<
        return self.ConsumerId
    # model的内部写一个函数返回json
    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]),cls=DateEncoder)

#加工数据表
class ProcessData(models.Model):
    ProcessID = models.CharField(max_length=22,unique=True, null=True, blank=True)   #加工编号(屠宰点编号7+生产内容ID10+屠宰点宰杀顺序)
    ProductionID = models.CharField(max_length=10)                 #生成内容ID 羊ID+00(8+2)
    ProcessPersonID = models.CharField(max_length=10)              #加工人员ID 继承与消费者ID
#    ProcessPersonID = models.ForeignKey('ProcessorRegistry',on_delete=models.CASCADE,)
    ProcessLocation = models.CharField(max_length=7)               #加工地 (企业编号7)
    ProcessTime = models.DateField(default=date.today)             #加工时间
    ProductionKind = models.IntegerField()                         #生产内容类型(分割为几个)
    ReproductionID1 = models.CharField(max_length=10)              #生产内容ID演化 羊ID
    ReproductionID2 = models.CharField(max_length=10)              #生产内容ID演化
    ReproductionID3 = models.CharField(max_length=10)              #生产内容ID演化
    ReproductionID4 = models.CharField(max_length=10)              #生产内容ID演化
    ReproductionID5 = models.CharField(max_length=10)              #生产内容ID演化
    ProcessUCLLink = models.CharField(max_length=50)               #UCL
    def __str__(self): # print的时候好看，类似于C++的重载<<
        return self.ProcessID
    # model的内部写一个函数返回json
    def toJSON(self):
       return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]),cls=DateEncoder)

#data 处理
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)
