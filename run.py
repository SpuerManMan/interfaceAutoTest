#coding=utf-8
import os
from log import *
import unittest
import readConfig as RC
from TestReport import HTMLTestReportCN
from config import configEmail

class AllTest:


    def __init__(self):
        self.logpath = MyLog.get_log()
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.logger.info('AutoTest Woking Start')
        self.test_report_path = self.logpath.get_report_path()
        self.testcase = os.path.join(RC.proDir, 'testcase')
        self.email=configEmail.MyEmail.get_email()

    def set_case_sute(self):

         test_suite=unittest.TestSuite()
         sutie_module=[]
         discover=unittest.defaultTestLoader.discover(self.testcase,pattern='test*.py',top_level_dir=None)
         sutie_module.append(discover)
         if len(sutie_module)>0:
             for suite in sutie_module:
                 for suite_name in suite:
                     test_suite.addTest(suite_name)
                     self.logger.info('运行的case为：%s'% suite_name)

         else:
             self.logger.info('没有获取到testcase！')
             return None
         return test_suite

    def run(self):
        try:
            suite=self.set_case_sute()
            if suite is not None:
                self.logger.info('------------ Test Start ------------')
                fp=open(self.test_report_path,'wb')
                runner=HTMLTestReportCN.HTMLTestRunner(stream=fp,title='普天自动化接口测试',description='Test Description',tester='Mr.Xiong')
                runner.run(suite)
            else:
                self.logger.info('没有要运行的testcase！')
        except Exception as e:
            self.logger.info(str(e))

        finally:
            self.logger.info('------------- Test End -------------')
            fp.close()
            if self.email.emflag=='on':
                self.email.send_Email()

if __name__=='__main__':
    all=AllTest()
    all.run()