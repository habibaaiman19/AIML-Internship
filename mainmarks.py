name = input("Enter student name: ")
marks = input("Enter marks:")
with open("marks1.txt","a")as file:
    file.write(f"{name}-{marks}\n")
    print("marks appended successfully!")
    
filename = input("enter your file: ")
with open(filename,"r")as file:
    lines=file.readlines()
    print("number of lines:",len(lines))