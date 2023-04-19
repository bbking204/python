import shutil
import os

def dirCopy(input_path, output_path, extentions=None):
    if extentions is None:
        shutil.copytree(input_path, output_path)
    else:
        [shutil.copy2(os.path.join(input_path, file), os.path.join(output_path, file)) for file in os.listdir(input_path) if os.path.splitext(file)[1] in extentions]


extensions = [".mp4", ".jpeg"]
dirCopy('/Users/user/Documents/pythonProjects/python/proj/src', '/Users/user/Documents/pythonProjects/python/proj/dst', extensions)