# Importing the predefined Array class
from static_array import Array

"""
IMPLEMENTATION OF THE DYNAMIC ARRAY ABSTRACT DATA TYPE:
This inherits the methods and properties of the Static array 
Implementation Decisions:
1. The size of the array is predefined to 10 and and increased continuously increases
if the length of the specified elements is greater than the size. 
"""


# Dynamic array inherits from Static Array class
class DynamicArray(Array):

    # The constructor takes in a variable length of input elements
    def __init__(self, *initial_values):
        # Initialising the parent constructor
        super().__init__(*initial_values)
        # calling the create arr method to adjust the size
        self.create_arr()
        # setting the elements to an empty array and re-validating it
        self.elem = []
        self.validate()
        # updating the values to reflect these changes
        self.val_update()

    def create_arr(self):
        # Continuously increasing the size until the size accommodates the element length
        while len(self.initial_values) >= self.size:
            self.size *= 2

    # A method for adding a value to the end of an array
    def arr_add(self, elem):
        index = self.arr_len()
        # Calling the double size method to create more space for us in case
        # There is not enough space to add a new element
        #self.double_size()
        self.arr_set(index, elem)

    # A method for del the last element in an array
    def arr_del(self):
        index = self.arr_len() - 1
        self.elem = self.elem[0:index]
        # Updating the values with update method defined in the parent class
        self.val_update()

    # A method to increase the size for methods the that alter the length of the array
    def double_size(self):
        # Continuously increasing the size until the size accommodates the element length
        while len(self.elem) >= self.size:
            self.size *= 2
        pass

    # Overriding the validate method in the parent class that prevents us from making
    # An array with a len smaller than the size
    def validate(self):
        count = 0
        for i in range(self.size):
            if count < len(self.initial_values):
                self.elem.append(self.initial_values[i])
            else:
                self.elem.append(None)
            count += 1
        self.values = self.elem[0:self.arr_len()]


