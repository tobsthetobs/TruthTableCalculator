# super class used for gates.
class Gate:
    def __init__(self, inputs):
        # Sanitize initialzations of class variables to be a list of booleans. 
        # if no list is given check if inputs is a singular bool, cast to a list and 
        if not isinstance(inputs, list) and isinstance(inputs,bool):
            inputs = [inputs]
        elif not isinstance(inputs, list) and not isinstance(inputs,bool): 
            raise ValueError("Inputs must be a list or bool, given type", type(inputs))
        
        if not all(isinstance(val,bool) for val in inputs):
            raise ValueError("Values in inputs must be bool")

        self.inputs = inputs
        self.output = False

    def print_inputs(self):
        print(self.inputs)
        
    def print_output(self):
        print(self.output)
    
    def set_input(self, input):
        self.inputs = input
        self.logic()
        
    def get_output(self):
        self.logic()
        return self.output
        
# implement AND gate logic
class ANDGate(Gate):
    def __init__(self,inputs):
        super().__init__(inputs)
        ANDGate.logic(self)
        
    # Run logic function to calculate output of ANDGate
    def logic(self):
        if all(val for val in self.inputs) == True:
            self.output = True
        else: 
            self.output = False
    
# implement NAND gate logic
class NANDGate(Gate):
    def __init__(self,inputs):
        super().__init__(inputs)
        NANDGate.logic(self)
        
    # Run logic function to calculate output of NANDGate
    def logic(self):
        if not all(val for val in self.inputs) == True:
            self.output = True
        else: 
            self.output = False

# implement OR gate logic
class ORGate(Gate):
    def __init__(self,inputs):
        super().__init__(inputs)
        ORGate.logic(self)
        
    # Run logic function to calculate output of ORGate
    def logic(self):
        if any(val for val in self.inputs) == True:
            self.output = True
        else: 
            self.output = False

# implement NOR gate logic
class NORGate(Gate):
    def __init__(self,inputs):
        super().__init__(inputs)
        NORGate.logic(self)
        
    # Run logic function to calculate output of ORGate
    def logic(self):
        if not any(val for val in self.inputs) == True:
            self.output = True
        else: 
            self.output = False

x = ORGate(inputs=[False, False])
x.print_inputs()
x.set_input([True,False])
x.print_output()

