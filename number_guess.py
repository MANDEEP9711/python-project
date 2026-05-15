import random
while True:
    print('enter your diff level')
    print(" enter 1 if you want difficult level")
    print(" enter 2 if you want mid level")
    print(" enter 3 if you want easy level")
    number=int(input("enter 1/2/3 for level: "))
    if number==1:
        turns=5
    elif number==2:
        turns=7
    elif number==3:
        turns=10
    else:
        print("enter valid number")
        continue
    num=random.randint(0,100)
    print("random number: ",num)
    x=0
    while True:
        try:
            x+=1
            guess_num=int(input("Enter your guess number: "))
            if guess_num==num:
                print(f"you guess your number in {x} turn")
                break
            elif guess_num<num:
                print("your guess number is too low enter again")
            else:
                print("your guess number is too high enter again")
            if x==turns:
                print("you not guess your number in 10 turn play again")
                break
        except ValueError:
            print("enter valid number")
    ch=input("enter y if you want play again or n for quit: ")
    if ch!='y' and ch!='Y':
        break
        