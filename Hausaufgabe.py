from typing import List

def dumme_multiplikation(a: int, b: int):
    if a == 0 or b == 0:  # Multiplikation mit 0
        return 0
    if a == 1:  # 1 * b = b
        return b
    if b == 1:  # a * 1 = a
        return a
    if b < 0:  # Behandlung von negativen b
        return -dumme_multiplikation(a, -b)
    if a < 0:  # Behandlung von negativen a
        return -dumme_multiplikation(-a, b)
    return a + dumme_multiplikation(a, b - 1)  # Rekursion für normale Multiplikation

def groesste_n_zahlen_implementation_1(liste: List[int], n: int):
    return sorted(liste)[-n:][::-1]

def groesste_n_zahlen_implementation_2(liste:List[int], n: int):
    return sorted(liste, reverse=True)[:n]
