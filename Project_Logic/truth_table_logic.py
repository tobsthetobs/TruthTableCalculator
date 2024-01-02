import numpy as np
from sympy import symbols, simplify_logic, SOPform
from string import ascii_uppercase

def get_boolean_expr(data: np.array):
    return simplify_logic(sum_of_products(data))

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
        if i == 1:
            minterms_sop.append(binary_val[k,:])
    return np.array(minterms_sop)
            
# Function used to calculate boolean expression
def sum_of_products(data: np.array):
    vars = []
    # Iterate over range of rows - 1 to get A,B,C etc for each var we need for SOPform function
    for i in range(len(data[0,:])-1):
        vars.append(symbols(ascii_uppercase[i]))
    minterms_int = get_minterms_for_SOP_integers(data)
    
    print("Vars: ", vars, "\n")
    print("Minterms: ", minterms_int, "\n")
    return SOPform(vars,minterms_int)