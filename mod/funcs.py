from collections import Counter
import math
import re
from functools import cache


def one():
    return 1


pat_whitespace = re.compile(r"\s")


def is_palindrome(text: str) -> bool:
    text = text.lower()
    text = pat_whitespace.sub("", text)
    n = len(text)
    for i in range(math.floor(n / 2)):
        if text[i] != text[n - i - 1]:
            return False
    return True


@cache
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError
    if n == 1 or n == 0:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def count_vowels(text: str) -> int:
    vowels = "aąeęioóuy"
    count = 0
    for c in text.lower():
        if c in vowels:
            count += 1
    return count


def calculate_discount(price: float, discount: float) -> float:
    if discount < 0.0 or discount > 1.0:
        raise ValueError
    return price * (1.0 - discount)


def flatten_list(nested_list: list) -> list:
    flattened = []
    for el in nested_list:
        if isinstance(el, list):
            for inner_el in flatten_list(el):
                flattened.append(inner_el)
        else:
            flattened.append(el)

    return flattened


pat_punctuation = re.compile("[!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]")


def word_frequencies(text: str) -> dict:
    # preprocess, remove punctuation
    text = text.strip().lower()
    text = pat_punctuation.sub("", text)
    return dict(Counter(text.split()))


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
