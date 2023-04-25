def tinh_giai_thua(n):
    giai_thua = 1
    for i in range(1, n+1):
        giai_thua = giai_thua*i
    return giai_thua
print(tinh_giai_thua(4))
