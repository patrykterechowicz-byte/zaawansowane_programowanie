def join_and_dedup(l1: list[int], l2: list[int]) -> list[int]:
    return [n**3 for n in list(set(l1) | set(l2))]
