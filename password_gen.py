import string
import random
import secrets
def main():
    print("valid features in this project:")
    print("1. view your passwords:")
    print("2. check strength of your password: ")
    print("3. save your password: ")
    val=int(input("enter your choice: "))
    match val:
        case 1:
            view()
        case 2:
            strength_check()
        case 3:
            social=input("enter your social id: ")
            print("generate password auto: ")
            savepass(social)
        case _:
            print("enter valid number")


def view():
    with open("pass.txt",'r') as file:
            for row in file:
                print(row)
def strength_check(password):
    length = len(password)
    digits = 0
    symbols = 0
    uppercase = 0
    for ch in password:
        if ch.isdigit():
            digits += 1
        elif ch.isupper():
            uppercase += 1
        elif not ch.isalnum():
            symbols += 1

    strength = length + digits + symbols + uppercase
    print("Strength Score:", strength)

def savepass(social):
    length=0
    while length<8:
        length=int(input("enter a valid length for password:"))
        if length<8:
            continue
        print("choose your password difficulty (1/2/3): ")
        print("enter 1 if you want easy only letters in password.")
        print("enter 2 if you want mid letters and digits in password.")
        print("enter 3 if you want hard letters , digits and special char also in password.")
        while True:
            val=int(input("enter your choose: "))
            if val>0 and val<=3:
                break

        char=""
        match val:
            case 1:
                char=string.ascii_letters
            case 2:
                char=string.ascii_letters+string.digits
            case 3:
                char=string.ascii_letters+string.digits+string.punctuation
            case _:
                print("invalid number.")
        password=""
        for i in range(length):
            password+=secrets.choice(char)
        print(password)
    with open("pass.txt",'a') as file:
            file.write(social+" :- "+password+"\n")
if __name__=="__main__":
    main()