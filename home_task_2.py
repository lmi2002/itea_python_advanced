import os


def monitor(cat_write, cat_result, cat_err):
    tuple_path_files = (os.walk(os.path.abspath('catalogs')))
    list_file = [file[2] for file in tuple_path_files]
    t = list_file[3]
    r = list(map(lambda file: file if file.split('.')[1] == 'txt' else remove_file_catalog_error(cat_write, cat_err, file), list_file[3]))
    print(r)

def remove_file_catalog_error(cat_write, cat_err, file):
    src = os.path.join(os.path.abspath('catalogs'), cat_write, file)
    dst = os.path.join(os.path.abspath('catalogs'), cat_err, file)
    os.replace(src, dst)



monitor('catalog_writing_files', 'catalog_result_files', 'catalog_error_files')
