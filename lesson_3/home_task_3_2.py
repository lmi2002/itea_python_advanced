import xlrd
import xlwt
import os


class ExcelFile:
    def __init__(self):
        self.path_file = r'C:\Users\Star\PycharmProjects\itea_python_advanced\lesson_3\Data of users.xlsx'
        self.list_data_users = []

    def _open_excel_file(self):
        return xlrd.open_workbook(self.path_file)

    def get_list(self):
        rb = self._open_excel_file()
        sheet = rb.sheet_by_index(0)
        for rownum in range(sheet.nrows):
            row = sheet.row_values(rownum)
            user_name = row[0]
            email = row[1]
            joined = xlrd.xldate_as_tuple(row[2], rb.datemode)
            self.list_data_users.append([user_name, email, joined])
        return self.list_data_users

d = ExcelFile()
print(d.get_list())