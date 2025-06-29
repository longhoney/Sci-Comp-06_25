import machine
import dht
import time

# Initialize DHT11 sensor on GPIO5 (you can change the GPIO pin as needed)
sensor = dht.DHT11(machine.Pin(23))

while True:
    sensor.measure()
    temp = sensor.temperature()  # Read temperature in Celsius
    hum = sensor.humidity()      # Read humidity in percentage
        
    # Print the values
    #print("Temperature: {}°C".format(temp))
    #print("Humidity: {}%".format(hum))
    
    #print("Temperature:",temp,"°C")
    #print("Humidity: ",hum,"%")
    
    print("Temperature: {}°C | Humidity: {}%".format(temp,hum))
    time.sleep(1)

