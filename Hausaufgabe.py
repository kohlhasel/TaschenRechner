from typing import List


def dumme_multiplikation(a: int, b: int):
    # Wenn einer der Werte 0 ist, gibt die Funktion 0 zurück
    if a == 0 or b == 0:
        return 0
    if a == 1:
        return b  # a * 1 = b, das ist korrekt
    if b == 1:
        return a  # b * 1 = a, das ist korrekt
    else:
        return a * b  # Die richtige Multiplikation der beiden Zahlen



def groesste_n_zahlen_implementation_1(liste:List[int], n:int):
    return sorted(liste)[-n:]

def groesste_n_zahlen_implementation_2(liste:List[int], n: int):
    return sorted(liste, reverse=True)[:n]
