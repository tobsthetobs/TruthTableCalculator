import unittest
import numpy as np
from Logic import truth_table_logic

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
        
        result_OR = truth_table_logic.get_minterms_for_SOP_integers(input_OR)
        result_AND = truth_table_logic.get_minterms_for_SOP_integers(input_AND)
        self.assertEqual(result_OR, [1,2,3])
        self.assertEqual(result_AND, [3])
        
