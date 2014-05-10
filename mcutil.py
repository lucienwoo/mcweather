#coding=utf-8

class GetCityId:
    def get_id_by_name(self,name):
        f=open("/home/lucienwoo/project/pythons/mcweather/dealdata.txt")
        t=f.read()
        name_len=len(name)
        i=t.find(name)
        if i<0:
            return i
        index1=i+name_len+1
        index2=index1+9
        v=t[index1:index2]
        return v

if __name__=="__main__":
    g=GetCityId()
    print g.get_id_by_name("非洲")
