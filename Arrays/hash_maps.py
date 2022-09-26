class HashMap:

    def __init__(self, size=43):
        self.hash_table = [None] * size
        self.size = size 

    def gen_hash(self, key):
        SALT = 47
        hashresults = 0 
        for char in key:
            hashresults = (hashresults * SALT + ord(char) - 96) % self.size
        return hashresults

    def get(self, key):
        key_hash = self.gen_hash(key)
        if self.hash_table[key_hash] == None:
            raise KeyError
        for values in self.hash_table[key_hash]:
            if values[0] == key:
                return values

    def set(self, key, value):
        key_hash = self.gen_hash(key)

        if self.hash_table[key_hash] == None:
           self.hash_table[key_hash] = []
        self.hash_table[key_hash].append([key, value]) 


    def keys(self):
        keys_array = []
        for values in self.hash_table:
            for pairs in values:
                keys_array.append(pairs[0])
        return keys_array

    def values(self):
        values_array = []
        for values in self.hash_table:
            for pairs in values:
                values_array.append(pairs[1])
        return values_array
        