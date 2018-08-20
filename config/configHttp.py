#coding=utf-8
from readConfig import ReadConfig as rc
import gzip
import requests,os
from log import MyLog
#rc=readConfig.ReadConfig()

log=MyLog.get_log()
logger=log.get_logger()


class configHttp:

    def __init__(self):
        self.host=rc.get_Http('host')
        self.port=rc.get_Http('port')

    #设置URL
    def set_url(self,url):
        self.url='http://'+self.host+':'+self.port+url

    #获取URL
    def get_url(self):
        return self.url

    #设置header
    def set_header(self):
        self.header={
            'Content-Encoding': 'gzip',
            'Content-Type': 'x-application/x-gzip'}

    #设置请求参数
    def set_data(self,data):
        da=str.encode(data)
        dat=gzip.compress(da)
        self.data=dat

    def set_params(self,params):
        self.params=params


    def post(self):
        try:
            self.reporse=requests.post(url=self.url,headers=self.header,data=self.data)
            return self.reporse
        except Exception as e:
            logger.info(e)

    def get(self):
        try:
            self.request=requests.get(url=self.url,params=self.params,headers=self.header)
            return self.request
        except Exception as e:
            logger.info(e)


if __name__=='__main__':
    conf=configHttp()
    conf.set_url('test')
    print(conf.get_url())