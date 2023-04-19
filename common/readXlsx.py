import pandas as pd
import os
import sys
import json

def add_syspath():
    path = os.path.join(
        (os.path.dirname((os.path.dirname(os.path.abspath(__file__))))))
    sys.path.append(path)


add_syspath()
print(sys.path)


class ReadFile():
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.file_obj = pd.read_excel(self.file_path)

    def read_excel(self):
        return self.file_obj

    def read_iloc(self,*row_name):
        return self.file_obj.iloc[row_name]

    def read_iat(self,*row_name):
        return self.file_obj.iat[row_name]

if __name__ == "__mai__":
    f = ReadFile('test_data/api/api_test_case.xlsx')


    print(f.read_iat(0,3))
    print(f.read_iat(0,5))
    print(json.loads(f.read_iat(0,6))['code'])
    # print(f.read_iat(0,7))


