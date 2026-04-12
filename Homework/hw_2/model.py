class Model:
    def __init__(self) -> dict:
        self.elements = []
    
    def __len__(self): 
        return len(self.elements)
        
    def append(self, desc: str, status: bool):
        self.desc = desc
        self.status = status
        task = f"#. {self.desc}"
        self.elements.append({task : self.status})
        self.update_index()
        
    
    def remove(self, task: int):
        self.elements.remove(self.elements[task - 1])
        self.update_index()
        
    def update_index(self):
        for i, item in enumerate(self.elements):
            for key in item:
                new_index = key.replace(key[:1], str(i+ 1))
            self.elements[i] = {new_index: item[key]}
        return self.elements
    
    def get_task(self):
        return self.elements
    
    def complete(self, index: int):
        task = self.elements[index - 1]
        for item in task:
            task[item] = True
        return self.elements
            
    def incomplete(self, index: int,):
        task = self.elements[index - 1]
        for item in task:
            task[item] = False
        return self.elements