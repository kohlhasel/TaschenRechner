from typing import List


def dumme_addition(a:int, b:int):
    if a == 0:
        return b
    if b ==0:
        return a+1
    else:
        return dumme_addition(a - 1, b - 1) + 2

def groesste_n_zahlen_implementation_1(liste:List[int], n:int):
    return sorted(liste)[-n:]

def groesste_n_zahlen_implementation_2(liste:List[int], n: int):
    return sorted(liste, reverse=True)[:n]
