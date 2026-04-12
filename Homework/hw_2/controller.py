class Controller:
    def __init__(self, model : classmethod, view : classmethod):
        self.model = model
        self.view = view

    def select_menu(self):
        select = self.view.actions()
        if select == 1:
            return self.view.add_task()
        elif select == 2:
            return self.view.view_list()
        elif select == 3:
            return self.view.complete()
        elif select == 4:
            return self.view.incomplete()
        elif select == 5:
            return self.view.remove()
        elif select == 6:
            exit()
        else:
            self.view.actions()
            
    def list(self):
        return self.model.get_task()
    
    def ref_list(self):
        task = self.model.get_task()
        
        if len(task) == 0:
            print("Your list is empty!\n")
        else:
            for item in task:
                for desc in item.keys():
                    print(f"{desc:<15} : {item[desc]}")
    
    def add_menu(self, task, status):
        
        return self.model.append(task, status)
        
        
    def remove_menu(self):
            return self.view.task_action("would you like to remove", self.model.remove)
    
    def incomplete_menu(self):
        if len(self.model) == 0:
            self.ref_list()
            self.view.actions()
        return self.view.task_action("is incomplete", self.model.incomplete)
    
    def complete_menu(self):
        if len(self.model) == 0:
            self.ref_list()
            self.view.actions()
        return self.view.task_action("is complete", self.model.complete)
    
    




