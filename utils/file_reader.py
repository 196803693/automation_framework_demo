import os
import yaml

class YamlReader:
    def __init__(self,yaml_file_path):
        if os.path.exists(yaml_file_path):
            self.yaml_path = yaml_file_path
        else:
            raise FileNotFoundError #抛出文件找不到的异常
        self._data = None
    @property   #让方法可以像属性一样访问，防止随意篡改
    def data(self):
        if not self._data:
            with open(self.yaml_path,'r') as f:
                self._data = list(yaml.safe_load_all(f))
                print('读取文件')
        return self._data
if __name__ == '__main__':
    base_path = os.path.dirname(os.getcwd())
    yaml_path = os.path.join(base_path, 'config', 'test.yaml')
    yr = YamlReader(yaml_path)
    print(yr.data)