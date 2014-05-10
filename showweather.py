#coding=utf-8
import pynotify
import mcutil

class WeatherShow:
    def __init__(self,weather):
       pynotify.init("icon-summary-body")
       self.weather=weather

    def show(self):
       n=pynotify.Notification(self.weather.city+"天气",self.__combine_info(),mcutil.get_rel_path()+"/weather_icon.png")
       n.show()


    def __combine_info(self):
        return "天气:"+self.weather.weather+"\n"+"当前温度:"+self.weather.temp+"\n"+"最低温度:"+self.weather.temp1+"    "+"最高温度:"+self.weather.temp2+"\n"+"风向:"+self.weather.wd+"\n"+"风速:"+self.weather.ws+"\n"+"湿度:"+self.weather.sd+"\n"+"发布时间:"+self.weather.time
