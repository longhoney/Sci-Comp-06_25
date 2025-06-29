with open('script.py', 'r') as file:
	code = file.read()  # Read the contents of the file
exec(code)  