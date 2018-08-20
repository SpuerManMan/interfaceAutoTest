#coding=utf-8
import  unittest
from config import common
from log import MyLog
import paramunittest
from config import configHttp

xls=common.get_xlsx('case.xlsx','Sheet1')

@paramunittest.parametrized(*xls)
class sendPack(unittest.TestCase):

    def setParameters(self,no,path,method,params,code,result):
        self.no=no
        self.path=path
        self.method=method
        self.params=params
        self.code=code
        self.result=result

    def setUp(self):

        self.log=MyLog.get_log()
        self.logger=self.log.get_logger()
        self.conf=configHttp.configHttp()
        self.logger.info('--------------------')


    def test_Send_1(self):
        if self.method=='post':
            self.conf.set_url(self.path)
            self.logger.info('测试URL为：%s'% self.conf.get_url())
            self.logger.info('传入header参数！')
            self.conf.set_header()
            self.logger.info('传入请求参数！')
            self.conf.set_data(self.params)
            repose=self.conf.post()
            self.logger.info('请求结果为：%s'% repose.text)
            self.assertEqual(repose.text,self.result)
    def test_Send_2(self):
        self.conf.set_url(self.path)
        self.logger.info('测试URL为：%s'% self.conf.get_url())
        self.conf.set_header()
        self.logger.info('传入header参数！')
        self.conf.set_data(self.params)
        self.logger.info('传入请求参数为：%s'% self.params)
        repose=self.conf.post()
        self.logger.info('请求结果码为：%s'% repose.status_code)
        self.assertEqual(repose.status_code,self.code)



    def tearDown(self):
        self.logger.info('--------------------')
