#coding=utf-8
import mcutil
from showweather import *
import dealjson,sys

#通过名称查询天气
def by_name(name):
    ci=mcutil.get_id_by_name(name)
    if ci<0:
        return
    by_id(ci)

#通过城市ID查询天气
def by_id(ci):
    w= dealjson.init_weather(ci)
    ws=WeatherShow(w)
    ws.show()

#获得命令行参数
if sys.argv[1]=="default":
    sys.argv[1]=mcutil.get_def_city()
elif sys.argv[2]=="2":
    mcutil.set_def_city(sys.argv[1])
    print "默认城市已改为:",sys.argv[1]
    sys.exit(0)

if sys.argv[2]=="1":
    by_name(sys.argv[1])
else:
    by_id(sys.argv[1])

