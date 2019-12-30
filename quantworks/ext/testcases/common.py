import os


def get_data_file_path(fileName):
    return os.path.join(os.path.split(__file__)[0], "data", fileName)