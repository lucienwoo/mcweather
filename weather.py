#coding=utf-8

def encode(str):
    return str.encode("utf-8")

class Weather:
    def __init__(self):
        self.city=''    #城市名
        self.city_id=''    #城市ID
        self.weather=''    #天气状况
        self.temp=''    #当前温度
        self.temp1=''    #最低温度
        self.temp2=''    #最高温度
        self.wd=''    #风向
        self.ws=''    #风速
        self.sd=''    #湿度
        self.time=''    #发布时间

    def __str__(self):
        return "city:"+encode(self.city)+" city_id:"+encode(self.city_id)+" weather:"+encode(self.weather)+" temp:"+encode(self.temp)+" temp1:"+encode(self.temp1)+" temp2:"+encode(self.temp2)+" wd:"+encode(self.wd)+" ws:"+encode(self.ws)+" sd:"+encode(self.sd)+" time:"+encode(self.time)
