import sys
import csv
def main():
    print("choose your number:(1/2/3/4)")
    print("1 for add your task:")
    print("2 for delete your task:")
    print("3 for modify your task:")
    print("4 for view your tasks:")
    number=int(input("enter your number:"))
    match number:
        case 1:
            add(2)
        case 2:
            delete([])
        case 3:
            modify(4)
        case 4:
            view(2)
        case _:
            print("enter valid number")
def view(task):
    with open("todo.csv",'r') as file:
        for i in file:
            print(i)

def modify(task):
    print(task)

def add(task):
    with open("todo.csv","a",newline="") as file:
        write=csv.DictWriter(file,fieldnames=["name","age"])
        write.writerow({
            "name" : sys.argv[1],
            "age" : sys.argv[2]
            })

def delete(task):
    str=input("enter deleted name: ")
    with open("todo.csv",'r') as file:
        reader=csv.DictReader(file)
        for row in reader:
            print(row)
            if row['name']!=str:
                task.append(row)
    with open("todo.csv",'w',newline="") as file:
        writer=csv.DictWriter(file,fieldnames=["name","age"])
        writer.writeheader()
        writer.writerows(task)

if __name__=="__main__":
    main()