import unittest

from ConversionFunctions.ConvFuncsSolved import ConvFuncsSolved


class ConvFuncsSolvedTester(unittest.TestCase):

    
    convFuncsSolved = None


    def setUp(self):

        id_text = self.id()
        id_desc = self.shortDescription()
        id_line = '-' * len(id_text)
        id_equl = '=' * len(id_text)

        print('')
        print(id_equl)
        print(id_text)
        if id_desc is not None:
            print(id_desc)
        print(id_line)
        print('')

        self.convFuncsSolved = ConvFuncsSolved()

        return


    def tearDown(self):
        # instantiated objects disposal
        unittest.TestCase.tearDown(self)
        return

        
    def test_absolute_value(self):
        
        value = -4
        result = self.convFuncsSolved.absolute_value(value)
        self.assertIsInstance(result, type(value))
        self.assertEqual(result, abs(value))
        
        value = None
        result = self.convFuncsSolved.absolute_value(value)
        self.assertIsInstance(result, TypeError)
        
        value = ''
        result = self.convFuncsSolved.absolute_value(value)
        self.assertIsInstance(result, TypeError)
        
        value = 'x'
        result = self.convFuncsSolved.absolute_value(value)
        self.assertIsInstance(result, TypeError)
    
    def test_all_elements_are_true(self):
        
        iterable = [True, True, True]
        result = self.convFuncsSolved.all_elements_are_true(iterable)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, True)
        
        iterable = [False, True, True]
        result = self.convFuncsSolved.all_elements_are_true(iterable)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, False)
        
        iterable = None
        result = self.convFuncsSolved.all_elements_are_true(iterable)
        self.assertIsInstance(result, TypeError)
        
        iterable = ''
        result = self.convFuncsSolved.all_elements_are_true(iterable)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, True)
        
        iterable = 'x'
        result = self.convFuncsSolved.all_elements_are_true(iterable)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, True)
   
    def test_any_element_is_true(self):
        
        iterable = [False, False, True]
        result = self.convFuncsSolved.any_element_is_true(iterable)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, True)
        
        iterable = [False, False, False]
        result = self.convFuncsSolved.any_element_is_true(iterable)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, False)
        
        iterable = None
        result = self.convFuncsSolved.any_element_is_true(iterable)
        self.assertIsInstance(result, TypeError)
        
        iterable = ''
        result = self.convFuncsSolved.any_element_is_true(iterable)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, False)
        
        iterable = 'x'
        result = self.convFuncsSolved.any_element_is_true(iterable)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, True)
    
    def test_floating_point_value(self):
        
        value = -4.6
        result = self.convFuncsSolved.floating_point_value(value)
        self.assertIsInstance(result, float)
        self.assertEqual(result, float(value))
        
        value = None
        result = self.convFuncsSolved.absolute_value(value)
        self.assertIsInstance(result, TypeError)
        
        value = ''
        result = self.convFuncsSolved.absolute_value(value)
        self.assertIsInstance(result, TypeError)
        
        value = 'x'
        result = self.convFuncsSolved.absolute_value(value)
        self.assertIsInstance(result, TypeError)
     
    def test_integer_value(self):
        
        value = -4.6
        result = self.convFuncsSolved.integer_value(value)
        self.assertIsInstance(result, int)
        self.assertEqual(result, int(value))
        
        value = None
        result = self.convFuncsSolved.absolute_value(value)
        self.assertIsInstance(result, TypeError)
        
        value = ''
        result = self.convFuncsSolved.absolute_value(value)
        self.assertIsInstance(result, TypeError)
        
        value = 'x'
        result = self.convFuncsSolved.absolute_value(value)
        self.assertIsInstance(result, TypeError)
    
    def test_largest_element_of_iterable(self):
        
        iterable = [1, 2, 3]
        result = self.convFuncsSolved.largest_element_of_iterable(iterable)
        self.assertIsInstance(result, int)
        self.assertEqual(result, max(iterable))
        
        iterable = None
        result = self.convFuncsSolved.largest_element_of_iterable(iterable)
        self.assertIsInstance(result, TypeError)
        
        iterable = ''
        result = self.convFuncsSolved.largest_element_of_iterable(iterable)
        self.assertIsInstance(result, ValueError)
        
        iterable = 'x'
        result = self.convFuncsSolved.largest_element_of_iterable(iterable)
        self.assertIsInstance(result, str)
        self.assertEqual(result, max(iterable))
    
    def test_largest_item_of_arguments(self):
        
        result = self.convFuncsSolved.largest_item_of_arguments(1, 2, 3)
        self.assertIsInstance(result, int)
        self.assertEqual(result, max(1, 2, 3))
        
        result = self.convFuncsSolved.largest_item_of_arguments(None, None)
        self.assertIsInstance(result, TypeError)
        
        result = self.convFuncsSolved.largest_item_of_arguments('', '')
        self.assertIsInstance(result, str)
        
        result = self.convFuncsSolved.largest_item_of_arguments('x', 'y')
        self.assertIsInstance(result, str)
        self.assertEqual(result, max('x', 'y'))
    
    def test_length_of_value(self):
        
        value = 'This should be 34 characters long!'
        result = self.convFuncsSolved.length_of_value(value)
        self.assertIsInstance(result, int)
        self.assertEqual(result, len(value))
        
        value = None
        result = self.convFuncsSolved.length_of_value(value)
        self.assertIsInstance(result, TypeError)
        
        value = ''
        result = self.convFuncsSolved.length_of_value(value)
        self.assertIsInstance(result, int)
        self.assertEqual(result, len(value))
        
        value = [1, 2, 3]
        result = self.convFuncsSolved.length_of_value(value)
        self.assertIsInstance(result, int)
        self.assertEqual(result, len(value))
        
        value = []
        result = self.convFuncsSolved.length_of_value(value)
        self.assertIsInstance(result, int)
        self.assertEqual(result, len(value))
    
    def test_smallest_element_of_iterable(self):
        
        iterable = [1, 2, 3]
        result = self.convFuncsSolved.smallest_element_of_iterable(iterable)
        self.assertIsInstance(result, int)
        self.assertEqual(result, min(iterable))
        
        iterable = None
        result = self.convFuncsSolved.smallest_element_of_iterable(iterable)
        self.assertIsInstance(result, TypeError)
        
        iterable = ''
        result = self.convFuncsSolved.smallest_element_of_iterable(iterable)
        self.assertIsInstance(result, ValueError)
        
        iterable = 'x'
        result = self.convFuncsSolved.smallest_element_of_iterable(iterable)
        self.assertIsInstance(result, str)
        self.assertEqual(result, min(iterable))
    
    def test_smallest_item_of_arguments(self):
        
        result = self.convFuncsSolved.smallest_item_of_arguments(1, 2, 3)
        self.assertIsInstance(result, int)
        self.assertEqual(result, min(1, 2, 3))
        
        result = self.convFuncsSolved.smallest_item_of_arguments(None, None)
        self.assertIsInstance(result, TypeError)
        
        result = self.convFuncsSolved.smallest_item_of_arguments('', '')
        self.assertIsInstance(result, str)
        
        result = self.convFuncsSolved.smallest_item_of_arguments('x', 'y')
        self.assertIsInstance(result, str)
        self.assertEqual(result, min('x', 'y'))
     
    def test_sort_list_of_items(self):
        
        iterable = [1, 2, 3]
        result = self.convFuncsSolved.sort_list_of_items(iterable)
        self.assertIsInstance(result, list)
        self.assertEqual(result, sorted(iterable))
        
        iterable = [1, 2, 3]
        result = self.convFuncsSolved.sort_list_of_items(iterable, reverse=True)
        self.assertIsInstance(result, list)
        self.assertEqual(result, sorted(iterable, reverse=True))
        
        iterable = None
        result = self.convFuncsSolved.sort_list_of_items(iterable)
        self.assertIsInstance(result, TypeError)
        
        iterable = ''
        result = self.convFuncsSolved.sort_list_of_items(iterable)
        self.assertIsInstance(result, list)
        self.assertEqual(result, sorted(iterable))
        
        iterable = 'X'
        result = self.convFuncsSolved.sort_list_of_items(iterable, key=str.lower)
        self.assertIsInstance(result, list)
        self.assertEqual(result, sorted(iterable, key=str.lower))

    
if __name__ == '__main__':
    unittest.main(verbosity=2)