from machine import Pin;  import time, utime #time, utime là hai thư viện thuộc hệ khác với Pin

led = Pin(13, Pin.OUT)

while True:
    # Lấy giá trị thời gian từ hệ thống (đơn vị là giây)
    current_time = utime.time()
    
    # Kiểm tra điều kiện: thời gian là số chẵn
    if (current_time % 2) == 0:
        led.on()  # nếu đúng (là số chẵn), bật đèn
    else:
        led.off()  # nếu sai, tắt đèn
    