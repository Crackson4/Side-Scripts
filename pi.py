import numpy as np

fast_flag = False


def slow():
    pi = float(0)
    i = 0
    while True:
        sign = 1 if i % 2 == 0 else -1
        pi += sign * 4 / (2 * i + 1)
        if i % 10000 == 0:
            print(pi)
        i += 1


if __name__ == "__main__":
    slow()
