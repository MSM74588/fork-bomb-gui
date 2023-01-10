import py_compile
import os


def path_finder(folder_name, filename):
    file_location = os.path.join(os.path.dirname(__file__), folder_name ,filename)
    return file_location

file_path = path_finder(".","main.py")

## OBFUSCATE
py_compile.compile(file_path)

