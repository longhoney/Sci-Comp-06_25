import machine
import dht
import time

# Initialize DHT11 sensor on GPIO5 (you can change the GPIO pin as needed)
sensor = dht.DHT11(machine.Pin(23))

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

    
while True:
    sensor.measure()  # Đọc giá trị từ cảm biến DHT
    temp_celsius = sensor.temperature()
    temp_fahrenheit = celsius_to_fahrenheit(temp_celsius) # đổi giá trị nhiệt độ từ C sang F 
    print("Temperature in Celsius:",temp_celsius,"°C")
    #print("Temperature in Fahrenheit:",temp_fahrenheit,"°F")
    print("Temperature in Fahrenheit: {}°F".format(temp_fahrenheit))
    time.sleep(1)


