import json
import os
import time


def process(func):
    def wrapper(*args):
        print(func.__name__)
        start = time.time()
        func(*args)
        finish = time.time()
        print(finish - start)
    return wrapper


def get_sum(file, name_file):
    try:
        for line in file.readlines():
            data = json.loads(line)
            file.close()
            return name_file + ": sum = " + str(sum(data)) + "\n"
    except Exception:
        file.close()
        remove_file_catalog_error('catalog_writing_files', 'catalog_error_files', name_file)


def record_to_file(cat_result, file, txt=None):
        file = open(os.path.join(os.path.abspath('catalogs'), cat_result, file), 'a', encoding='utf-8')
        file.writelines(txt)
        file.close()


def remove_file_catalog_error(cat_read=None, cat_err=None, file=None):
    src = os.path.join(os.path.abspath('catalogs'), cat_read, file)
    dst = os.path.join(os.path.abspath('catalogs'), cat_err, file)
    os.replace(src, dst)


@process
def monitor(cat_read=None, cat_result=None, cat_err=None):
    list_to_data_result = []
    tuple_path_files = os.walk(os.path.abspath('catalogs'))
    print(tuple_path_files)
    list_file = [file[2] for file in tuple_path_files]
    list_txt = list(filter(lambda file: file if file.split('.')[1] == 'txt' else \
                    remove_file_catalog_error(cat_read, cat_err, file), list_file[3]))
    for txt in list_txt:
        try:
            file = open(os.path.join(os.path.abspath('catalogs'), cat_read, txt), 'r', encoding='utf-8')
            text_sum = get_sum(file, txt)
            if text_sum is not None:
                list_to_data_result.append(text_sum)
                os.remove(os.path.join(os.path.abspath('catalogs'), cat_read, txt))
        except Exception:
            file.close()
            remove_file_catalog_error('catalog_writing_files', 'catalog_error_files', txt)

    for txt in list_to_data_result:
        record_to_file(cat_result, 'result.txt', txt)
