from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from datetime import date
import datetime
import json
from django.shortcuts import HttpResponse
# Create your models here.

#消费者注册表
class ConsumerRegistry(models.Model):
    ConsumerId=models.CharField(max_length=15)#消费者注册ID
    ConsumerName=models.CharField(max_length=10)#姓名
    ContactNo=models.BigIntegerField()
    RegisterTimeConsumer=models.DateField(default=date.today)
    SearchCounts=models.IntegerField(default=0)
    VIP=models.BooleanField(default=False)
    Password=models.CharField(max_length=30)
    CharacterFlag = models.IntegerField(default=1)

    def __str__(self):  # print的时候好看，类似于C++的重载<<
        return self.ConsumerId

    # model的内部写一个函数返回json
    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

#企业组织注册表
class CompanyRegistry(models.Model):
    CompanyId=models.CharField(max_length=15)
    CompanyName=models.CharField(max_length=40)
    CorporateName=models.CharField(max_length=10)#法人姓名
    CorporateIDNo=models.BigIntegerField(default=0)
    CorporateContactNo=models.BigIntegerField(default=0)
    RegisterTime=models.DateField(default=date.today)
    OperatingPlace=models.CharField(max_length=30)
    OperatingKind=models.IntegerField(default=0)
    InvestigateRes=models.IntegerField(default=0)
    BLicenseRegisterNo=models.BigIntegerField(default=0)
    BLicenseSrc=models.CharField(max_length=50)
    BLicenseDeadline=models.DateField(default=date.today)
    PLicenseNo=models.CharField(max_length=30)
    PLicenseSrc=models.CharField(max_length=40)
    PLicenseDeadline=models.DateField(default=date.today)
    AEPCertificateNo=models.BigIntegerField(default=0)
    AEPCertificateSrc=models.CharField(max_length=40)
    TaxRCNo=models.BigIntegerField(default=0)
    TaxRCSrc=models.CharField(max_length=50)
    FoodDistributionLicenseNo=models.BigIntegerField(default=0)
    FoodDistributionLicenseSrc=models.CharField(max_length=50)
    FoodHygienePermitNo=models.BigIntegerField(default=0)
    FoodHygienePermitSrc=models.CharField(max_length=50)
    OrganizationCodeCertificateNo=models.BigIntegerField(default=0)
    OrganizationCodeCertificateSrc=models.CharField(max_length=50)
    RoadTransportBusinessLicenseNo=models.BigIntegerField(default=0)

    RoadTransportBusinessLicenseSrc=models.CharField(max_length=50)

    AnimalEpidemicPCNo=models.BigIntegerField(default=0)
    AnimalEpidemicPCSrc=models.CharField(max_length=50)
    SecretKeys=models.CharField(max_length=100)#这里存json，秘钥系统分发
    Password=models.CharField(max_length=35)

    def __str__(self):  # print的时候好看，类似于C++的重载<<
        return self.CompanyId

    # model的内部写一个函数返回json
    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))


class Uni_Manager(models.Manager):
    def create(self,company,**kwargs):
        #kwargs.update(classroom_ptr_id=temp.id,c_id=temp.c_id,c_number=temp.c_number)
        # if company==-1:#表示是销售员的个人信息完善
        #     super().create(consumerregistry_ptr_id=temp.id, ConsumerId=temp.ConsumerId, ConsumerName=temp.ConsumerName,
        #                    ContactNo=temp.ContactNo, RegisterTimeConsumer=temp.RegisterTimeConsumer,
        #                    SearchCounts=temp.SearchCounts, VIP=temp.VIP, Password=temp.Password,
        #                    **kwargs)
        # else:
        #     com=CompanyRegistry.objects.filter(CompanyName=company)
        #     if com.count()==0:#公司表里没有这个公司
        #         return 0
        #     else:
        #         comid=com.first().id
        #         super().create(consumerregistry_ptr_id=temp.id,ConsumerId=temp.ConsumerId,ConsumerName=temp.ConsumerName,
        #                    ContactNo=temp.ContactNo,RegisterTimeConsumer=temp.RegisterTimeConsumer,
        #                    SearchCounts=temp.SearchCounts,VIP=temp.VIP,Password=temp.Password,companyregistry_id=comid,
        #                    **kwargs)
        com = CompanyRegistry.objects.filter(CompanyName=company)
        if com.count()==0:#公司表里没有这个公司
            return 0
        else:
            comid=com.first().id
            # super().create(ConsumerId=temp.ConsumerId,ConsumerName=temp.ConsumerName,
            #            ContactNo=temp.ContactNo,RegisterTimeConsumer=temp.RegisterTimeConsumer,
            #            SearchCounts=temp.SearchCounts,VIP=temp.VIP,Password=temp.Password,companyregistry_id=comid,
            #            **kwargs)
            super().create(companyregistry_id=comid,**kwargs,RegisterTime=date.today)
