def bintidec(n):
    decimal = 0
    power = 0
    
    while n > 0:
        ld = n % 10
        decimal = decimal + ld * (2 ** power)
        power += 1
        n //= 10
    
    print(decimal)


def dectobin(n):
    bin_num = 0
    power = 0
    
    while n > 0:
        rem = n % 2
        bin_num = bin_num + rem * (10 ** power)
        power += 1
        n //= 2
    
    print(bin_num)


# ---------- main ----------
dectobin(5)     # output → 101
# bintidec(101) # output → 5
