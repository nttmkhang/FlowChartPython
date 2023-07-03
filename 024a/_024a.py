
print("Bài 024a, Phù Đức Quân")
# Nhập số nguyên dương n từ người dùng
n = int(input("Nhập một số nguyên dương n: "))

# Gọi hàm để tìm chữ số hàng trăm của n

hundreds_digit = int((n / 100) % 10)

# In kết quả
print("Chữ số hàng trăm của", n, "là:", hundreds_digit)
