# Khai báo danh sách
colors = ["red", "green", "blue"]

# Truy xuất phần tử
print(colors[0])  # phần tử vị trí 0 (đầu tiên) có giá trị là "red"

# Thay đổi giá trị
colors[1] = "yellow"
print(colors)  # ["red", "yellow", "blue"]

# Thêm phần tử vào danh sách
colors.append("white")
print(colors)  # ["red", "yellow", "blue", "white"]

# Duyệt qua danh sách
for color in colors: #color là các biến trong list "colors"
    print(color)
