from __future__ import unicode_literals
from django.db import models
import json
from datetime import date
from datetime import datetime
# Create your models here.
''' python manage.py makemigrations 记录改动
    python manage.py migrate 改动到数据库
    创建或修改model
    删除数据表:
    
    migrations文件夹只保留__init__.py
    delete from django_migrations where app_ren= "account";
    delete from django_migrations where app= "account";
    重新同步
'''

# 消费者注册表

class ConsumerRegistry(models.Model):
    ConsumerId = models.CharField(max_length=15)  # 消费者注册ID
    ConsumerName = models.CharField(max_length=10)  # 姓名
    ContactNo = models.CharField(max_length=20)
    RegisterTimeConsumer = models.DateField(default=date.today())
    # RegisterTimeConsumer = models.DateTimeField()
    SearchCounts = models.IntegerField(default=0)
    VIP = models.BooleanField(default=False)
    Password = models.CharField(max_length=128)
    # CharacterFlag = models.IntegerField(default=1)

    def __str__(self):  # print的时候好看，类似于C++的重载<<
        return self.ConsumerId

    # model的内部写一个函数返回json
    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]), cls=ComplexEncoder)


class QuarantineRegistry(ConsumerRegistry):
    QuarantinePersonID = models.CharField(max_length=10)
    #Password = models.CharField(max_length=128)
    QuarantinerName = models.CharField(max_length=16)
    IDNo = models.CharField(max_length=18)
    ContactNo_Quar = models.CharField(max_length=20, null=True, blank=True)
    RegisterTime = models.CharField(max_length=30)
    WorkPlaceID = models.CharField(max_length=30)
    PhotoSrc = models.CharField(max_length=100, null=True, blank=True)
    CertificateNo = models.CharField(max_length=32, null=True, blank=True)
    CertificateSrc = models.CharField(max_length=100, null=True, blank=True)
    LicensedVeterinaryQCNo = models.CharField(max_length=32, null=True, blank=True)
    LicensedVeterinaryQCSrc = models.CharField(max_length=32, null=True, blank=True)
    QuarantineCounts = models.IntegerField(default=0)

    def __unicode__(self):
        return self.QuarantineID

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]), cls=ComplexEncoder)


class QuarantineData(models.Model):
    QuarantineID = models.CharField(max_length=10, null=True, blank=True)
    ProductionId = models.CharField(max_length=10)
    QuarantinerName = models.CharField(max_length=16, null=True, blank=True)
    QuarantinePersonID = models.CharField(max_length=10)
    QuarantineLocation = models.CharField(max_length=100)
    QuarantineRes = models.CharField(max_length=100)
    QuarantineLink = models.CharField(max_length=100, null=True, blank=True)
    QuarantineTime = models.DateField(default=date.today)
    QuarantineBatch = models.CharField(max_length=50)
    QuarantineUCLLink = models.CharField(max_length=100, null=True, blank=True)
    Applicant = models.CharField(max_length=30)

    def __unicode__(self):
        return self.QuarantineID

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]), cls=ComplexEncoder)


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


