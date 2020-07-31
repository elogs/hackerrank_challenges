# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple


if __name__ == '__main__':
    n = int(input())
    Student = namedtuple('Student', input())
    records = [Student._make(input().split()) for _ in range(n)]

    print(round(sum([int(rec.MARKS) for rec in records])/n, 2))