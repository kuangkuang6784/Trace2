from __future__ import unicode_literals
from django.db import models
import json
from datetime import date
from datetime import datetime

class ComplexEncoder(json.JSONEncoder):                  #时间解析函数
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

'''运输数据表'''
class TransportData(models.Model):
    TransactionID=models.CharField(max_length=50)
    BatchNum = models.IntegerField(default=0)
    ProductionID=models.CharField(max_length=50)                      #生产内容ID
    TransactionPersonID=models.CharField(max_length=50,default='')    #运输人员ID(与信息表中的id建立关联)
    From=models.CharField(max_length=50)
    To=models.CharField(max_length=50)
    Flag=models.CharField(max_length=50)                              #环节标志
    TransactionStartTime=models.DateField(default=date.today)         #流通开始时间
    TransactionEndTime=models.DateField(default=date.today)
    TransactionStartUCLLink=models.CharField(max_length=50)           #起点UCL索引
    TransactionEndUCLLink=models.CharField(max_length=50)
    def __str__(self):
        return self.TransactionID

    def info_dict(self):                                              #生成包含所有属性的字典
        dict2 = dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])
        return dict2

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]),cls=ComplexEncoder)

global produce_transport_memory                          #运输-生产批次记忆
produce_transport_memory = 0
global produce_quarantine_memory                         #运输-检疫批次记忆
produce_quarantine_memory = 0
global produce_process_memory                            #运输-加工批次记忆
produce_process_memory = 0
global sell_transport_memory                             #运输-加工批次记忆
sell_transport_memory = 0

global new_product_id_list                               #获取的最新生产内容id缓冲区，最终要写到检疫的表中
new_product_id_list =[]
global new_quarantine_id_list                            #获取的最新检疫内容id缓冲区，最终要写到加工的表中
new_quarantine_id_list =[]
global new_process_id_list                               #获取的最新加工内容id缓冲区，最终要写到销售的表中
new_process_id_list =[]



'''生产对接部分'''
'''该函数返回最新的生产批次号'''
def produce_trans_data():
    all_batch_list = []                                           #用于接受所有的批次号
    produce_batch_list = []                                       #用于接受生产者填写的批次号
    allbatchlist = TransportData.objects.all().values('BatchNum') #读入运输数据表中所有的批次号，返回的是字典列表
    for dict in allbatchlist:
        tempbatch = dict['BatchNum']                              #取出每一个批次号
        all_batch_list.append(tempbatch)                          #生成批次号列表
    print("所有的批次号" + str(all_batch_list))
    for batch in all_batch_list:
        if batch>=10000000 and batch<20000001:
            produce_batch_list.append(batch)                      #求出生产者批次号列表
    print("生产者的的批次号" + str(produce_batch_list))
    max_produce_batch = max(produce_batch_list)                   #取出最新的生产批次号
    print("最大生产批次值" + str(max_produce_batch))
    return max_produce_batch

'''该函数返回最新生产批次的id的列表，并更新生产批次记忆'''
def produce_id_get(max_product_batch):
    global produce_transport_memory
    if max_product_batch > produce_transport_memory and new_product_id_list.__len__()==0:#如果输入的批次号大于当前的生产批次记忆，且缓冲区为空（表示已经把生产数据填入检疫）
        produce_transport_memory = max_product_batch                                     #更新生产批次记忆
        print("生产者批次记忆更新为" + str(produce_transport_memory))                    #取出最新批次号对应的所有生产内容id
        tempcluster= TransportData.objects.filter(BatchNum=max_product_batch)            #从运输数据库中取出最新批次的所有记录
        for temp in tempcluster:                                                         #取出这些记录的生产内容id并形成list返回
            tempid = temp.ProductionID
            new_product_id_list.append(tempid)
        print("生成最新生产id执行完成")
    elif max_product_batch <= produce_transport_memory:
        print( str(max_product_batch) + "不是最新的生产批次号")
    elif new_product_id_list.__len__() > 0:
        print("生产数据缓冲区没有清空，请查看运输员是否在前端提交了生产运输数据")

'''该函数将上面的id列表写入到下游的检疫表中'''
def write_quarantine():
    global new_product_id_list
    for value in new_product_id_list:
        print(str(value) + "has been wrote down")
    new_product_id_list =[]
    print("检疫数据写入完毕，并清空了生产缓冲区")


