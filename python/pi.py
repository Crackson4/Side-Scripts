from decimal import Decimal


def main():
    pi = Decimal(3)
    i = 1
    while True:
        sign = -1 if i % 2 == 0 else 1
        two_i = 2 * i
        pi += Decimal(sign * 4 / (two_i * (two_i + 1) * (two_i + 2)))
        i += 1
        if i % 100000 == 0:
            print(pi)


if __name__ == "__main__":
    main()
