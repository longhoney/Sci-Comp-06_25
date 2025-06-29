# Lặp số lần cố định với `for`
print("Vòng lặp số lần cố định, bắt đầu từ 0")
for i in range(5):  # Lặp 5 lần từ 0 đến 4
    print("Lần lặp thứ:", i)
  
print("Vòng lặp số lần cố định trong 1 khoảng cho trước")
for i in range(1,7):  # Lặp 6 lần từ 1 đến 7
    print("Lần lặp thứ:", i)  

# Lặp theo điều kiện với `while`
print("Vòng lặp theo điều kiện")
count = 0 #gán 0 thành giá trị ban đầu của biến count
while count < 5:  # Tiếp tục lặp khi `count` nhỏ hơn 5
    print("Lần lặp thứ:", count)
    count += 1  # Tăng giá trị của `count` mỗi lần lặp
		#vòng lặp dừng lại khi count =5
"""
count = 5
while count > 0:  # Tiếp tục lặp khi `count` nhỏ hơn 5
    print("Lần lặp thứ:", count)
    count -= 1  # Giảm giá trị của `count` mỗi lần lặp
		#vòng lặp dừng lại khi count =1
"""