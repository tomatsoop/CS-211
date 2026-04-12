"""Sabrina Zhang - CS 211 
   MVC Task Application : Classes and Subclasses
   References : 
    while True : https://www.toolsqa.com/python/python-while-loop/
    https://www.w3schools.com/python/python_try_except.asp """


if __name__ == "__main__":
    from model import Model
    from controller import Controller
    from view import View
    
    model = Model()
    controller = Controller(model, None)
    view = View(controller)
    controller.view = view
    while True:
        controller.select_menu()