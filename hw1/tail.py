import sys

def tail(input_files=None):
    """
    Функция для вывода последних 10 строк из файла или последних 17 строк из stdin.
    :param input_files: Список путей к файлам (если None, читает из stdin)
    """
    if input_files:
        for input_file in input_files:
            with open(input_file, 'r') as file:
                lines = file.readlines()[-10:]
                if len(input_files) > 1:
                    print(f'==> {input_file} <==')
                for line in lines:
                    print(line, end='')

    else:
        lines = sys.stdin.readlines()[-17:]
        for line in lines:
            print(line, end='')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        tail(sys.argv[1:])
    else:
        tail()