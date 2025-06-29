from machine import UART
import time

# Initialize UART with default pins (TX=GPIO1, RX=GPIO3)
u_art = UART(1, baudrate=115200, tx=1, rx=3)

def check_input():
        if u_art.any():  # Check if there's any data available to read
            received_data = u_art.read().decode('utf-8').strip()  # Read and decode the data
            
            if received_data.lower() == "hello":
                u_art.write("hi\n")
            if received_data.lower() == "name":
                u_art.write("my name is ESP32\n")
            if received_data.lower() == "language":
                u_art.write("my language is Python\n")
            if received_data.lower() == "bye":
                u_art.write("goodbye!\n")

        time.sleep(0.01)  # Small delay to prevent overloading the CPU

while True: #vòng lặp vô tận này khiến máy treo
    check_input() #bấm reset để thực hiện lại