import numpy as np
from sympy import symbols, simplify_logic, SOPform
from string import ascii_uppercase

def get_boolean_expr(data):
    pass

# Returns tuple of table and minterms
def split_data_minterms(data: np.array):
    return data[:,:-1], data[:,-1]

# Returns minterms only
def get_minterms(data: np.array):
    return data[:,-1]

# Function takes unprocessed table and returns minterms for sympy SOP as integers
def get_minterms_for_SOP_integers(data: np.array):
    binary_val, minterms = split_data_minterms(data)
    minterms_sop = []
    for k,i in enumerate(minterms):
        if i == 1:
            minterms_sop.append(k)
    return minterms_sop

# Function takes unprocessed table and returns minterms for sympy SOP as binary values table
def get_minterms_for_SOP_bin(data: np.array):
    binary_val, minterms = split_data_minterms(data)
    minterms_sop = []
    for k,i in enumerate(minterms):
        print(i)
        if i == 1:
            minterms_sop.append(binary_val[k,:])
    return np.array(minterms_sop)
            

def sum_of_products(data):
    minterms_int = get_minterms_for_SOP_integers(data)
    
    expr = SOPform(minterms_int)

input_array = np.array([[0, 0, 0],
                        [0, 1, 1],
                        [1, 0, 0],
                        [1, 1, 1]])
print(get_minterms_for_SOP_integers(input_array))
