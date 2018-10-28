import time

from home_task_2 import monitor

while True:
    monitor('catalog_writing_files', 'catalog_result_files', 'catalog_error_files')
    time.sleep(5)