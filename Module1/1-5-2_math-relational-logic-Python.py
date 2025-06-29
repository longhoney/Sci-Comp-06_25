from machine import Pin

# Khởi tạo biến
a = 10; b = 3; c = 5

# Thực hiện phép toán số học
sum_result = a + b   # Cộng, Add(ition)
difference_result = a - b  # Trừ, Sub(traction)
product_result = a * b  # Nhân, Multi(plication)
quotient_result = a / b  # Chia, Div(ision)
floor_result_1 = a // b #Chia lấy số nguyên, Floor Div(ision)
floor_result_2 = -a // b
remainder_result = a % b  # Chia lấy dư, Modulus
    #a % b = a - b * (a // b)
power_result = a ** b  # Lũy thừa, Exponentitaion

# In kết quả phép toán số học
print("Tổng:", sum_result)
print("Hiệu:", difference_result)
print("Tích:", product_result)
print("Thương:", quotient_result)
print("Thương lấy số nguyên:", floor_result_1)
print("-a//b:", floor_result_2)
print("Dư:", remainder_result)
print("Lũy thừa:", power_result)

# Thực hiện phép toán so sánh
is_equal = (a == b)  # Bằng
is_not_equal = (a != c)  # Khác
is_greater = (a > c)  # Lớn hơn
is_less = (a < c)  # Nhỏ hơn
is_greater_equal = (a >= c)  # Lớn hơn hoặc bằng
is_less_equal = (a <= b)  # Nhỏ hơn hoặc bằng

# In kết quả phép toán so sánh
print("Bằng nhau:", is_equal)
print("Khác nhau:", is_not_equal)
print("Lớn hơn:", is_greater)
print("Nhỏ hơn:", is_less)
print("Lớn hơn hoặc bằng:", is_greater_equal)
print("Nhỏ hơn hoặc bằng:", is_less_equal)

# Thực hiện phép toán logic
logical_and = (a > b) and (b < c)  # Và
logical_or = (a > c) or (b < c)  # Hoặc
logical_not = not (a == b)  # Không

# In kết quả phép toán logic
print("Và:", logical_and)
print("Hoặc:", logical_or)
print("Không:", logical_not)