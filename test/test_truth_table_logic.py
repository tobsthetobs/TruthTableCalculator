import unittest
import numpy as np
from Project_Logic.truth_table_logic import *

class test_logic(unittest.TestCase):
    
    def test_get_minterms_ints(self):
        input_OR = np.array([[0, 0, 0],
                                [0, 1, 1],
                                [1, 0, 1],
                                [1, 1, 1]])
        input_AND = np.array([[0, 0, 0],
                                [0, 1, 0],
                                [1, 0, 0],
                                [1, 1, 1]])
        
        input_3var = np.array([[0, 0, 0, 0],
                                [0, 0, 1, 0.],
                                [0, 1, 0, 0],
                                [0, 1, 1, 1],
                                [1, 0, 0, 0],
                                [1, 0, 1, 1],
                                [1, 1, 0, 1],
                                [1, 1, 1, 1]])
        
        result_OR = get_minterms_for_SOP_integers(input_OR)
        result_AND = get_minterms_for_SOP_integers(input_AND)
        result_3var = get_minterms_for_SOP_integers(input_3var)
        self.assertEqual(result_OR, [1,2,3])
        self.assertEqual(result_AND, [3])
        self.assertEqual(result_3var, [3, 5, 6, 7])
        
    def test_sop(self):
        input = np.array([[0, 0, 0, 0],
                            [0, 0, 1, 0.],
                            [0, 1, 0, 0],
                            [0, 1, 1, 1],
                            [1, 0, 0, 0],
                            [1, 0, 1, 1],
                            [1, 1, 0, 0],
                            [1, 1, 1, 1]])
        result = str(sum_of_products(input))
        self.assertEqual(result, "(A & C) | (B & C)")
        
    def test_get_bool_expr(self):
        input = np.array([[0, 0, 0, 0],
                            [0, 0, 1, 0.],
                            [0, 1, 0, 0],
                            [0, 1, 1, 1],
                            [1, 0, 0, 0],
                            [1, 0, 1, 1],
                            [1, 1, 0, 0],
                            [1, 1, 1, 1]])
        result = str(get_boolean_expr(input))
        self.assertEqual(result, "C & (A | B)")