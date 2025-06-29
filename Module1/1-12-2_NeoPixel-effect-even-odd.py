import machine
import neopixel
import time

# Cấu hình chân và số lượng LED
pin = machine.Pin(23)  # điều chỉnh theo chân bạn đang dùng
num_leds = 8
np = neopixel.NeoPixel(pin, num_leds)

# Danh sách màu (tùy chọn: có thể lặp hoặc thay đổi theo số LED)
colors = [
    (255, 0, 0),      # red
    (0, 255, 0),      # green
    (0, 0, 255),      # blue
    (255, 255, 0),    # yellow
    (0, 255, 255),    # cyan
    (255, 0, 255),    # magenta
    (255, 255, 255),  # white
    (255, 80, 0)      # orange
]

def turn_off_all():
    for i in range(num_leds):
        np[i] = (0, 0, 0)
    np.write()

while True:
    # Sáng các đèn CHẴN: 0, 2, 4, 6
    for i in range(0, num_leds, 2):  # bước nhảy là 2
        np[i] = colors[i]
    np.write()
    time.sleep(1)

    turn_off_all()
    time.sleep(1)

    # Sáng các đèn LẺ: 1, 3, 5, 7
    for i in range(1, num_leds, 2):
        np[i] = colors[i]
    np.write()
    time.sleep(1)

    turn_off_all()
    time.sleep(1)
