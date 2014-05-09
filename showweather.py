#coding=utf-8
import pynotify
pynotify.init("icon-summary-body")
n=pynotify.Notification("今日天气","温度:27c     风向:西北",
"/home/lucienwoo/project/pythons/mcweather/weather_icon.png")
n.show()

def __combine_info(weather):
    return ""
