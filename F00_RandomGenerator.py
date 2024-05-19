import time

def rng():
    seed = int(time.time())
    a = 2**3
    c = 100
    m = 1000000
    angka = (a * seed + c) % m
    return angka

def interval(minimal,maksimal):
    range_angka = minimal + (rng() % (maksimal-minimal + 1))
    return range_angka

