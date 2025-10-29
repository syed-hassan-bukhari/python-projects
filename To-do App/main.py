def task():
    tasks = []

    total_task=int(input("enter how many task u want to add: "))
    for i in range(1,total_task+1):
        task_name=input(f"enter task {i}: ")
        tasks.append(task_name)


    print(f"todays task are\n{tasks}") 

    while True:
        operation=int(input("enter 1=add\n2-update\n3-delete\n4-view\n5-exit/stop"))
        
        if operation==1:
            add = input("enter the task you want to add: ")
            tasks.append(add)
            print(f"task {add} has beenm added succesfully")

        elif operation==2:
            update_val=input("enter the name of task you want to update:  ")
            if update_val in tasks:
                up = input("enter new task: ")
                ind = tasks.index(update_val)
                tasks[ind]=up
                print(f"updated task {up}")
        elif operation==3:
            del_val=input("enter tha task you want to delete: ")
            if del_val in tasks:
                ind =tasks.index(del_val)
                del tasks[ind]
                print(f"task {del_val} has been deleted ") 
        elif operation == 4:
            print(f"total task:{tasks}")
        elif operation == 5:
            print("closing the program.....")
            break               
        else:
            print("invalid input")
            

task()
