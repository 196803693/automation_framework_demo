import os
from builtins import FileNotFoundError

import yaml
import xlrd,xlwt
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
                # print('读取文件')
        return self._data
class SheetTypeError(Exception):
    pass
class ExcelReader:
    def __init__(self,file_path,sheet=0,title_line=True):
        if os.path.exists(file_path):
            self.excel_path = file_path
        else: raise FileNotFoundError
        self.sheet = sheet
        self._data = list()
        self.title_line = title_line
    @property
    def data(self):
        if not self._data:
            workbook = xlrd.open_workbook(self.excel_path)
            if type(self.sheet) not in [int,str]:
                raise SheetTypeError('Please pass sheet type in <type int> or <type str>,not %s' %type(self.sheet))
            elif type(self.sheet) == int:
                st = workbook.sheet_by_index(self.sheet)
            else:
                st = workbook.sheet_by_name(self.sheet)
            title = st.row_values(0)
            for r in range(1,st.nrows):
                #依次遍历其余行，与首行组成dict，拼到_data中
                self._data.append(dict(zip(title,st.row_values(r))))
        return self._data
if __name__ == '__main__':
    base_path = os.path.dirname(os.getcwd())
    yaml_path = os.path.join(base_path, 'config', 'test.yaml')
    yr = YamlReader(yaml_path)
    print(yr.data)
    excel_path = os.path.join(base_path,'data','user_account.xlsx')
    er = ExcelReader(excel_path,sheet=0)
    print(er.data)

