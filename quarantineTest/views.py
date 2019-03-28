from __future__ import unicode_literals
from django.shortcuts import HttpResponse
from quarantineTest import models
from datetime import datetime
from quarantineTest.models import ComplexEncoder

import hashlib
from django.shortcuts import render_to_response
from django.template import Context
from django.forms.models import model_to_dict
import json
# Create your views here.
from quarantineTest import quarantinedata
from quarantineTest import quarantiner
def quarantine_submit(request):
    if request.method == "POST":
        quarantinedata.submit(**json.loads(request.body))
        print("检疫数据上传数据库成功!")
    return HttpResponse("检疫数据上传数据库成功!")

def quarantine_inquiry(request):
    if request.method == "GET":
        production_id = request.GET.get("ProductionId")

        ret = quarantinedata.inquiry(production_id)
        if ret:
            return HttpResponse(ret, content_type="application/json")
        else:
            return HttpResponse("No result found")

def quarantiner_inquiry(request):
    if request.method == "GET":
        quarantiner_id = request.GET.get("QuarantinePersonID")

        includekey = ['QuarantinePersonID', 'QuarantinerName', 'IDNo', 'ContactNo_Quar', 'WorkPlaceID', \
                      'CertificateNo', 'CertificateSrc', 'LicensedVeterinaryQCNo', 'LicensedVeterinaryQCSrc', \
                      'QuarantineCounts ', 'PhotoSrc', 'Password']
        ret = quarantiner.inquiry(quarantiner_id, includekey)
        if isinstance(ret, str):
            return HttpResponse(ret)
        else:
            return HttpResponse(json.dumps(ret, cls=ComplexEncoder), content_type="application/json")

def encrypt(pwd):
    # 密码加密
    h = hashlib.sha256()
    h.update(bytes(pwd, encoding='utf-8'))
    return pwd
    #return h.hexdigest()

def qurarantiner_application(request):
    if request.method == "GET":
        producer_id = request.GET.get("ProducerId")
        includekey = ['QuarantinePersonID', 'QuarantinerName', 'IDNo', 'ContactNo_Quar', 'WorkPlaceID',\
                        'CertificateNo', 'CertificateSrc', 'LicensedVeterinaryQCNo', 'LicensedVeterinaryQCSrc',\
                        'QuarantineCounts ', 'PhotoSrc']
        ret = quarantiner.application(producer_id, includekey)
        if isinstance(ret, str):
            return HttpResponse(ret)
        else:
            return HttpResponse(json.dumps(ret, cls=ComplexEncoder), content_type="application/json")


def quarantiner_registry(request):
    if request.method == "POST":
        items = json.loads(request.body)

        quarantiner_id = items.get("QuarantinePersonID")
        password = items.get("Password")
        registertime = items.get("RegisterTime", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        items['RegisterTime'] = registertime

        items['Password'] = encrypt(password)
        res = models.QuarantineRegistry.objects.filter(QuarantinePersonID=quarantiner_id)
        if(len(res)>0):
            return HttpResponse("已存在相同ID!")
        else:
            models.QuarantineRegistry(**items).save()
            return HttpResponse("检疫员注册成功!")

def checkPwd(quarantine_id, pwd):
    pwdEncrypted = encrypt(pwd)

    pwdSaved = models.QuarantineRegistry.objects.get(QuarantinePersonID=quarantine_id).Password
    return pwdSaved == pwdEncrypted

def quarantiner_alter(request):
    if request.method == "POST":
        items = json.loads(request.body)
        quarantine_id = items.get("QuarantinePersonID")
        password = items.get("Password")

        if checkPwd(quarantine_id, password) == True:
            # 验证密码,并判断有无新密码
            if 'newpassword' in items and items['newpassword'] != None:
                items['Password'] = encrypt(items.pop('newpassword'))

            quarantiner.alter(quarantine_id, items)
            return HttpResponse("检疫员数据修改成功!")
        else:
            return HttpResponse("密码错误!")



