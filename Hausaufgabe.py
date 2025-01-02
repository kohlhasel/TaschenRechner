from typing import List


def dumme_multiplikation(a:int, b:int):
    if a == 0 or b == 0: # Multiplikation mit 0 ergibt 0
        return 0
    if a == 1:            # Multiplikation mit 1 ergibt b
        return b
    return b + dumme_multiplikation(a -1, b) #rekrusive Addition

def groesste_n_zahlen_implementation_1(liste:List[int], n:int):
    return sorted(liste)[-n:]

def groesste_n_zahlen_implementation_2(liste:List[int], n: int):
    return sorted(liste, reverse=True)[:n]
