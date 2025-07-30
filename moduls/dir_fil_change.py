import os
import shutil
def del_dir(dir_name):
    path = os.path.join(os.getcwd(), dir_name)
    if os.path.exists(path):
        os.rmdir(path)
        pass
def create_dir(dir_name):
    path = os.path.join(os.getcwd(), dir_name)
    if not os.path.exists(path):
        os.mkdir(path)
        pass
def del_file(file_name):
    path = os.path.join(os.getcwd(), file_name)
    if os.path.exists(path):
        os.remove(path)
        pass
def create_file(file_name):
    path = os.path.join(os.getcwd(), file_name)
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            f.write("")
            pass
def copy_file(file_name, file_name_new):
    if '.' in file_name_new:
        path = os.path.join(os.getcwd(), file_name_new)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(file_name)
    else:
        path = os.path.join(os.getcwd(), file_name)
        path_2 = os.path.join(os.getcwd(), file_name_new)
        shutil.copytree(path, path_2)
    pass