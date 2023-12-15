import customtkinter as ck 
import tkinter as tk
from string import ascii_uppercase
    
class Table_Object(ck.CTkFrame):
    def __init__(self, master, terms, cols, table_data):
        super().__init__(master)
        self.table_data = table_data
        
        for i in range(cols):
            label = ck.CTkLabel(self, text=ascii_uppercase[i])
            label.grid(row = 0, column = i, padx=5, pady=5)
        
        self.table_elements = []
        for row in range(terms):
            for col in range(cols):
                entry = ck.CTkEntry(self)
                entry.insert(0, self.table_data[row][col])
                entry.grid(row = row+1, column=col, padx=5, pady=5)
                self.table_elements.append(entry)
        
    def get_table_data():
        pass
                
        
 
    
class App(ck.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x900")
        
        self.table_data = [[0, 0], [0, 0], [0, 0], [0, 0]]
        # self.table = Table_Object(self, 4,2,self.table_data)
        # self.table.pack(padx = 20, pady = 20, fill=ck.BOTH, expand = True)
        
        self.add_table_button = ck.CTkButton(self, text="Add Table", command=self.tablebutton)
        self.add_table_button.pack(pady = 10)
        
        
    def tablebutton(self):
        # User enter cols we only need to know how many variables we have 
        dialog = ck.CTkInputDialog(text="Enter number of variables: ", title="Add table")
        cols= int(dialog.get_input())
        
        # assign amount of terms
        terms = 2**cols
        
        # print for debugging.
        print(terms,cols)
        
        # Make table and assign all initial values to zero for data. 
        self.table_data = 0
        for n in [cols, terms]:
            self.table_data = [self.table_data] * n
        print(self.table_data)
        for row in range(terms):
            for col in range(cols):
                self.table_data[row][col] = 0
                
        self.table = Table_Object(self,terms, cols, self.table_data)
        self.table.pack(padx = 20, pady = 20, fill=ck.BOTH, expand = True)
        
    def calculate_kmap(self):
        pass
    

if __name__ == "__main__":
    app = App()
    app.mainloop()