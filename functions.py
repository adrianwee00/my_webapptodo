FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH) -> list:
    """This is to read a file and this string is called a doc string"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def file_write(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("hello")
    print("test")
    print("wow")
    print("hey")