#生产者注册表
class ProducerRegistry(ConsumerRegistry):
    #ProducerId=models.CharField(max_length=10)#唯一标识生产者；2位省份，8位人员编号
    #ProducerName=models.CharField(max_length=10)
    IDNo=models.BigIntegerField(null=True)
    #ContactNo=models.BigIntegerField()
    RegisterTime=models.DateField(default=date.today)
    ProductionPlace=models.CharField(max_length=30,null=True)
    ProductionKind=models.IntegerField(default=0,null=True)
    ProductionScale=models.CharField(max_length=100,null=True)#这里存json
    InvestigateRes=models.IntegerField(default=0,null=True)
    SecretKeys=models.CharField(max_length=100,null=True)#这里存json
    #Password=models.CharField(max_length=30)
    CompanyName=models.CharField(max_length=15,null=True)
    imgID=models.ImageField(upload_to='images/',default="")
    imgwork = models.ImageField(upload_to='images/',default="")
    companyregistry=models.ForeignKey("CompanyRegistry",on_delete=models.CASCADE,related_name="producer",null=True)#一个农场有好多生产者
    #这里
    inherit=Uni_Manager()

    def __str__(self):  # print的时候好看，类似于C++的重载<<
            return self.ConsumerId

    # model的内部写一个函数返回json
    def toJSON(self):
            return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))


#运输员注册表
class TransporterRegistry(ConsumerRegistry):
    #TransporterId=models.CharField(max_length=15)
    #TransporterName=models.CharField(max_length=10)
    IDNo=models.BigIntegerField()
    #ContactNo=models.BigIntegerField()
    RegisterTime=models.DateField()
    WorkPlaceID=models.CharField(max_length=30)
    PhotoSrc=models.CharField(max_length=40)
    RoadTransportQCNo=models.BigIntegerField()
    RoadTransportQCSrc=models.CharField(max_length=40)
    TransportCounts=models.IntegerField(default=0)
    #Password=models.CharField(max_length=30)
    imgID = models.ImageField(upload_to='images/', default="")
    imgwork = models.ImageField(upload_to='images/', default="")
    imgquality = models.ImageField(upload_to='images/', default="")
    companyregistry = models.ForeignKey("CompanyRegistry", on_delete=models.CASCADE,
                                        related_name="transporter",null=True)  # 一个农场有好多生产者
    inherit = Uni_Manager()
    def __str__(self):  # print的时候好看，类似于C++的重载<<
            return self.ConsumerId

    # model的内部写一个函数返回json
    def toJSON(self):
            return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))



class ProductionData(models.Model):
    RecordID=models.CharField(max_length=30)
    MonitorId=models.BigIntegerField()
    State=models.IntegerField()
    HealthState=models.SmallIntegerField()
    GPSLocation=models.CharField(max_length=50)#json存经纬度
    ActiveDis=models.FloatField()#活动距离
    Weight=models.FloatField()
    BodyTemperature=models.FloatField()
    UCLLink=models.CharField(max_length=50)
    MonitorRecordTime=models.TimeField()#timestamp()
    def __str__(self):  # print的时候好看，类似于C++的重载<<
            return self.RecordID

            # model的内部写一个函数返回json

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))


