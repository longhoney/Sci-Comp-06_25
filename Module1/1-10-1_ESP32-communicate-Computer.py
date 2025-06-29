while True:
    # Tạo câu lệnh để nhập vào 
    user_input = input("Enter a command: ")
    # In đoạn lệnh bạn vừa nhập vào
    print("You entered:", user_input)
    
   
    if user_input.lower() == "hi":
        print("Hello!")
    elif user_input.lower() == "name":
        print("My name is ESP32.")
    else:
        print("Invalid input")

