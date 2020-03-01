import unittest
from static_array import Array
from dynamic_array import DynamicArray
from array_methods import *
from associative_array import AssArray


class TestDsa(unittest.TestCase):

    def test_static_array(self):
        # Creating an array object for testing
        arr = Array(4, 3, 4, 7)
        # testing the length function
        self.assertEqual(arr.arr_len(), 4)
        # testing the values method
        self.assertEqual(arr.values, [4, 3, 4, 7])
        # testing that our places within an array are initialised to None
        self.assertEqual(arr.elem, [4, 3, 4, 7, None, None, None, None, None, None])
        # Testing the set method
        arr.arr_set(2, 1)
        self.assertEqual(arr.values, [4, 3, 1, 7])
        self.assertEqual(arr.elem, [4, 3, 1, 7, None, None, None, None, None, None])
        # testing the get method
        self.assertEqual(arr.arr_get(1), 3)
        # testing a couple of edge cases and variability
        arr = Array(4)
        self.assertEqual(arr.arr_len(), 1)
        self.assertEqual(arr.values, [4])
        self.assertEqual(arr.elem, [4, None, None, None, None, None, None, None, None, None])
        arr = Array()
        self.assertEqual(arr.arr_len(), 0)
        self.assertEqual(arr.values, [])
        self.assertEqual(arr.elem, [None, None, None, None, None, None, None, None, None, None])
        # # testing for Out of bound IndexError exceptions
        with self.assertRaises(IndexError):
            arr.arr_set(1, 1)
        with self.assertRaises(IndexError):
            arr.arr_get(6)
        # testing correct data type input
        with self.assertRaises(ValueError):
            arr = Array('3', 4)
        with self.assertRaises(ValueError):
            arr = Array(3, 4, 5, '6', 7)

    def test_dynamic_array(self):
        # To test that our new array object is actually dynamic:
        # We test with an input size less than our predefined size of 10
        arr = DynamicArray(3, 5, 6, 7)
        self.assertEqual(arr.size, 10)
        # We also test with an input size greater than our predefined size and if the size size of our array has doubled
        arr = DynamicArray(9, 4, 6, 3, 4, 5, 1, 4, 6, 8, 4, 8, 9, 0, 4, 7)
        self.assertEqual(arr.size, 20)
        # Testing the delete method
        arr.arr_del()
        self.assertEqual(arr.values, [9, 4, 6, 3, 4, 5, 1, 4, 6, 8, 4, 8, 9, 0, 4])

    def test_array_methods(self):
        arr = DynamicArray(3, 9, 1, 4)
        self.assertEqual(arr.values, [3, 9, 1, 4])
        # testing the contains function
        self.assertEqual(contains(arr, 1), True)
        # testing the reverse function
        self.assertEqual(reverse(arr), [4, 1, 9, 3])
        # testing the insert function
        self.assertEqual(insert(arr, 0, 1), [4, 0, 1, 9, 3])

    def test_associative_list(self):
        a_arr = AssArray('name', 'paul')
        # testing the instance
        self.assertEqual(a_arr.as_array, [('name', 'paul')])
        # testing the insert method
        a_arr.insert('age', 230)
        self.assertEqual(a_arr.as_array, [('name', 'paul'), ('age', 230)])
        #  testing the lookup method
        self.assertEqual(a_arr.lookup('name'), 'paul')
        self.assertEqual(a_arr.lookup('age'), 230)
        # testing the remove method
        a_arr.remove('name')
        self.assertEqual(a_arr.as_array, [('age', 230)])
        # testing the modify method
        a_arr.modify('age', 23)
        self.assertEqual(a_arr.as_array, [('age', 23)])
        a_arr.insert('Nationality', 'Nigerian')
        # testing the lookup method
        self.assertEqual(a_arr.lookup('Nationality'), 'Nigerian')
        # testing exceptions for the different methods
        with self.assertRaises(KeyError):
            a_arr.lookup('School')
        with self.assertRaises(KeyError):
            a_arr.remove('car')
        with self.assertRaises(KeyError):
            a_arr.modify('blood-group', '+O')


if __name__ == '__main__':
    unittest.main()



