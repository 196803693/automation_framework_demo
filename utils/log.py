import logging
from logging.handlers import TimedRotatingFileHandler
from utils.config import LOG_PAHT
import os


class Logger:
    def __init__(self,logger_name = 'framework'):
        self.logger = logging.getLogger(logger_name)
        # self.logger.setLevel(logging.INFO)
        logging.root.setLevel(logging.NOTSET)
        self.log_file_name = 'test.log'
        #日志输出格式
        self.formatter = logging.Formatter('%(name)s - %(levelname)s - %(asctime)s - %(message)s')

    def get_logger(self):
        if not self.logger.handlers:    #避免重复日志
            print('StreamHandler')
            console_hdl = logging.StreamHandler()
            console_hdl.setLevel(logging.INFO)
            console_hdl.setFormatter(self.formatter)
            self.logger.addHandler(console_hdl)
            #每天重新创建一个日志文件，保留backupCount份
            file_hdl = TimedRotatingFileHandler(filename=os.path.join(LOG_PAHT,self.log_file_name),
                                                when='D',
                                                interval=1,
                                                backupCount=5,
                                                delay=False,
                                                encoding='utf-8'
                                                )
            file_hdl.setLevel(logging.INFO)
            file_hdl.setFormatter(self.formatter)
            self.logger.addHandler(file_hdl)
        return self.logger
logger = Logger().get_logger()
if __name__ == '__main__':
    logger.info('info message')