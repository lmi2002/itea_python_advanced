import xlrd
import xlwt
import os
import csv
import string


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
            self.list_data_users.append({'user_name': user_name, 'email': email, 'joined': joined})
        return self.list_data_users


class FileConverter:

    def converter_file_csv(self, name_file, data_list):
        with open(name_file + '.csv', 'w', newline='') as csvfile:
            fieldnames = ['user_name', 'email', 'joined']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            for row in data_list:
                writer.writerow(row)






d = ExcelFile()
data_list = d.get_list()
f = FileConverter()
f.open_file_csv('dim', data_list)