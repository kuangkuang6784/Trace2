from __future__ import unicode_literals
from django.shortcuts import HttpResponse, render, redirect
from app import models
from django.shortcuts import render_to_response
from django.template import Context
#from django.utils import simplejson
from django.core import serializers
import json
import datetime


# Create your views here.

'''
def register(request):
    characterflag = request.GET.get("characterFlag")
    print(characterflag)
    def producer():
        models.ProducerRegistry(**json.loads(request.body)).save()  # 可以直接存，没传进来的表项数据里默认为空
    def trans():
        models.TransporterRegistry(**json.loads(request.body)).save()  # 可以直接存，没传进来的表项数据里默认为空
    def quaratine():
        models.QuarantineRegistry(**json.loads(request.body)).save()
    def processor():
        models.ProcessorRegistry(**json.loads(request.body)).save()
    def seller():
        models.SellerRegistry(**json.loads(request.body)).save()
    def company():
        models.CompanyRegistry(**json.loads(request.body)).save()
    def consumer():
        models.ConsumerRegistry(**json.loads(request.body)).save()
    switcher={
        "0":producer(),
        "1":trans(),
        "2":quaratine(),
        "3":producer(),
        "4":seller(),
        "5":consumer(),
        "6":company()
    }
    switcher.get(characterflag,"error")()#替代switch/case,Expression is not callable
    
    return {
        "0":producer(),
        "1":trans(),
        "2":quaratine(),
        "3":producer(),
        "4":seller(),
        "5":consumer(),
        "6":company()
        }.get(characterflag, 'error')  # 'error'为默认返回值，可自设置
    
    return HttpResponse("注册成功！")
'''


def DateEncoder(obj):
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.strftime('%Y-%m-%d')

idcountper=0#反正所有人ID都是从这里来，干脆定义一个全局变量，个人用户的自增id
idcountcom=0#企业的自增id
def register(request):#少一个企业的注册
    ContactNo = json.loads(request.body.decode())["ContactNo"]  # 通过电话号码注册
    temp = models.ConsumerRegistry.objects.filter(ContactNo=ContactNo)
    if temp.exists():
        return HttpResponse("该手机号已被注册！")
    characterflag = request.GET.get("CharacterFlag")  # 表明注册的人是个人还是企业,1为个人，0为企业
    import random
    province = str(random.randint(1, 34)).zfill(2)
    if characterflag=="1":
        global idcountper
        ID = province + str(idcountper).zfill(8)
        idcountper += 1
        models.ConsumerRegistry(**json.loads(request.body),ConsumerId=ID).save()
        print(request.body)
        dict_ = {
            "ConsumerId": ID,
        }
        return HttpResponse(json.dumps(dict_, ensure_ascii=False),
                            content_type="application/json")

    else:
        global idcountcom
        ID=province+str(idcountcom).zfill(5)
        idcountcom+=1
        models.CompanyRegistry(**json.loads(request.body),CompanyId=ID).save()
        dict_ = {
            "CompanyId": ID,
        }
        return HttpResponse(json.dumps(dict_, ensure_ascii=False),
                            content_type="application/json")





def login(request):##登陆注册之后返回企业名称，经营地址，还有个人全部信息！！！！！！！！！！包括角色属性
    characterflag = request.GET.get("CharacterFlag")#表明登陆的人是个人还是企业
    if characterflag=="1":#个人
        ContactNo = json.loads(request.body.decode())["ContactNo"]#通过电话号码登录
        Password = json.loads(request.body.decode())["Password"]
        aaa=models.ConsumerRegistry.objects.filter(ContactNo=ContactNo)
        if(aaa.count()==0):
            return HttpResponse("该用户不存在！")
        else:
            temp=aaa.first()
            if Password!=temp.Password:
                return HttpResponse("密码不正确！")
            else:
                temp.__dict__.pop("_state")
                temp.__dict__.pop("Password")
                dict_ = {
                    "ConsumerId": temp.ConsumerId,
                    "CharacterFlag": temp.CharacterFlag,
                }
                temp.__dict__.update(dict_)
                return HttpResponse(json.dumps(temp.__dict__, ensure_ascii=False, default=DateEncoder),content_type="application/json")
    else:#跟上面一样的，企业
        CorporateContactNo = json.loads(request.body.decode())["CorporateContactNo"]
        Password = json.loads(request.body.decode())["Password"]
        aaa = models.ConsumerRegistry.objects.filter(CorporateContactNo=CorporateContactNo)
        if (aaa.count() == 0):
            return HttpResponse("该用户不存在！")
        else:
            temp = aaa.first()
            if Password != temp.Password:
                return HttpResponse("密码不正确！")
            else:
                temp.__dict__.pop("_state")
                temp.__dict__.pop("Password")
                dict_ = {
                    "CompanyId": temp.CompanyId,
                }
                temp.__dict__.update(dict_)
                return HttpResponse(json.dumps(temp.__dict__, ensure_ascii=False, default=DateEncoder),content_type="application/json")


