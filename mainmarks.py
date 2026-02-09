name = input("Enter student name: ")
marks = input("Enter marks:")
with open("marks1.txt","a")as file:
    file.write(f"{name}-{marks}\n")
    print("marks appended successfully!")