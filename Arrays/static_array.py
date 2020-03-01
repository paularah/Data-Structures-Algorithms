"""
A Static Array Abstract Data Type Implementation
Implementations Decisions:
This mimics the implementation of python's list except that they are static
The size of the array is predefined to be of 10
This ADT uses zero based indexing
"""


class Array:
    def __init__(self,  *initial_value):
        """
         The class constructor taking a finite value for the size while the initial input the list
         list are theoritically infinite as long they are less than the specified size.
        """
        self.initial_values = initial_value
        self.size = 10
        # An empty list that would hold our array elements after validation
        self.elem = []
        self.values = []
        self.type_check()
        self.validate()

    def type_check(self):
        # Type checking for size input to be strictly and integer
        if type(self.size) != int:
            raise ValueError

        # Type checking to ensure that initial instantiation elements are all integers
        # N/B: The resulting values from the variable arguments in the constructor is a tuple
        for i in self.initial_values:
            if type(i) != int:
                raise ValueError
        pass

    def validate(self):
        # adding our initial values straight to a elem list if the size and length are all
        # specified input corresponds
        if len(self.initial_values) == self.size:
            for i in self.initial_values:
                self.elem.append(i)

        # Initialising the other empty spaces in memory to None if the length of the specified values
        # is less than the size
        elif len(self.initial_values) < self.size:
            count = 0
            for i in range(self.size):
                if count < len(self.initial_values):
                    self.elem.append(self.initial_values[i])
                else:
                    self.elem.append(None)
                count += 1
            self.values = self.elem[0:self.arr_len()]

            # Raising a values if the length of the specified elements at instantiation is more
            # than the size
        else:
            raise ValueError

    # Calculating the length of the length of the actual values that have been initialised within  the alloted size
    def arr_len(self):
        length = 0
        for i in self.elem:
            if i is None:
                pass
            else:
                length += 1
        return length

    # A method to set a value to array at a particular index
    def arr_set(self, index, val):
        if index <= (self.arr_len()):
            self.elem[index] = val
            self.val_update()
            # Raising an index error if the index is greater the length of the elements
        else:
            raise IndexError

    def val_update(self):
        self.values = self.elem[0:self.arr_len()]

    # A method to get a value by it index
    def arr_get(self, index):
        if index < self.arr_len():
            return self.values[index]
        else:
            # Raises an in error if the value is greater the length of the elements
            raise IndexError

    # Overriding the string magic method to allow us print out our array object.
    def __str__(self):
        return str(self.values)

