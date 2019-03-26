from django.db import models

import json
import datetime
from datetime import date
import django.utils.timezone as timezone

# Create your models here.

# 消费者注册表
class ConsumerRegistry(models.Model):
    ConsumerId = models.CharField(max_length=15,unique=True,null=True,blank=True)   # 消费者注册ID
    ConsumerName = models.CharField(max_length=10,null=True,blank=True)             # 姓名
    # ContactNo = models.IntegerField()
    ContactNo = models.CharField(max_length=11)                                     # 联系方式
    # RegisterTimeConsumer = models.DateField(default=date.today())
    RegisterTimeConsumer = models.DateTimeField(default=timezone.now)               # 消费者注册时间
    SearchCounts = models.IntegerField(default=0)                                   # 查询次数
    VIP = models.BooleanField(default=False)                                        # 会员标志位
    Password = models.CharField(max_length=30)                                      # 登陆密码
    CharacterFlag = models.IntegerField(default=1)                                  # 角色属性

    def __str__(self):  # print的时候好看，类似于C++的重载<<
        return self.ConsumerId

    # model的内部写一个函数返回json
    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]),cls=DateEncoder)

class SellerRegistry(ConsumerRegistry):
    # SellerID = models.IntegerField()                        #销售人员注册ID(唯一的标识销售人员)
    # SellerID = models.CharField(max_length=20,unique=True,null=True,blank=True)  # 销售人员注册ID(唯一的标识销售人员)
    # SellerName = models.CharField(max_length=10)  # 姓名
    # SellerName = ConsumerRegistry.ConsumerName
    # IDNo = models.BigIntegerField()                         #身份证号
    IDNo = models.CharField(max_length=18)  # 身份证号
    # ContactNo = models.BigIntegerField()                    #联系方式
    # RegisterTime = models.DateTimeField()  # 销售人员注册时间
    RegisterTime = models.DateTimeField(default=timezone.now)  # 销售人员注册时间
    WorkPlaceID = models.CharField(max_length=50)  # 工作单位ID(企业注册ID)
    PhotoSrc = models.CharField(max_length=100)  # 销售人员证件照地址

    # Password = models.CharField(max_length=30)              #登陆密码(需加密保存)

    # def __str__(self):  # print的时候好看，类似于C++的重载<<
    #    return self.SellerID

    # model的内部写一个函数返回json
    # def toJSON(self):
    #    import json
    #    return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]),cls=DateEncoder)

    def to_dict(self):
        return dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])


class SellData(models.Model):
    # SellID = models.BigIntegerField()                       #销售编号(销售点编号+销售/生产内容编号+销售点顺序号)
    SellID = models.CharField(max_length=20,unique=True,null=True,blank=True)  # 销售编号(销售点编号+销售/生产内容编号+销售点顺序号)
    # ProductionID = models.BigIntegerField()                 #生产内容ID/生产内容再加工ID(销售内容ID)
    ProductionID = models.CharField(max_length=20,null=True,blank=True)  # 生产内容ID/生产内容再加工ID(销售内容ID)
    SellLocation = models.CharField(max_length=50,null=True,blank=True)  # 销售地
    SPReceiveTime = models.DateTimeField()  # 销售点接收时间
    SPSelloutTime = models.DateTimeField(null=True,blank=True)  # 销售点售出时间(为空则未销售)
    Price = models.IntegerField()  # 销售价格(避免销售点恶意抬价)
    APApprovalRes = models.IntegerField(default=0)  # 被溯源次数
    AccountabilityFlag = models.IntegerField(default=0)  # 追责标志位
    SellUCLLink = models.CharField(max_length=100,null=True,blank=True)  # 销售UCL索引
    SellName = models.CharField(max_length=50,null=True,blank=True)      #商品名称

    def __str__(self):  # print的时候好看，类似于C++的重载<<
        return self.SellID

    # model的内部写一个函数返回json
    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]),
                          cls=DateEncoder)


