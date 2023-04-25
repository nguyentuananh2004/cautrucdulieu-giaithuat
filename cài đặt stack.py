#Bài 3: cài đặt stack
# Định nghĩa một lớp Stack để quản lý các phần tử trong stack:
class Stack:

	# Khởi tạo stack với một mảng rỗng
	def __init__(self):
		self.items = []

	# Kiểm tra xem stack có rỗng hay không, nếu số lượng phần tử trong mảng bằng 0 thì stack rỗng
	def is_empty(self):
		return len(self.items) == 0

	# Thêm một phần tử mới vào đầu stack, thêm phần tử mới vào cuối mảng
	def push(self, data):
		self.items.append(data)

	# Loại bỏ và trả về phần tử đầu tiên của stack, nếu stack rỗng thì trả về None
	def pop(self):
		if not self.is_empty():
			return self.items.pop()

	# Trả về phần tử đầu tiên của stack, nhưng không loại bỏ phần tử đó, nếu stack rỗng thì trả về None
	def peek(self):
		if not self.is_empty():
			return self.items[0]

	# Trả về kích thước stack
	def size(self):
		return len(self.items)


stack = Stack()
print('Stack có rỗng hay không: ', stack.is_empty())  # True

# Thêm phần tử mới vào đầu stack
stack.push(1)
stack.push(2)
stack.push(3)
print('Stack: ', stack.items)
print('Size của stack: ', stack.size())

print('Loại bỏ và trả về phần tử đầu tiên: ', stack.pop())
print('Stack hiện tại: ', stack.items)
print('Trả về phần tử đầu tiên của stack: ', stack.peek())
print('Size của stack: ', stack.size())



