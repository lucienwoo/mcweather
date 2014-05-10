#!/usr/bin/env python
#coding=utf-8
from receiveweather import *
from weather import *
import simplejson

def init_weather(city_id):
  #通过城市ID获得API返回的天气信息
  ah=ApiHander(city_id)
  result=ah.get_weather()
  result_info=ah.get_weather_info()

  #将结果转换为dict类型
  wt_info=simplejson.loads(str(result))
  wt_info_city=simplejson.loads(str(result_info))
  wt=wt_info['weatherinfo']
  wt_city=wt_info_city['weatherinfo']

  #构建weather对象
  current_weather=Weather()
  current_weather.city=wt['city']
  current_weather.city_id=wt['cityid']
  current_weather.weather=wt_city['weather']
  current_weather.temp=wt['temp']
  current_weather.temp1=wt_city['temp1']
  current_weather.temp2=wt_city['temp2']
  current_weather.wd=wt['WD']
  current_weather.ws=wt['WS']
  current_weather.sd=wt['SD']
  current_weather.time=wt['time']

  return current_weather
