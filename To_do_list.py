import os

def show_tasks(tasks):
    if not tasks:
         print("No tasks found. ")
    else:
         for i,tasks in enumerate(tasks,1):
             print(f"{i}. {tasks}")
def add_tasks(tasks, new_tasks):                   
    tasks.append(new_tasks)
    print("Tasks Added succussfully.")

def update_tasks(tasks, index, updated_tasks):
     if 1 <= index <=len(tasks):
          tasks[index -1] =updated_tasks
          print("Tasks update succussfully")
     else:
          print("invalid Tasks Index.")    

def delete_tasks(tasks, index):
       if 1 <= index <=len(tasks):
          delete_tasks = tasks.pop(index-1)
          print(f"Tasks '{delete_tasks}' deleted successfully ")
       else:
          print("invalid Tasks Index.")            

def save_task_to_file(file_path, tasks): 
    with open(file_path, "w" ) as file:
         for tasks in tasks:
              file.write(f"{tasks}\n")





def load_tasks_from_file(file_path):
    tasks = []
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            task= file.read().spiltlines()
    return  task
          


def main():
    file_path = "todo_list.txt"
    tasks = load_tasks_from_file(file_path)
    while True:
     print("\n==== To-do list ====")
     print("1. Show tasks")
     print("2. Add tasks")
     print("3. Update tasks")
     print("4. Delete tasks")
     print("5. Save and Exit")
     choice = input("Enter your choice (1-5): ")
     if choice=="1":
          show_tasks(tasks)
     elif choice=="2":
            new_tasks = input("Enter the tasks to add: ")
            add_tasks(tasks, new_tasks) 
     elif choice=="3":
            Index = int(input("Enter the tasks index to update: "))
            update_tasks = input("Enter the update tasks: ")
            update_tasks(tasks, Index, update_tasks)
     elif choice=="4":
            Index = int(input("Enter the tasks index to delete: "))
            delete_tasks(tasks, Index)
     elif choice=="5":
            save_task_to_file(file_path, tasks)
            print("Tasks saved. Exiting..")   
            break
     else:
         print("invalid choice. please try again. ") 
                

  

if __name__:=  "__main__":
    main()
