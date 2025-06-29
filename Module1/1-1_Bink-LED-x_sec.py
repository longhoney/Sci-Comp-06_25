'''
from machine import Pin; import time #time là một thư viện thuộc hệ khác với Pin

#Cài đặt chân GPIO 13 làm output
led = Pin(13, Pin.OUT) #Đây là cú pháp của MicroPython

led.on()  # Bật LED
time.sleep(2) #dừng chương trình 1 giây
led.off() # Tắt LED
#time.sleep(1)
'''
import machine; import time #time là một thư viện thuộc hệ khác với Pin

led = machine.Pin(13, machine.Pin.OUT)

led.value(1)
time.sleep(2)
led.value(0)
    
'''
Thử tính năng ghi chú như đoạn văn.
Với ngôn ngữ C, ghi chú như đoạn văn sẽ bắt đầu với /* và kết thúc với */
'''
