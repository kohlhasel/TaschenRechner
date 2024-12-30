from typing import List

def dumme_multiplikation(a:int, b:int):
    if a == 0 or b == 0:
        return 0  

    if a == 1:
        return b
    if b == 1:
        return a
    else:
        return a + dumme_multiplikation(a, b - 1)

def groesste_n_zahlen_implementation_1(liste:List[int], n:int):
    return sorted(liste)[-n:]

def groesste_n_zahlen_implementation_2(liste:List[int], n: int):
    return sorted(liste, reverse=True)[:n]
