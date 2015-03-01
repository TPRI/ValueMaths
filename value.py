# A class to implement a value/quantity that consists of a number and a unit
import os
import yaml


class Value(object):

    # Constructor
    def __init__(self, *args):

        # The lead is the first argument
        lead = args[0]

        # Check the type of lead
        if type(lead) == type(self):
            # Copy constructor
            self.data = dict(lead.data)  # TODO check behavior
            self.coefficient = lead.coefficient
        elif type(lead) == int:
            self.from_constant(lead)
        elif type(lead) == str:
            self.from_symbol(*args)
        elif type(lead) == dict:
            self.from_dictionary(*args)
        else:
            self.from_lists(*args)

        self.to_base_units()

    def to_base_units(self):
        # load the unit definitions
        units = yaml.load(open(os.path.join(os.path.dirname(__file__), 'unit_defs.yml')))

        # Initialise the base units
        self.base_units = {'m': 0, 'kg': 0, 's': 0, 'A': 0, 'k': 0, 'cd': 0, 'mol': 0}

        # Convert symbol,exponent in data into base units
        for symbol, exponent in self.data.iteritems():
            new_unit = units[symbol]
            new_base = new_unit['base']
            new_num = new_unit['num']

            # Multiply coefficient by unit number^exponent
            self.coefficient *= pow(new_num, exponent)

            # Add new_base to base_units
            for key, value in new_base.items():
                self.base_units[key] += new_base[key]*exponent


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
    def multiply(self, *others):

        result_data = dict(self.data)
        result_coeff = self.coefficient

        # Convert arguments to Terms first if they are
        # constants or integers
        others = map(Value, others)
        for another in others:
            for symbol, exponent in another.data.iteritems():
                if symbol in result_data:
                    result_data[symbol] += another.data[symbol]
                else:
                    result_data[symbol] = another.data[symbol]
            result_coeff *= another.coefficient
        return Value(result_data, result_coeff)


    def __mul__(self, other):
        return self.multiply(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    # Add (Check unit compatibility)
    def add(self, other):
        pass

    # Equality
    def equality(self, other):
        return (self.base_units == other.base_units) and\
               (self.coefficient == other.coefficient)

    def __eq__(self, other):
        return self.equality(other)

    # Return a string
    def __str__(self):
        def unit_string(unit, power):
            if power == 1:
                return unit
            elif power == 0:
                return''
            else:
                return unit + '^' + str(power)

        unit_strings = [unit_string(unit, power)
                          for unit, power in self.base_units.iteritems()]

        prod = ' '.join(unit_strings)

        if not prod:
            # if empty string (i.e. no units)
            return str(self.coefficient)
        else:
            return str(self.coefficient) + '' + prod

