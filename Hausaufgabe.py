from typing import List


def dumme_multiplikation(a:int, b:int):
    # Prüfen, ob einer der Werte 0 ist
    if a == 0 or b == 0:
        return 0  # Multiplikation mit 0 ergibt immer 0

    if a == 1:
        return b
    if b == 1:
        return a
    else:
        # Die rekursive Berechnung bleibt unverändert
        return dumme_multiplikation(a - 1, b - 1) + a + b - 1

def groesste_n_zahlen_implementation_1(liste:List[int], n:int):
    return sorted(liste)[-n:]

def groesste_n_zahlen_implementation_2(liste:List[int], n: int):
    return sorted(liste, reverse=True)[:n]
