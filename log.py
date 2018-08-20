#coding=utf-8

import readConfig
import os
from datetime import datetime
import threading
import  logging

class log:

    def __init__(self):
        #创建日志文件
        self.logPath=os.path.join(readConfig.proDir,'log')
        if not os.path.exists(self.logPath):
            os.mkdir(self.logPath)
        self.logFilePath=os.path.join(self.logPath,datetime.now().strftime('%Y%m%d%H%M%S'))

        if not os.path.exists(self.logFilePath):
            os.mkdir(self.logFilePath)
        filePath=os.path.join(self.logFilePath,'test.log')

        #设置log输出格式
        log_format='[%(asctime)s][%(levelname)s][%(filename)s]->%(lineno)d %(message)s'

        logging.basicConfig(format=log_format,filename=filePath,level=logging.DEBUG)

        self.logger=logging.getLogger()

        console=logging.StreamHandler()
        console.setLevel(logging.DEBUG)

        fomater=logging.Formatter(log_format)
        console.setFormatter(fomater)
        self.logger.addHandler(console)

    def get_logger(self):
            """
            get logger
            :return:
            """
            return self.logger


    def get_report_path(self):
        reportpath = os.path.join(self.logFilePath, 'report.html')
        return reportpath

    def get_result_path(self):
        return self.logFilePath

    def d(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def i(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def w(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def c(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)

    def e(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)


class MyLog:

    log=None
    mutex=threading.Lock()

    @staticmethod
    def get_log():

        if MyLog.log is None:

            MyLog.mutex.acquire()
            try:
                MyLog.log=log()
            finally:
                MyLog.mutex.release()
        return MyLog.log

if __name__=='__main__':

  pass
