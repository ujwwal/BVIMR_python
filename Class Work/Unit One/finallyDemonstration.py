try:
    file = open('example.txt', 'r')
    content = file.read()
    print(content)  
except FileNotFoundError:
    print("Error, the file was not found")
finally:
    if file is not None:
        file.close()