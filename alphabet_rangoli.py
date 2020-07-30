# https://www.hackerrank.com/challenges/alphabet-rangoli/problem


def print_rangoli(size):
    height = size*2 - 1
    line_list = []
    line_char_count = 1
    dash_count = height - 1

    for i in range(height):
        char_list = []
        char_in_decimal = ord('a') + size - 1

        for x in range(line_char_count):
            if line_char_count == 1:
                char_list.append(chr(char_in_decimal))
                continue
            if x < line_char_count // 2:
                char_list.append(chr(char_in_decimal))
                char_in_decimal -= 1
                continue
            if x >= line_char_count // 2:
                char_list.append(chr(char_in_decimal))
                char_in_decimal += 1
                continue

        if i >= size:
            line_list = line_list + line_list[i-2::-1]
            break

        line_list.append('-'*dash_count + '-'.join(char_list) + '-'*dash_count)
        dash_count -= 2
        line_char_count += 2

    print('\n'.join(line_list))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)