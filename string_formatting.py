# https://www.hackerrank.com/challenges/python-string-formatting/problem


def print_formatted(number):
    for i in range(1, number + 1):
        deci = "{0:d}".format(i)
        octa = "{0:o}".format(i)
        hexa = "{0:X}".format(i)
        bina = "{0:b}".format(i)

        w = len(str("{0:b}".format(number))) + 1
        print("{:>{f}}{:>{w}}{:>{w}}{:>{w}}".format(deci, octa, hexa, bina, f=w - 1, w=w))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
