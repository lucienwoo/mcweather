#coding=utf-8
from mcutil import *
import dealjson,sys

def by_name(name):
    g=GetCityId()
    ci=g.get_id_by_name(name)
    if ci<0:
        return
    by_id(ci)

def by_id(ci):
    dealjson.init_apihander(ci)

if sys.argv[2]=="1":
    by_name(sys.argv[1])
else:
    by_id(sys.argv[1])

