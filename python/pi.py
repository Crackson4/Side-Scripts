pi = float()

limit = 76651


def main():
    global pi
    pi = 3
    i = 1
    while i < limit:
        sign = -1 if i % 2 == 0 else 1
        two_i = 2 * i
        pi += sign * 4 / (two_i * (two_i + 1) * (two_i + 2))
        i += 1
    print(pi)
    print(len(str(pi)) - 2)


if __name__ == "__main__":
    main()
