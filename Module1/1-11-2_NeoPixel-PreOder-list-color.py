import machine
import neopixel
import time

# Cấu hình số LED và chân kết nối
num_leds = 8
pin = 23  # Chân D11 kết nối với dải NeoPixel

# Khởi tạo dải NeoPixel
np = neopixel.NeoPixel(machine.Pin(pin), num_leds)

# Danh sách màu RGB
colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "white": (255, 255, 255),
    "orange": (255, 80, 0)
}

# Danh sách LED với màu tương ứng
led_colors = ["red", "green", "blue", "yellow", "cyan", "magenta", "white", "orange"]

# Gán màu cho từng LED
for i in range(num_leds):
    np[i] = colors[led_colors[i]]
    # Hiển thị màu sắc trên dải LED
    np.write()
# Giữ nguyên màu trong x giây trước khi tắt
time.sleep(3)

# Tắt toàn bộ LED
for i in range(num_leds):
    np[i] = (0, 0, 0)
    np.write()
