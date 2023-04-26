def tinh_giai_thua(n):
    giai_thua = 1
    for i in range(1, n+1): #vòng lặp i với phạm vi từ 1 đến n+1
        giai_thua = giai_thua*i #giá trị giai thừa bằng giá trị giai thừa ban đầu nhân với i
    return giai_thua
print(tinh_giai_thua(4))
