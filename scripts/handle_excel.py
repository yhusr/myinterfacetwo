"""
Time:2020/1/31 0031
"""
import openpyxl
from scripts.handle_os import EXCEL_PATH


class GetObj:
    pass


class HandleExcel:
    def __init__(self, sheetname, filepath=None):
        if filepath:
            self.filepath = filepath
        else:
            self.filepath = EXCEL_PATH
        self.sheetname = sheetname

    # 打开excel
    def open_excel(self):
        self.workbook = openpyxl.load_workbook(self.filepath)
        self.sh = self.workbook[self.sheetname]

    # 读取excel内容
    def read_excel(self):
        self.open_excel()
        excel_values = list(self.sh.rows)
        head_value = [h.value for h in excel_values[0]]
        obj_li = []
        for ob in excel_values[1:]:
            go = GetObj()
            value_li = [v.value for v in ob]
            hv_zip = zip(head_value, value_li)
            for hv in hv_zip:
                setattr(go, hv[0], hv[1])
            obj_li.append(go)
        self.workbook.close()
        return obj_li

    # 写入内容到excel中
    def write_excel(self, row_num, col_num, value):
        self.open_excel()
        self.sh.cell(row_num, col_num, value)
        self.workbook.save(self.filepath)
        self.workbook.close()