def fulfil(request):#个人信息完善函数,这个函数也要返回完善过后的所有信息的！！
    #characterflag = request.POST.get("CharacterFlag")#表明要完善哪个角色
    #ConsumerId = request.POST.get("ConsumerId")
    #imgID=request.FILES.get("imgID")
    #imgwork = request.FILES.get("imgwork")
    characterflag = request.GET.get("CharacterFlag")#表明要完善哪个角色
    print(type(characterflag))
    #0为生产者；1为检疫员；2为加工员；3为运输员；4为销售员；5为普通用户
    # 这个时候这个json里是有个人的ID的,因为登陆进去之后我是传了这个人的ID给前端的
    dicttemp = json.loads(request.body.decode())
    ConsumerId = dicttemp["ConsumerId"]
    dicttemp.pop("ConsumerId")  # 把ConsumerId这个键值对删掉，删掉后的字典就是完完全全的个人信息完善的内容
    temp = models.ConsumerRegistry.objects.get(ConsumerId=ConsumerId)#在消费者表里找到该表项，该人




    # 这里可能需要把temp删掉，然后把temp的数据存在一个字典里。。。，然后下面的子类再create
    # temp.__dict__.pop("_state")
    # temp.__dict__.pop("id")
    # temp.__dict__.pop("Password")
    # 要么不定义consumerresistryid



    CompanyName=dicttemp["CompanyName"]
    dicttemp.pop("CompanyName")#后面注册的时候公司名称是要去掉的
    #注册的时候外键还得设置好啊！！！！


    dic=temp.__dict__
    temp.delete()
    dic.pop("_state")
    dic.pop("id")
    dicttemp.update(dic)
    for key,value in dicttemp.items():
        print(key,value)



    def producer():
        #CompanyName=dicttemp["CompanyName"]
        #company=models.CompanyRegistry.objects.get(CompanyName=CompanyName)
        # if models.ProducerRegistry.inherit.create(CompanyName, **dicttemp)==0:
        #     return HttpResponse("该农场不存在")
        # else:
        #     temp.CharacterFlag |= 0b100000  # 把第一位置0
        models.ProducerRegistry(**dicttemp).save()#还要判断公司呢
        temp.CharacterFlag |= 0b100000  # 把第一位置0

    def quarantine():
        if models.ProducerRegistry.inherit.create(CompanyName, **dicttemp) == 0:
            return HttpResponse("该检疫局不存在")
        else:
            temp.CharacterFlag |= 0b010000  # 把第二位置0

    def processor():
        if models.ProducerRegistry.inherit.create(CompanyName, **dicttemp) == 0:
            return HttpResponse("该加工厂不存在")
        else:
            temp.CharacterFlag |= 0b001000  # 把第三位置0

    def trans():
        if models.ProducerRegistry.inherit.create(CompanyName, **dicttemp) == 0:
            return HttpResponse("该物流公司不存在")
        else:
            temp.CharacterFlag |= 0b000100  # 把第四位置0

    def seller():
        if models.SellerRegistry.inherit.create(CompanyName, **dicttemp) == 0:
            return HttpResponse("该物流公司不存在")
        else:
            temp.CharacterFlag |= 0b000010  # 把第五位置0
    '''
    def consumer():
        models.ConsumerRegistry(**json.loads(request.body)).save()
    '''
    # switcher = {
    #     "0": producer(),
    #     "1": quarantine(),
    #     "2": processor(),
    #     "3": trans(),
    #     "4": seller(),
    # }
    # switcher.get(characterflag, "error")  # 替代switch/case,Expression is not callable
    if characterflag=="0":
        producer()
    elif characterflag=="1":
        quarantine()
    elif characterflag=="2":
        processor()
    elif characterflag=="3":
        trans()
    elif characterflag=="4":
        seller()
    dict_ = {"ConsumerId": ConsumerId}
    return HttpResponse(json.dumps(dict_, ensure_ascii=False),content_type="application/json")#返回ID

