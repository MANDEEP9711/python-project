import sys
import csv
from colorama import Fore,Style
from datetime import date, datetime
def main():
    status_mark()
    print("choose your number:(1/2/3/4)")
    print("1 for add your task:")
    print("2 for delete your task:")
    print("3 for modify your task:")
    print("4 for view your tasks:")
    print("5 for dash board:")
    number=int(input("enter your number:"))
    match number:
        case 1:
            add()
        case 2:
            delete()
        case 3:
            mark_task=input("which task you want modify: ")
            status_mark(mark_task)
        case 4:
            view()
        case 5:
            statistics_dashboard()
        case _:
            print("enter valid number")
def statistics_dashboard():
    comp=0
    pend=0
    fail=0
    with open("todo.csv",'r') as file:
        reader=csv.DictReader(file)
        for row in reader:
            if row["status"]=="complete":
                comp+=1
            elif row["status"]=="pending":
                pend+=1
            else:
                fail+=1
    print("completed tasks: ",comp)
    print("pending tasks: ",pend)
    print("failed tasks: ",fail)
def view():
    with open("todo.csv",'r') as file:
        reader=csv.DictReader(file)
        for i in reader:
            if i["status"]=="complete":
                color=Fore.GREEN
            elif i["status"]=="fail":
                color=Fore.RED
            else:
                color=Fore.YELLOW
            print(color+str(i)+Style.RESET_ALL)


def status_mark(mark_task=None):
    fil=[]
    with open("todo.csv",'r') as file:
        reader=csv.DictReader(file)
        for row in reader:
            if datetime.strptime(row["Duedate"], "%Y-%m-%d").date() < date.today():
                row["status"] = "fail"
            elif row["task"] == mark_task:
                row["status"]="complete"
            fil.append(row)
    with open("todo.csv",'w',newline="") as file:
        writer=csv.DictWriter(file,fieldnames=["task","status","Duedate"])
        writer.writeheader()
        writer.writerows(fil)

def add():
    task = input("Enter task: ")
    status = input("Enter status: ")
    due = input("Enter due date (YYYY-MM-DD): ")
    with open("todo.csv","a",newline="") as file:
        write=csv.DictWriter(file,fieldnames=["task","status","Duedate"])
        write.writerow({
            "task" : task,
            "status" : status,
            "Duedate": due
            })

def delete():
    update_task=[]
    task_name=input("enter which task you want delete: ")
    with open("todo.csv",'r') as file:
        reader=csv.DictReader(file)
        for row in reader:
            if row['task']!=task_name:
                update_task.append(row)
    with open("todo.csv",'w',newline="") as file:
        writer=csv.DictWriter(file,fieldnames=["task","status","Duedate"])
        writer.writeheader()
        writer.writerows(update_task)
if __name__=="__main__":
    main()