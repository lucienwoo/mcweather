#coding=utf-8

def encode(str):
    return str.encode("utf-8")

class Weather:
    def __init__(self):
        self.city=''    #城市名
        self.city_id=''    #城市ID
        self.temp=''    #温度
        self.wd=''    #风向
        self.ws=''    #风速
        self.sd=''    #湿度
        self.time=''    #发布时间

    def __str__(self):
        return "city:"+encode(self.city)+" city_id:"+encode(self.city_id)+" temp:"+encode(self.temp)+" wd:"+encode(self.wd)+" ws:"+encode(self.ws)+" sd:"+encode(self.sd)+" time:"+self.time
