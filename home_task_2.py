import os


def monitor(cat_write, cat_result, cat_err):

    tuple_path_files = (os.walk(os.path.abspath('catalogs')))
    list_file = [file[2] for file in tuple_path_files]
    print(list_file[2])
    print(os.path.abspath('catalog_result_files'))


def remove_file_catalog_error():
    r = os.path.join(os.path.abspath('catalog_result_files'), 'r.txt')
    d = os.path.join(os.path.abspath('catalog_error_files'), 'r.txt')
    os.rename(r, d)



monitor('catalog_writing_files', 'catalog_result_files', 'catalog_error_files')

