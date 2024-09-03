
FILEPATH="todos.txt"

def open_todo(filepath=FILEPATH):
    """function to read a file"""
    with open(filepath, 'r') as file:
        list_1 = file.readlines()
    return list_1

def write_todo(todos_arg,filepath=FILEPATH):
    """function to write in a file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


print(__name__)
if __name__=="__main__":#means we are running functions.py directly
    print("hello")