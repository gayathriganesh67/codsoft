def Addtask():
  task=input("Please enter a task:")
  tasks.append(task)
  print("Tasks are added to the list")
def Listtask():
  if tasks==[]:
    print("There are no tasks currently")
  else:
    print("Current Tasks:")
    for i in range(len(tasks)):
      print(str(i+1)+" "+tasks[i])
def Deletetask():
  Listtasks()
  Tasktodelete=int(input("enter the task to be deleted"))
  if Tasktodelete>=0 and Tasktodelete<len(tasks):
    tasks.pop(Tasktodelete)
    print("Task is deleted")
  else:
    print("task not found")
def main():
  tasks=[]
  print("Welcome to the To Do List app")
  while True:
    print("Please select one of the following choices:")
    print("-------------------------------------------")
    print("1. Add a new Task")
    print("2.Delete a task")
    print("3.List taks")
    print("4.Exit")
choice=input("Enter your choice:")
if choice=="1":
  Addtask()
elif choice=="2":
  Deletetask()
elif choice=="3":
  Listtask()
elif choice== "4":
  print("Thank you for using the app")
else:
  print("Invalid input,please try agan")
print("Thank You")