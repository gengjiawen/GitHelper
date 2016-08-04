import os

def get_immdiate_dir(folder):
    file_list = [os.path.abspath(os.path.join(folder, i)) for i in next(os.walk(folder))[1]]
    return file_list
