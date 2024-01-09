import unittest
from Project_Logic import str_gate_parser

class test_str_parse(unittest.TestCase):
    
    def test_and_gate(self):
        expression_string = "x & y"
        res, _ , _ = str_gate_parser.count_logic_operators(expression_string)
        self.assertEqual(res, 1)
    
    def test_or_gate(self):
        expression_string = "x | y"
        res, _ , _ = str_gate_parser.count_logic_operators(expression_string)
        self.assertEqual(res, 1)
        
    def test_duplicate_operator_count(self):
        expression_string_3 = "(x & y) | (~z)"
        expression_string_4 = "(x & y) | (~z) | (y)"
        
        res_3, _ , _ = str_gate_parser.count_logic_operators(expression_string_3)
        res_4, _ , _ = str_gate_parser.count_logic_operators(expression_string_4)
        
        self.assertEqual(res_3, 3)
        self.assertEqual(res_4, 4)
        
    def test_bigger_expr(self):
        expression_string = "(x & y) | (~z) | (y) | (x & y & ~z)"
        res, _ , _ = str_gate_parser.count_logic_operators(expression_string)
        self.assertEqual(res, 8)
        
    def test_seperation_counts(self):
        expression_string = "(x & y) | (~z) | (y) | (x & y & ~z)"
        res = str_gate_parser.count_logic_operators(expression_string)
        self.assertEqual(res, (8,6,2))
