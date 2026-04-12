
class View:
    def __init__(self, controller: classmethod):
       self.controller  = controller 
        
    def actions(self):
        print("\n--- To-Do List Menu ---\n",
              "1. Add Task\n",
              "2. View Tasks\n",
              "3. Mark Task as Complete\n",
              "4. Mark Task as Incomplete\n",
              "5. Remove Task\n",
              "6. Exit\n")
    
        while True:
            try:
                user = int(input("What would you like to do (Select Number for task): "))
                if 1 <= user <= 6:
                    return user
                else: 
                    print("\nPlease Choose a value between 1 - 6!")
            except ValueError:
                    print("\nPlease Choose a value between 1 - 6!")
                
    def add_task(self):
        task = input("What is your task: ")
        if task == "":
            print("Please enter a Task!")
            task = input("What is your task: ")
        status = (input("What is the status (True or False): ")).lower()
        while status not in("true", "false"):
            status = (input("What is the status (True or False): ")).lower()
        status = True if status == "true" else False
        print("\nTask added successfully.")
        return self.controller.add_menu(task, status)
    
    def task_action(self, desc: str, func: function):
        while True:
            try:
                index = int(input(f"\nWhich task {desc} - \n"
                                "(Select task number): "))
        
                if len(self.controller.list())  >= index:
                    func(index)
                    break
                else: 
                    print("\nInvalid Index: Please choose a task from the list!")
            except ValueError:
                print("\nInvalid Index: Please choose a task from the list!")
    
    def view_list(self):
        print(f"{"-" * 8}Task{"-" * 8}")
        return f"{self.controller.ref_list()}\n"
                    
    def complete(self):
        self.view_list()
        print()
        return self.controller.complete_menu()
    
    def incomplete(self):
        self.view_list()
        return self.controller.incomplete_menu()
        
    def remove(self):
        self.view_list()
        return self.controller.remove_menu()
   
                
   