class CompanyRegistry(models.Model):
    # CompanyID = models.IntegerField()                         #企业注册ID(企业唯一标识)
    CompanyID = models.CharField(max_length=20)                 # 企业注册ID(企业唯一标识)
    CompanyName = models.CharField(max_length=50)               # 企业名称
    # CorporateIDNo = models.BigIntegerField()                #企业法人身份证号
    CorporateIDNo = models.CharField(max_length=20)             # 企业法人身份证号
    CorporateContactNo = models.BigIntegerField()               # 企业法人联系方式
    RegisterTime = models.DateTimeField()                       # 企业注册时间
    OperatingPlace = models.CharField(max_length=50)            # 经营地址
    OperatingKind = models.IntegerField()                       # 经营类型
    InvestigateRes = models.BooleanField()                      # 生产地实地考察结果
    # BLicenseRegisterNo = models.BigIntegerField()           #营业执照注册号
    BLicenseRegisterNo = models.CharField(max_length=20)        # 营业执照注册号
    BLicenseSrc = models.CharField(max_length=100)              # 营业执照图片地址
    BLicenseDeadline = models.DateTimeField()                   # 营业执照经营期限
    # PLicenseNo = models.BigIntegerField()                   #生产许可证编号
    PLicenseNo = models.CharField(max_length=20)                # 生产许可证编号
    PLicenseSrc = models.CharField(max_length=100)              # 生产许可证图片地址
    PLicenseDeadline = models.DateTimeField()                   # 生产许可证生产期限
    # AEPCertificateNo = models.BigIntegerField()             #动物防疫条件合格证号(农场)
    AEPCertificateNo = models.CharField(max_length=20)          # 动物防疫条件合格证号(农场)
    AEPCertificateSrc = models.CharField(max_length=100)        # 动物防疫条件合格证图片地址(农场)
    # TaxRCNo = models.BigIntegerField()                      #税务登记证编号
    TaxRCNo = models.CharField(max_length=20)                   # 税务登记证编号
    TaxRCSrc = models.CharField(max_length=100)                 # 税务登记证图片地址
    # FoodDistributionLicenseNo = models.BigIntegerField()    #食品流通许可证编号
    FoodDistributionLicenseNo = models.CharField(max_length=20) # 食品流通许可证编号
    FoodDistributionLicenseSrc = models.CharField(max_length=100)   # 食品流通许可证图片地址
    # FoodHygienePermitNo = models.BigIntegerField()          #食品卫生许可证编号
    FoodHygienePermitNo = models.CharField(max_length=20)       # 食品卫生许可证编号
    FoodHygienePermitSrc = models.CharField(max_length=100)     # 食品卫生许可证图片地址
    # OrganizationCodeCertificateNo = models.BigIntegerField()#组织机构代码证编号
    OrganizationCodeCertificateNo = models.CharField(max_length=20) # 组织机构代码证编号
    OrganizationCodeCertificateSrc = models.CharField(max_length=100)   # 组织机构代码证图片地址
    # RoadTransportBusinessLicenseNo = models.BigIntegerField()#道路运输经营许可证编号
    RoadTransportBusinessLicenseNo = models.CharField(max_length=20)    # 道路运输经营许可证编号
    RoadTransportBusinessLicenseSrc = models.CharField(max_length=100)  # 道路运输经营许可证图片地址
    # AnimalEpidemicPCNo = models.BigIntegerField()           #动物防疫合格证编号(农场)
    AnimalEpidemicPCNo = models.CharField(max_length=20)        # 动物防疫合格证编号(农场)
    AnimalEpidemicPCSrc = models.CharField(max_length=100)      # 动物防疫合格证图片地址(农场)
    # SecretKeys = json  # 密钥对(密钥系统分发)
    SecretKeys = models.CharField(max_length=2048)
    Password = models.CharField(max_length=30)                  # 登陆密码(需加密保存)

    def __str__(self):  # print的时候好看，类似于C++的重载<<
        return self.CompanyID

    # model的内部写一个函数返回json
    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]),cls=DateEncoder)


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            print('test')

            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)
