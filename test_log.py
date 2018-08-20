#coding=utf-8


from log import *

log = MyLog.get_log()
logger = log.get_logger()


logger.info('info')

#log.LOG_DEBUG('debug')
#log.LOG_ERROR('error')