"""
Associative List Abstract Data Type Implementation
"""


class AssArray:
    def __init__(self, key, value):
        self.as_array = []
        self.insert(key, value)

    # Insert method
    def insert(self, key, value):
        for pair in self.as_array:
            if pair[0] == key:
                raise KeyError
        return self.as_array.append((key, value))

    # remove method
    def remove(self, key):
        for pair in self.as_array:
            if pair[0] == key:
                return self.as_array.remove(pair)
        raise KeyError

    # modify method
    def modify(self, key, value):
        for pair in self.as_array:
            if pair[0] == key:
                self.as_array.remove(pair)
                return self.as_array.append((key, value))
        raise KeyError

    # lookup method
    def lookup(self, key):
        for pair in self.as_array:
            if pair[0] == key:
                return pair[1]
        raise KeyError

    # Overriding the string magic method to allow us print our associative array object
    def __str__(self):
        return str(self.as_array)


