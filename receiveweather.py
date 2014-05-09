import urllib2
_API_URL='http://www.weather.com.cn'
_RES_URI='/data/sk/'
_RES_URI_INFO='/data/cityinfo/'

class ApiHander:
    def __init__(self,city_code):
        self.city_code=city_code

    def __combine_uri(self,flag):
        if flag:
            return _RES_URI+self.city_code+'.html'
        else:
            return _RES_URI_INFO+self.city_code+'.html'

    def get_weather(self):
        return  urllib2.urlopen(_API_URL+self.__combine_uri(True)).read()

    def get_weather_info(self):
        return urllib2.urlopen(_API_URL+self.__combine_uri(False)).read()

#ah=ApiHander('101010100')
#ah.get_weather()
