#!/usr/bin/env python
#coding=utf-8
from receiveweather import *
from weather import *
import simplejson

#通过城市ID获得API返回的天气信息
ah=ApiHander('101190401')
result=ah.get_weather()

#将结果转换为dict类型
wt_info=simplejson.loads(str(result))
#print result_obj['weatherinfo']['city']
#print type(result_obj)
wt=wt_info['weatherinfo']

#构建weather对象
current_weather=Weather()
current_weather.city=wt['city']
current_weather.city_id=wt['cityid']
current_weather.temp=wt['temp']
current_weather.wd=wt['WD']
current_weather.ws=wt['WS']
current_weather.sd=wt['SD']
current_weather.time=wt['time']

print current_weather
