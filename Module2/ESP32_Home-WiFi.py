import network
import time

# Thông tin mạng Wi-Fi, cần xóa thông tin này khi public ra khỏi máy tính
SSID = '' #Tên wifi
PASSWORD = '' #mật khẩu

# Hàm kết nối Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)  # Chế độ Station
    wlan.active(True)  # Bật Wi-Fi
    wlan.connect(SSID, PASSWORD)  # Kết nối Wi-Fi

    # Chờ đến khi kết nối thành công
    while not wlan.isconnected():
        print("Đang kết nối đến Wi-Fi...")
        time.sleep(1)
    print("Đã kết nối Wi-Fi!")
    
    print("Thông tin IP: ")
    print(wlan.ifconfig())  # In thông tin IP

# Kết nối Wi-Fi
connect_wifi()