def fulfil_img(request):
    ConsumerId=request.POST.get("ConsumerId")
    characterflag = request.POST.get("CharacterFlag")  # 表明要完善哪个角色
    imgID=request.FILES.get("imgID")
    imgwork = request.FILES.get("imgwork")
    def producer():
        temp=models.ProducerRegistry.objects.get(ConsumerId=ConsumerId)
        temp.imgID=imgID
        temp.imgwork=imgwork
        temp.save()
    def quarantine():
        imgquality1 = request.FILES.get("imgquality1")
        imgquality2 = request.FILES.get("imgquality2")
        temp=models.QuarantineRegistry.objects.get(ConsumerId=ConsumerId)
        temp.imgID = imgID
        temp.imgwork = imgwork
        temp.imgquality1=imgquality1
        temp.imgquality2 = imgquality2
        temp.save()
    def processor():
        imgquality = request.FILES.get("imgquality")
        temp=models.ProcessorRegistry.objects.get(ConsumerId=ConsumerId)
        temp.imgID = imgID
        temp.imgwork = imgwork
        temp.imgquality=imgquality
        temp.save()
    def trans():
        imgquality = request.FILES.get("imgquality")
        temp=models.TransporterRegistry.objects.get(ConsumerId=ConsumerId)
        temp.imgID = imgID
        temp.imgwork = imgwork
        temp.imgquality=imgquality
        temp.save()
    def seller():
        temp=models.SellerRegistry.objects.get(ConsumerId=ConsumerId)
        temp.imgID = imgID
        temp.imgwork = imgwork
        temp.save()

    switcher = {
        "0": producer(),
        "1": quarantine(),
        "2": processor(),
        "3": trans(),
        "4": seller(),
    }
    switcher.get(characterflag, "error")  # 替代switch/case,Expression is not callable
    dict_ = {"ConsumerId": ConsumerId}
    return HttpResponse(json.dumps(dict_, ensure_ascii=False), content_type="application/json")  # 返回ID

#传给我要修改的生产者的ID
def producer_alter_personal(request):#只能改ContactNo和Password,
    dicttemp = json.loads(request.body.decode())
    ConsumerId=dicttemp["ConsumerId"]
    temp=models.ConsumerRegistry.objects.get(ConsumerId=ConsumerId)
    temp.ContactNo=dicttemp["ContactNo"]#更改电话号码
    temp.Password = dicttemp["Password"]#更改密码
    temp.save()
    #models.ConsumerRegistry.objects.filter(user='yangmv').update(pwd='520')
    dict_={"ConsumerId":ConsumerId}
    return HttpResponse(json.dumps(dict_, ensure_ascii=False),
                        content_type="application/json")#返回ID

#传给我要修改的生产者的ID
def producer_alter_farm(request):#只能改CompanyName OperatingPlace，即农场名，农场地址
    dicttemp = json.loads(request.body.decode())
    ConsumerId = dicttemp["ConsumerId"]
    CompanyName = dicttemp["CompanyName"]
    OperatingPlace = dicttemp["OperatingPlace"]
    temp_consumer = models.ConsumerRegistry.objects.get(ConsumerId=ConsumerId)
    #temp_consumer.producerregistry.companyregistry.CompanyName=dicttemp["CompanyName"]#实际上不允许这样改的，因为这是一对多，怎么可能直接改1的值，应该在company里面搜索
    #有没有要改的新的公司，如果有，外键对应上，如果没有，新创建一个，但是怎么确保这个公司不是乱填的呢？？？我的想法是：确保的时候可能需要查询一下公司表里有木有营业许可证啥的
    temp_company=models.CompanyRegistry.objects.filter(CompanyName=CompanyName)
    temp_place = models.CompanyRegistry.objects.filter(OperatingPlace=OperatingPlace)
    if temp_company.exists() and temp_place.exists() and temp_company[0].id==temp_place[0].id:#数据库里有新的企业名称和经营地址且匹配
        temp_consumer.producerregistry.companyregistry = temp_company[0].id  # 将生产者的外键指向新的农场
                    # producerregistry是父类通过子类的小写表明访问子类的数据
        #dict_ = {"ConsumerId": ConsumerId}
        #return HttpResponse(json.dumps(dict_, ensure_ascii=False),content_type="application/json")  # 返回ID
        return HttpResponse("修改成功！")

    if temp_company.exists() and temp_place.exists() and temp_company[0].id != temp_place[0].id:
        return HttpResponse("该企业名称和经营地址不匹配！")

    if temp_company.exists() and temp_place.count()==0:
        return HttpResponse("该经营地址不存在")
    if temp_place.exists() and temp_company.count()==0:
        return HttpResponse("该企业名称不存在")
    if temp_place.count()==0 and temp_company.count()==0:
        return HttpResponse("该企业名称和经营地址均不存在")


def sheep_state(request):
    temp=models.ProductionData.objects.all()
    data = serializers.serialize("json", temp)
    return HttpResponse(data, content_type="application/json")#直接不管三七二十一将queryset序列化成json给前端


def fully_grown(request):
    sheep_id=request.GET.get("Sheep_Id")
    temp=models.ProductionData.objects.filter(RecordID__contains=sheep_id).first()
    if temp.State==0:
        temp.State=2
        temp.save()
        return HttpResponse("出栏成功！")
    else:
        return HttpResponse("出栏失败！")


