#加工员注册表
class ProcessorRegistry(ConsumerRegistry):
    #ProcessorId = models.CharField(max_length=30)                                #加工员注册ID
    #ProcessorName = models.CharField(max_length=10)                       #姓名
    IDNo = models.BigIntegerField()                                       #身份证号
    #ContactNo = models.BigIntegerField()                                  #联系方式
    RegisterTime = models.DateField()                   #注册时间
    WorkPlaceID = models.CharField(max_length=50)                         #工作单位ID
    PhotoSrc = models.CharField(max_length=50)                            #加工人员证件照地址
    HC4foodCertificationNo = models.BigIntegerField()                     #食品从业人员健康证明编号
    HC4foodCertificationSrc = models.CharField(max_length=50)             #食品从业人员健康证明图片地址
    ProcessorCounts = models.IntegerField(default=0)                      #加工操作次数
    #Password = models.CharField(max_length=30)
    imgID = models.ImageField(upload_to='images/', default="")
    imgwork = models.ImageField(upload_to='images/', default="")
    imgquality = models.ImageField(upload_to='images/', default="")
    companyregistry = models.ForeignKey("CompanyRegistry", on_delete=models.CASCADE,
                                        related_name="processor",null=True)  # 一个农场有好多生产者
    inherit = Uni_Manager()
    def __unicode__(self):  # print的时候好看，类似于C++的重载<<
        return self.ConsumerId
    # model的内部写一个函数返回json
    #def toJSON(self):
     #   return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]),cls=DateEncoder)

class QuarantineRegistry(models.Model):
    #QuarantineID = models.CharField(max_length=10)
    #Password = models.CharField(max_length=128)
    #QuarantineName = models.CharField(max_length=16)
    IDNo = models.CharField(max_length=18)
    #ContactNo = models.BigIntegerField(null=True, blank=True)
    RegisterTime = models.CharField(max_length=30)
    WorkPlaceID = models.CharField(max_length=10)
    PhotoSrc = models.CharField(max_length=100, null=True, blank=True)
    CertificateNo = models.CharField(max_length=32, null=True, blank=True)
    CertificateSrc = models.CharField(max_length=100, null=True, blank=True)
    LicensedVeterinaryQCNo = models.CharField(max_length=32, null=True, blank=True)
    LicensedVeterinaryQCSrc = models.CharField(max_length=32, null=True, blank=True)
    QuarantineCounts = models.IntegerField(default=0)
    imgID = models.ImageField(upload_to='images/', default="")
    imgwork = models.ImageField(upload_to='images/', default="")
    imgquality1 = models.ImageField(upload_to='images/', default="")
    imgquality2 = models.ImageField(upload_to='images/', default="")
    companyregistry = models.ForeignKey("CompanyRegistry", on_delete=models.CASCADE,
                                        related_name="quarantine",null=True)  # 一个农场有好多生产者
    inherit = Uni_Manager()

    def __unicode__(self):
        return self.ConsumerId

    #def toJSON(self):
     #   return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]), cls=ComplexEncoder)


class SellerRegistry(ConsumerRegistry):
    #SellerID = models.CharField(max_length=20)  # 销售人员注册ID(唯一的标识销售人员)
    #SellName = models.CharField(max_length=10)  # 姓名
    IDNo = models.BigIntegerField()                         #身份证号
    #IDNo = models.CharField(max_length=20)  # 身份证号
    # ContactNo = models.BigIntegerField()                    #联系方式
    RegisterTime = models.DateTimeField()  # 销售人员注册时间
    WorkPlaceID = models.CharField(max_length=50)  # 工作单位ID(企业注册ID)
    PhotoSrc = models.CharField(max_length=100)  # 销售人员证件照地址
    imgID = models.ImageField(upload_to='images/', default="")
    imgwork = models.ImageField(upload_to='images/', default="")#销售员没有工作单位
    companyregistry = models.ForeignKey("CompanyRegistry", on_delete=models.CASCADE,
                                        related_name="seller", null=True)  # 一个农场有好多生产者
    inherit = Uni_Manager()

class DateEncoding(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.date):
            return o.strftime('%Y/%m/%d')

















