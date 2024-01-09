import customtkinter as ck 
import tkinter as tk
from string import ascii_uppercase
from Project_Logic import truth_table_logic, str_gate_parser
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
            label.grid(row = 0, column = i, padx=25, pady=5)
        

        # Generate the binary table
        binary_table = np.zeros((terms, cols-1), dtype=int)
        for i in range(terms):
            binary_table[i, :] = [int(x) for x in bin(i)[2:].zfill(cols-1)]
        
        col_max_index = max(range(cols))
        
        self.table_elements = []
        for row in range(terms):
            for col in range(cols):
                if col == col_max_index:
                    # make a entry for each row in the last column, each of these entries validates inputs on keystroke changes 
                    # then pass the value of the text if change is allowed to the function is_input_valid which returns either 
                    # True or False if input is allowed.
                    entry = ck.CTkEntry(self, validate="key", validatecommand=(self.register(self.is_input_valid), "%P"))
                    entry.insert(0, self.table_data[row][col])
                    entry.grid(row = row+1, column=col, padx=5, pady=5)
                    self.table_elements.append(entry)
                # Table elements that correspond to non - maxterms dont need to be entries :
                else:
                    label = ck.CTkLabel(self, text=str(binary_table[row,col]))
                    label.grid(row = row+1, column=col, padx=25, pady=5)
                    self.table_elements.append(label)

                
                """  Code below is used to make all entries of the table a CTkEntry, 
                     this however makes the entire table writeable and does not make sense to do so as Logic is not implemented to account for this.    
                else:
                    entry = ck.CTkEntry(self)
                    entry.insert(0, binary_table[row,col])
                    entry.grid(row = row+1, column=col, padx=5, pady=5)
                    self.table_elements.append(entry)            
                """
    # Function to convert table from GUI into np.ndarray() of shape (terms, cols)    
    def get_table_data(self):
        data = np.zeros((self.terms_i, self.cols_i))
        row_i = 0
        col_i = 0
        allowed_chars = set('xXzZ')
        
        # Iterate over table elements and add to data array
        for i, element in enumerate(self.table_elements):
            if i % self.cols_i == 0 and i != 0:
                row_i += 1    
            
            if isinstance(element, ck.CTkEntry):
                element_i = element.get()
                try:
                    data[row_i, col_i] = element_i
                except ValueError:
                    if all(char in allowed_chars for char in element_i):
                        data[row_i,col_i] = -1  
            else:
                data[row_i, col_i] = int(element.cget("text"))
            col_i += 1
            
            if col_i == self.cols_i:
                col_i = 0
            
        return data
    
    # Destroy table used if table already exists and a new table is called to be made.
    def destroy_table(self):
        self.destroy()
     
    # Function used to validate entry values in table to only 0,1,x,X,z,Z   
    def is_input_valid(self, input):
        allowed_inputs = set('01xXzZ')
        if len(input) <= 1:
            if type(input) == str:
                return all(char in allowed_inputs for char in input)
            else:
                return False
        else:
            return False
            

class BoolExpResult(ck.CTkFrame):
    def __init__(self, master, res: str, count: str):
        super().__init__(master)
        label = ck.CTkLabel(self, text=res)
        label.pack(pady=5)
        gate_label = ck.CTkLabel(self, text=count)
        gate_label.pack(pady=5)
    
    def destroy_result(self):
        self.destroy()
 
    
class App(ck.CTk):
    def __init__(self):
        super().__init__()
        self.title("Truthtable Calculator")
        self.minsize(350,125)
        self.table = None
        self.result = BoolExpResult(self, "N/A", "N/A")
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
        # print("Number of variables entered: ", cols)
        
        # assign amount of terms and add one to cols for last column as 
        terms = 2**cols
        cols = cols + 1
        
        # print for debugging.
        # print("Table of dims: ",terms,cols)
        
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
            expr = str(truth_table_logic.get_boolean_expr(self.table.get_table_data()))
            total, and_or, nots = str_gate_parser.count_logic_operators(expr)
            text = "Boolean Expression for truth table is: " + expr
            count = "Function can be implemented using: " + str(and_or) + " logic gates and " + str(nots) + " inverters."
            self.result = BoolExpResult(self, text, count)
            self.result.pack(pady = 20)
        else:
            raise ValueError("No table data loaded")
            
    
    def get_data(self):
        if self.table != None:
            data = self.table.get_table_data()
            print("Data from table parsed", data)
            return data
        else:
            return 0

if __name__ == "__main__":
    app = App()
    app.mainloop()