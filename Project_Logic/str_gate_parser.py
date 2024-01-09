from sympy import parse_expr
from sympy.logic.boolalg import Or, And, Not

# returns a tuple (total, and_ors, nots), this looks horrible though
def count_logic_operators(str_expr):
    logic_operators = {"&": 0, "|": 0}
    not_operators = {"~": 0}
    
    for char in str_expr:
        if char in logic_operators:
            logic_operators[char] += 1
        elif char in not_operators:
            not_operators[char] += 1
    return (sum(logic_operators.values()) + sum(not_operators.values()), sum(logic_operators.values()), sum(not_operators.values())) 
print(count_logic_operators("(x & y) | (~z) | (y) | (x & y & ~z)"))