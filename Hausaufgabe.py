from typing import List


def dumme_multiplikation(a:int, b:int):
    ergebnis = 0
    for _ in range(b):
        ergebnis += a
    return ergebnis


def groesste_n_zahlen_implementation_1(liste:List[int], n:int):
    return sorted(liste)[-n:]

def groesste_n_zahlen_implementation_2(liste:List[int], n: int):
    return sorted(liste, reverse=True)[:n]
