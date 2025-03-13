import sys

def number_lines(input_file=None):
    """
    Функция для нумерации строк из файла или stdin.
    :param input_file: Путь к файлу (если None, читает из stdin)
    """
    if input_file:
        with open(input_file, 'r') as file:
            lines = file.readlines()
    else:
        lines = sys.stdin.readlines()

    for i, line in enumerate(lines, start=1):
        print(f"    {i}  {line.rstrip()}", end='\n')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        number_lines(sys.argv[1])
    else:
        number_lines()