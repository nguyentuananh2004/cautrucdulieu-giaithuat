def USCLN(a, b):
    if b == 0:
        return a
    else:
        return USCLN(b, a % b)


print(USCLN(12, 24))
