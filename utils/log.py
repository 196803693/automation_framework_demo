import logging
from logging.handlers import TimedRotatingFileHandler
from utils.config import LOG_PAHT,Config
import os


class Logger:
    def __init__(self,logger_name = 'framework'):
        self.logger = logging.getLogger(logger_name)
        # self.logger.setLevel(logging.INFO)
        logging.root.setLevel(logging.NOTSET)
        log_cfg = Config().get('log')
        print(log_cfg)
        self.log_file_name = log_cfg.get('file_name') if log_cfg and log_cfg.get('file_name') else 'test.log'
        #日志输出的级别
        self.console_output_level = log_cfg.get('consle_level') if log_cfg and log_cfg.get('consle_level') else 'WARNING'
        self.file_output_level = log_cfg.get('file_level') if log_cfg and log_cfg.get('file_level') else 'DEBUG'
        #保留的日志的数量
        self.backup_count = log_cfg.get('backup') if log_cfg and log_cfg.get('backup') else 5
        #日志输出格式
        pattern = log_cfg.get('pattern') if log_cfg and log_cfg.get('pattenr') else \
            '%(name)s - %(levelname)s - %(asctime)s - %(message)s'
        self.formatter = logging.Formatter(pattern)


    def get_logger(self):
        if not self.logger.handlers:    #避免重复日志
            console_hdl = logging.StreamHandler()
            console_hdl.setLevel(self.console_output_level)
            console_hdl.setFormatter(self.formatter)
            self.logger.addHandler(console_hdl)
            #每天重新创建一个日志文件，保留backupCount份
            file_hdl = TimedRotatingFileHandler(filename=os.path.join(LOG_PAHT,self.log_file_name),
                                                when='D',
                                                interval=1,
                                                backupCount=self.backup_count,
                                                delay=False,
                                                encoding='utf-8'
                                                )
            file_hdl.setLevel(self.file_output_level)
            file_hdl.setFormatter(self.formatter)
            self.logger.addHandler(file_hdl)
        return self.logger
logger = Logger().get_logger()
if __name__ == '__main__':
    logger.info('info message')
    logger.debug('debug')
    logger.warning('warnning')