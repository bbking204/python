import json

def save_date(file_name: str, list_of_objects: list):
    with open(file_name, 'w') as file:
        file.write(json.dumps(list_of_objects))


def load_data(file_name: str):
    with open(file_name, 'r') as file:
        return json.loads(file.read())

my_list = ["this", "is", "a_list", True, 420, 6.9]
save_date("/Users/user/Documents/pythonProjects/python/proj/funcs/data_file.txt", my_list)
load_data("/Users/user/Documents/pythonProjects/python/proj/funcs/data_file.txt")