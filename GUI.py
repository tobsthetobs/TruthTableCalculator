import customtkinter as ck 
import tkinter as tk
from string import ascii_uppercase
from Logic import Logic
import numpy as np

# Table object used to handle entries of values into table    
class Table_Object(ck.CTkFrame):
    def __init__(self, master, terms, cols, table_data):
        super().__init__(master)
        self.table_data = table_data
        self.terms_i = terms
        self.cols_i = cols
        
        for i in range(cols):
            label = ck.CTkLabel(self, text=ascii_uppercase[i])
            label.grid(row = 0, column = i, padx=5, pady=5)
        

        # Generate the binary table
        binary_table = np.zeros((terms, cols-1), dtype=int)
        for i in range(terms):
            binary_table[i, :] = [int(x) for x in bin(i)[2:].zfill(cols-1)]
        
        col_max_index = max(range(cols))
        
        self.table_elements = []
        for row in range(terms):
            for col in range(cols):
                if col == col_max_index:
                    entry = ck.CTkEntry(self)
                    entry.insert(0, self.table_data[row][col])
                    entry.grid(row = row+1, column=col, padx=5, pady=5)
                    self.table_elements.append(entry)
                else:
                    entry = ck.CTkEntry(self)
                    entry.insert(0, binary_table[row,col])
                    entry.grid(row = row+1, column=col, padx=5, pady=5)
                    self.table_elements.append(entry)
    
    # Function to convert table from GUI into np.ndarray() of shape (terms, cols)    
    def get_table_data(self):
        data = np.zeros((self.terms_i, self.cols_i))
        row_i = 0
        col_i = 0
        
        # Iterate over table elements and add to data array
        for i, element in enumerate(self.table_elements):
            if i % self.cols_i == 0 and i != 0:
                row_i += 1    
            
            data[row_i, col_i] = element.get()
            col_i += 1
            
            if col_i == self.cols_i:
                col_i = 0
            
        print(data)
        return data
    
    def destroy_table(self):
        self.destroy()

class BoolExpResult(ck.CTkFrame):
    def __init__(self, master, res: str):
        super().__init__(master)
        label = ck.CTkLabel(self, text=res)
        label.pack(pady=5)
    
    def destroy_result(self):
        self.destroy()
 
    
class App(ck.CTk):
    def __init__(self):
        super().__init__()
        self.title("Truthtable Calculator")
        self.minsize(350,125)
        self.table = None
        self.result = BoolExpResult(self, "N/A")
        self.table_data = [[0, 0], [0, 0], [0, 0], [0, 0]]

        self.add_table_button = ck.CTkButton(self, text="Add Table", command=self.tablebutton)
        self.add_table_button.pack(pady = 10)
        
        self.get_table_data_button = ck.CTkButton(self, text="Get Table Data", command=self.get_data)
        self.get_table_data_button.pack(pady = 10)
        
        self.calculate_bool_expr_button = ck.CTkButton(self, text="Calculate Bool Expression", command=self.calculate_bool_expr)
        self.calculate_bool_expr_button.pack(pady = 10)
        
        self.pack_propagate(True)
        
    def tablebutton(self):
        if self.table != None:
            self.table.destroy_table()
        # User enter cols we only need to know how many variables we have 
        dialog = ck.CTkInputDialog(text="Enter number of variables: ", title="Add table")
        cols= int(dialog.get_input())
        
        # print for debugging.
        print("Number of variables entered: ", cols)
        
        # assign amount of terms and add one to cols for last column as 
        terms = 2**cols
        cols = cols + 1
        
        # print for debugging.
        print("Table of dims: ",terms,cols)
        
        # Make table and assign all initial values to zero for data. 
        self.table_data = 0
        for n in [cols, terms]:
            self.table_data = [self.table_data] * n

        for row in range(terms):
            for col in range(cols):
                self.table_data[row][col] = 0
                
        self.table = Table_Object(self,terms, cols, self.table_data)
        self.table.pack(padx = 20, pady = 20, fill=ck.BOTH, expand = True)
        
    def calculate_bool_expr(self):
        if self.table != None:
            self.result.destroy_result()
            text = "Boolean Expression for truth table is: " + str(Logic.get_boolean_expr(self.table.get_table_data()))
            self.result = BoolExpResult(self, text)
            self.result.pack(pady = 20)
        else:
            raise ValueError("No table data loaded")
            
    
    def get_data(self):
        if self.table != None:
            data = self.table.get_table_data()
            print("Data from table parsed")
            return data
        else:
            return 0

if __name__ == "__main__":
    app = App()
    app.mainloop()