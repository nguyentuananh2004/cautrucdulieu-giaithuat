#Bài 4: cài đặt queue
class Queue:
    # Khởi tạo một danh sách rỗng self.items để lưu trữ các phần tử của queue
    def __init__(self):
        self.front = 0
        self.rear = -1
        self.size = 0
        self.items = []
    # Kiểm tra xem queue có rỗng hay không
    def is_empty(self):
        return self.items == []
    # Thêm một phần tử mới vào cuối danh sách
    def enqueue(self, item):
        self.rear += 1
        self.items.append(item)
        self.size += 1
    # Lấy ra và trả về phần tử đầu tiên của danh sách. Nếu danh sách rỗng, trả về None
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        item = self.items[self.front]
        self.front += 1
        self.size -= 1
        return item
        return self.items.pop(0)
    # Trả về phần tử đầu tiên của queue hoặc trả về None nếu queue rỗng
    def front_q(self):
      if self.is_empty():
        return None
      return self.items[self.front]
    # Trả về số lượng phần tử trong danh sách
    def size_q(self):
        return self.size
    # In ra các phần tử có trong queue
    def print_q(self):
        if self.is_empty():
            return "Queue is empty"
        return ', '.join(str(item) for item in self.items[self.front:self.rear+1])

queue = Queue()
print('Queue có rỗng hay không: ',queue.is_empty())

# Thêm phần tử mới vào đầu stack
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print('Queue ở hiện tại: ',queue.print_q())
print('Size của queue: ',queue.size_q())

# Loại bỏ và trả về phần tử đầu tiên của queue
print('Loại bỏ và trả về phần tử đầu tiên: ',queue.dequeue())
# Trả về phần tử cuối cùng của queue nhưng không loại bỏ nó
print('Trả về phần tử đầu tiên của queue: ',queue.front_q())
# In ra list queue ở hiện tại và số phần tử có trong queue
print('Queue hiện tại: ',queue.print_q())
print('Size của queue: ',queue.size_q())