'''检疫对接部分'''
'''该函数返回最新的检疫批次号'''
def quarantine_trans_data():
    all_batch_list = []                                            #用于接受所有的批次号
    quarantine_batch_list = []                                     #用于接受检疫者填写的批次号
    allbatchlist = TransportData.objects.all().values('BatchNum')  # 读入运输数据表中所有的批次号，返回的是字典列表
    for dict in allbatchlist:
        tempbatch = dict['BatchNum']                               #取出每一个批次号
        all_batch_list.append(tempbatch)                           #生成批次号列表
    print("所有的批次号" + str(all_batch_list))
    for batch in all_batch_list:
        if batch >= 30000000 and batch < 40000001:
            quarantine_batch_list.append(batch)                    # 求出生产者批次号列表
    print("检疫者的的批次号" + str(quarantine_batch_list))
    max_quarantine_batch = max(quarantine_batch_list)              # 取出最新的生产批次号
    print("最大检疫批次值" + str(max_quarantine_batch))
    return max_quarantine_batch

'''该函数返回最新检疫批次的id的列表，并更新检疫批次记忆'''
def quarantine_id_get(max_quarantine_batch):
    global produce_quarantine_memory
    if max_quarantine_batch > produce_quarantine_memory and new_quarantine_id_list.__len__() == 0:  # 如果输入的批次号大于当前的生产批次记忆，且缓冲区为空（表示已经把生产数据填入检疫）
        produce_quarantine_memory = max_quarantine_batch                                            # 更新生产批次记忆
        print("检疫者批次记忆更新为" + str(produce_quarantine_memory))                              # 取出最新批次号对应的所有生产内容id
        tempcluster = TransportData.objects.filter(BatchNum=max_quarantine_batch)                   # 从运输数据库中取出最新批次的所有记录
        for temp in tempcluster:                                                                    # 取出这些记录的生产内容id并形成list返回
            tempid = temp.ProductionID
            new_product_id_list.append(tempid)
        print("生成最新检疫id 的list执行完成")
    elif max_quarantine_batch <= produce_quarantine_memory:
        print( str(max_quarantine_batch) + "不是最新的检疫批次号")
    elif new_quarantine_id_list.__len__() > 0:
        print("检疫数据缓冲区没有清空，请查看运输员是否在前端提交了检疫运输数据")

'''该函数将上面的id列表写入到下游的加工表中'''
def write_process():
    global new_quarantine_id_list
    for value in new_quarantine_id_list:
        print(str(value) + "has been wrote down")
    new_quarantine_id_list = []
    print("加工数据写入完毕，并清空了检疫缓冲区")


'''加工对接部分'''
'''该函数返回最新的加工批次号'''
def process_trans_data():
    all_batch_list = []                                             # 用于接受所有的批次号
    process_batch_list = []                                         # 用于接受检疫者填写的批次号
    allbatchlist = TransportData.objects.all().values('BatchNum')   # 读入运输数据表中所有的批次号，返回的是字典列表
    for dict in allbatchlist:
        tempbatch = dict['BatchNum']                                # 取出每一个批次号
        all_batch_list.append(tempbatch)                            # 生成批次号列表
    print("所有的批次号" + str(all_batch_list))
    for batch in all_batch_list:
        if batch >= 20000000 and batch < 30000000:
            process_batch_list.append(batch)                        # 求出生产者批次号列表
    print("加工者的的批次号" + str(process_batch_list))
    max_process_batch = max(process_batch_list)                     # 取出最新的生产批次号
    print("最大加工批次值" + str(max_process_batch))
    return max_process_batch

'''该函数返回最新加工批次的id的列表，并更新加工批次记忆'''
def process_id_get(max_process_batch):
    global produce_process_memory
    if max_process_batch > produce_process_memory and new_process_id_list.__len__() == 0:  # 如果输入的批次号大于当前的生产批次记忆，且缓冲区为空（表示已经把生产数据填入检疫）
        produce_process_memory = max_process_batch                                         # 更新生产批次记忆
        print("加工批次记忆更新为" + str(produce_process_memory))                        # 取出最新批次号对应的所有生产内容id
        tempcluster = TransportData.objects.filter(BatchNum=max_process_batch)             # 从运输数据库中取出最新批次的所有记录
        for temp in tempcluster:                                                           # 取出这些记录的生产内容id并形成list返回
            tempid = temp.ProductionID
            new_product_id_list.append(tempid)
        print("生成最新加工id 的list执行完成")
    elif max_process_batch <= produce_process_memory:
        print( str(max_process_batch) + "不是最新的加工批次号")
    elif new_process_id_list.__len__() > 0:
        print("加工数据缓冲区没有清空，请查看运输员是否在前端提交了加工运输数据")


'''该函数将上面的id列表写入到下游的加工表中'''
def write_sell():
    global new_process_id_list
    for value in new_process_id_list:
        print(str(value) + "has been wrote down")
    new_process_id_list = []
    print("销售数据写入完毕，并清空了加工缓冲区")

