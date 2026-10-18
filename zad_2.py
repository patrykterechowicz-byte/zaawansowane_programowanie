import random


def show(names):
    for n in names:
        print(n)


def mul(nums):
    result = []
    for n in nums:
        result.append(n * 2)

    return result


def mul_v2(nums):
    return [n * 2 for n in nums]


def filter_even(nums):
    for n in nums:
        if n % 2 == 0:
            print(n)


def every_other(nums):
    skip = False
    for n in nums:
        skip = not skip
        if skip:
            continue
        print(n)


if __name__ == "__main__":
    show(["iga", "patryk", "julia", "imie1", "imie2"])
    print(mul([1, 2, 3, 4, 5]))
    print(mul_v2([1, 2, 3, 4, 5]))
    filter_even(list(range(10)))
    every_other(list(range(10)))
