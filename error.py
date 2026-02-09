try:
    file = open("config.txt","r")
    print(file.read())
except FileNotFoundError:
    print("oops !that file doesn't exit yet")      