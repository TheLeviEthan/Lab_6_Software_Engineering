

"""
Author: Ethan Ruddell
Created 10-25-23
"""

new_password = ""


def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode(pwd):
    global new_password
    new_password = ""
    for num in pwd:
        val = int(num)
        val += 3
        if val >= 10:
            val -= 10
        new_password += str(val)


def decode(pwd):
    pass


while __name__ == "__main__":
    print_menu()
    selection = int(input("Please enter an option: "))
    if selection == 1:
        password = input("Please enter your password to encode: ")
        encode(password)
        print("Your password has been encoded and stored!")
    elif selection == 2:
        print(f"The encoded password is {new_password}, and the original password is {decode(new_password)}")
    elif selection == 3:
        break
