def mdc (z, d):
    while d != 0:
        z, d = d, z %d
    return z