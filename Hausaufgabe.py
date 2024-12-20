from typing import List


def dumme_addition(a:int, b:int):
    if a == 0:
        return b
    if b ==0:
        return a
    else:
        return 1 + dumme_addition(a, b - 1) 

def groesste_n_zahlen_implementation_1(liste:List[int], n:int):
    return sorted(liste)[-n:]

def groesste_n_zahlen_implementation_2(liste:List[int], n: int):
    return sorted(liste, reverse=True)[:n]
