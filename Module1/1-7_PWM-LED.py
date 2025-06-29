from machine import Pin, PWM
import time #thư viện của các hàm thời gian
#Cài đặt chân GPIO 13 làm output cho LED với PWM
led = PWM(Pin(13), freq=5000)

#Thay đổi độ sáng đèn LED giả lập tín hiệu analog
led.duty(100) #Độ sáng ở mức 100/1023 (~10%)
time.sleep(1) #dừng chương trình 1 giây
led.duty(300) #Độ sáng ở mức 300/1023
time.sleep(1)
led.duty(1000)  
time.sleep(1)
led.duty(500)
time.sleep(1)
led.duty(100)
time.sleep(1)
led.duty(0)
time.sleep(1) #tắt đèn