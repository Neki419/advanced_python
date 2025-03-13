import sys

def wc_line_word_byte(input_files=None):
    """
    Аналог утилиты wc (без дополнительных опций).
    Выводит количество `\n` (как `wc -l`), слов и байт.
    """
    results = []

    if input_files:
        total_l = total_wc = total_b = 0
        for filename in input_files:
            with open(filename, 'rb') as f:
                data = f.read()

            b = len(data)  # Количество байт
            l = data.count(b'\n')  # Количество символов `\n` (как `wc -l`)

            # Подсчёт слов
            wc = sum(len(line.decode('utf-8', errors='replace').split()) for line in data.splitlines())

            results.append((l, wc, b, filename))
            total_l += l
            total_wc += wc
            total_b += b

        if len(results) > 1:
            results.append((total_l, total_wc, total_b, 'итого'))

    else:
        data = sys.stdin.buffer.read()
        b = len(data)
        l = data.count(b'\n')
        wc = sum(len(line.decode('utf-8', errors='replace').split()) for line in data.splitlines())

        results.append((l, wc, b, None))

    return results

def main():
    input_files = sys.argv[1:]
    results = wc_line_word_byte(input_files if input_files else None)

    for (l, wc, b, filename) in results:
        if filename is None:
            print(l, wc, b)
        else:
            print(l, wc, b, filename)

if __name__ == "__main__":
    main()