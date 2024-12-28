from typing import List


def dumme_multiplikation(a: int, b: int):
    # Abbruchbedingungen für 0
    if a == 0 or b == 0:
        return 0
    # Abbruchbedingung für a = 1
    if a == 1:
        return b
    # Abbruchbedingung für b = 1
    if b == 1:
        return a
    # Rekursiver Schritt
    else:
        return dumme_multiplikation(a-1, b) + b

def groesste_n_zahlen_implementation_1(liste:List[int], n:int):
    return sorted(liste)[-n:]

def groesste_n_zahlen_implementation_2(liste:List[int], n: int):
    return sorted(liste, reverse=True)[:n]
