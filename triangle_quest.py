# https://www.hackerrank.com/challenges/python-quest-1/problem

if __name__ == '__main__':
    for i in range(1, int(input())):
        print(i * (sum(map(lambda x: 10**x, list(range(1, i)))) + 1))
