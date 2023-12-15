import customtkinter as ck 
import tkinter as tk
from string import ascii_uppercase
    
class Table_Object(ck.CTkFrame):
    def __init__(self, master, shape, table_data):
        super().__init__(master)
        self.table_data = table_data
        
        for row in shape[0]:
            for cols in shape[1]:
                
        
 
    
class App(ck.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x900")
        self.table_dims = [0,0]
        self.table = None
        
        self.add_table_button = ck.CTkButton(self, text="Add Table", command=self.tablebutton)
        self.add_table_button.grid(row = 0)
        
        
    def tablebutton(self):
        # User enter cols we only need to know how many variables we have 
        dialog = ck.CTkInputDialog(text="Enter number of variables: ", title="Add table")
        cols= int(dialog.get_input())
        
        # assign amount of terms
        terms = 2**cols
        
        # print for debugging.
        print(terms,cols)
        self.
    
    def update_table(self):
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()