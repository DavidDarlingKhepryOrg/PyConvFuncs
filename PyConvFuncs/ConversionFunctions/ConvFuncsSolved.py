'''
Created on Jul 12, 2016

@author: David Darling

'''

class ConvFuncsSolved(object):
    '''
    Python Conversion Functions
    '''


    def __init__(self):
        pass
        
        
    def absolute_value(self,
                       value):
        '''
        return the absolute value of the parameter value
        or TypeError or ValueError if it is invalid
        '''
        
        try:
            result = abs(value)
        except TypeError as err:
            result = err
        except ValueError as err:
            result = err
        
        return result

    
    def all_elements_are_true(self,
                              iterable):
        '''
        return True if all elements of the parameter iterable are true or the iterable is empty
        or TypeError or ValueError if it is invalid
        '''
        
        try:
            result = all(iterable)
        except TypeError as err:
            result = err
        except ValueError as err:
            result = err
        
        return result
 
    
    def any_element_is_true(self,
                            iterable):
        '''
        return True if any element of the parameter iterable is true
        or False if the iterable is empty
        or TypeError or ValueError if it is invalid
        '''
        
        try:
            result = any(iterable)
        except TypeError as err:
            result = err
        except ValueError as err:
            result = err
        
        return result
    
    
    def floating_point_value(self,
                             value):
        '''
        return a floating point number of the parameter value
        or TypeError or ValueError if it is invalid
        '''
        
        try:
            result = float(value)
        except TypeError as err:
            result = err
        except ValueError as err:
            result = err
        
        return result
    
    
    def int_to_hex_value(self,
                         value):
        '''
        return a hexadecimal string of the parameter value
        or TypeError or ValueError if it is invalid
        '''
        
        try:
            result = hex(value)
        except TypeError as err:
            result = err
        except ValueError as err:
            result = err
            
        return result
    
    def integer_value(self,
                      value):
        '''
        return an integer number of the parameter value
        or TypeError or ValueError if it is invalid
        '''
        
        try:
            result = int(value)
        except TypeError as err:
            result = err
        except ValueError as err:
            result = err
        
        return result
 
    
    def largest_element_of_iterable(self,
                                    iterable):
        '''
        return largest item of an iterable
        or TypeError or ValueError if it is invalid
        '''
        
        try:
            result = max(iterable)
        except TypeError as err:
            result = err
        except ValueError as err:
            result = err
        
        return result
 
    
    def largest_item_of_arguments(self,
                                   arg1,
                                   arg2,
                                   *args):
        '''
        return largest item of two or more arguments
        or TypeError or ValueError if it is invalid
        '''
        
        try:
            result = max(arg1, arg2, *args)
        except TypeError as err:
            result = err
        except ValueError as err:
            result = err
        
        return result
    
    
    def length_of_value(self,
                        value):
        '''
        return an integer number of the length of the parameter value
        or TypeError or ValueError if it is invalid
        '''
        
        try:
            result = len(value)
        except TypeError as err:
            result = err
        except ValueError as err:
            result = err
        
        return result
 
    
    def smallest_element_of_iterable(self,
                                     iterable):
        '''
        return smallest item of an iterable
        or TypeError or ValueError if it is invalid
        '''
        
        try:
            result = min(iterable)
        except TypeError as err:
            result = err
        except ValueError as err:
            result = err
        
        return result
 
    
    def smallest_item_of_arguments(self,
                                   arg1,
                                   arg2,
                                   *args):
        '''
        return smallest item of two or more arguments
        or TypeError or ValueError if it is invalid
        '''
        
        try:
            result = min(arg1, arg2, *args)
        except TypeError as err:
            result = err
        except ValueError as err:
            result = err
        
        return result
    
    
    def sort_list_of_items(self,
                           iterable,
                           key=None,
                           reverse=False):
        '''
        return a sorted iterable of the iterable parameter
        or TypeError or ValueError if it is invalid
        '''
        
        try:
            result = sorted(iterable, key=key, reverse=reverse)
        except TypeError as err:
            result = err
        except ValueError as err:
            result = err
        
        return result
    
       