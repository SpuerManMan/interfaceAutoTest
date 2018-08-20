#coding=utf-8
import configparser,os
'''
******读取配置文件数据*******
'''
proDir=os.path.split(os.path.realpath(__file__))[0]
confPath=os.path.join(proDir,'conf.ini') #获取conf.ini路径
conf=configparser.ConfigParser()
conf.read(confPath)
class ReadConfig:

    def __init__(self):
        pass


    @staticmethod
    def get_Http(name):
        value=conf.get("HTTP",name)
        return value

    @staticmethod
    def get_Email(name):
        value=conf.get("EMAIL",name)
        return value


if __name__=="__main__":

    rcd=ReadConfig()
    value=rcd.get_Http('host')

    print(value)
