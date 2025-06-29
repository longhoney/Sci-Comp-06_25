'''
import machine
import time #không sử dụng lệnh "import Pin"

#Không sử dụng lệnh "from machine" nên phải gọi cụ thể trong lệnh
led = machine.Pin(13, machine.Pin.OUT) 


while True:
    led.value(1)
    time.sleep(2) 
    led.value(0) 
    time.sleep(2)
'''

from machine import Pin; import time #time là một thư viện thuộc hệ khác với Pin

led = Pin(13, Pin.OUT)

while True:
    led.on()
    time.sleep(2)
    #không tồn tại câu lệnh: "machine.time.sleep(2)"
    led.off()
    time.sleep(2)
