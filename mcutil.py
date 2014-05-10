#coding=utf-8
import os

#获得安装的目录
def get_rel_path():
    return os.environ['MC_WEATHER_HOME']

#通过城市名称获得城市ID
def get_id_by_name(name):
    f=open(get_rel_path()+"/dealdata.txt")
    t=f.read()
    f.close()
    name_len=len(name)
    i=t.find(name)
    if i<0:
        print "发生错误:未找到该城市===>>"+name+"<<==="
        return i
    index1=i+name_len+1
    index2=index1+9
    v=t[index1:index2]
    return v

def get_def_city():
    f=open(get_rel_path()+"/defcity.txt")
    t=f.read()
    f.close()
    return t.strip()

def set_def_city(name):
    f=open(get_rel_path()+"/defcity.txt",'w')
    f.write(name)
    f.close()

