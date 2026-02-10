with open("friends.txt","w")as f:
    for i in range(3):
        name=input(f"Enter friend name{i+1}: ")
        f.write(name+"\n")
        print("friend names saved to friends.txt")

search_name = input("enter name to search: ")
with open("friends")