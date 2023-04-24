### Tháp Hà Nội

# Recursive Python function to solve the tower of hanoi

def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Di chuyển Đĩa 1 từ cột nguồn", source, "đến cột nhận", destination)
        return
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    print("Di chuyển Đĩa", n, "từ cột nguồn", source, "đến cột nhận", destination)
    TowerOfHanoi(n - 1, auxiliary, destination, source)


n = 4
TowerOfHanoi(n, 'A', 'B', 'C')




