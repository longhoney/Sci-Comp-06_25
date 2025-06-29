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

# Hiệu ứng chạy màu
while True:
    for i in range(num_leds):
        # Tắt tất cả LED trước khi cập nhật
        for j in range(num_leds):
            np[j] = (0, 0, 0)

        # Bật LED hiện tại với màu tương ứng
        np[i] = colors[led_colors[i]]
        np.write()

        # Chờ một khoảng thời gian ngắn trước khi chuyển LED tiếp theo
        time.sleep(0.2)

