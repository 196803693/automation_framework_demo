from utils.file_reader import YamlReader
import os

BASE_PATH = os.path.dirname(os.getcwd())
CONFIG_FILE_PATH = os.path.join(BASE_PATH, 'config', 'config.yml')
DATA_PAHT = os.path.join(BASE_PATH, 'data')
DRIVER_PATH = os.path.join(BASE_PATH, 'driver')
LOG_PAHT = os.path.join(BASE_PATH, 'log')
REPORT_PAHT = os.path.join(BASE_PATH, 'report')

class Config:
    def __init__(self,config_path=CONFIG_FILE_PATH):
        self.config_list = YamlReader(config_path).data
    def get(self,element,index=0):
        '''
        yaml是可以通过'---'分节的。用YamlReader读取返回的是一个list，第一项是默认的节，如果有多个节，可以传入index来获取。
        这样我们其实可以把框架相关的配置放在默认节，其他的关于项目的配置放在其他节中。可以在框架中实现多个项目的测试。
        '''
        print('get element')
        return self.config_list[index].get(element)