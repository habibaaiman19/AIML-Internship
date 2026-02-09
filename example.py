try:
    file = open("sample.txt","r")
    print(file.read())
except Exception as e:
    print(f"error: {e}")
finally:
    file.close()       