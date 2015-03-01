# A class to implement a value/quantity that consists of a number and a unit

class Value(object):

    # Constructor
    def __init__(self, *args):

        # The lead is the first argument
        lead = args[0]

        # Check the type of lead
        if type(lead) == type(self):
            # Copy constructor
            self.data = dict(lead.data)
            self.coefficient = lead.coefficient
        elif type(lead) == int:
            self.from_constant(lead)
        elif type(lead) == str:
            self.from_symbol(*args)
        elif type(lead) == dict:
            self.from_dictionary(*args)
        else:
            self.from_lists(*args)


    # lead int -> constant
    def from_constant(self, constant):
        self.coefficient = constant
        self.data = {}

    # lead str -> symbol
    def from_symbol(self, symbol, coefficient=1, power=1):
        self.coefficient = coefficient
        self.data = {symbol: power}

    # lead dict -> data
    def from_dictionary(self, data, coefficient=1):
        self.data = data
        self.coefficient = coefficient

    # lead list -> data
    def from_lists(self, symbols=[], powers=[], coefficient=1):
        self.coefficient = coefficient
        self.data = {symbol: exponent for symbol, exponent
                     in zip(symbols, powers)}

    # Multiply
    def multiply(self, other):
        pass

    # Add (Check unit compatibility)
    def add(self, other):
        pass

    # Equality
    def equality(self, other):
        pass

    # __str__
    def __str__(self):
        pass

