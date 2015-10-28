
class A(object):
    ''' A class will be converting from lower to uppercase. This is just for
    testing how Sphinx works, I am not that silly to do a class like this, man.

    '''

    def __init__(self, a_string):
        ''' Initialise with a string.

        Args:
            a_string (str): a string that will be stored as internal attribute.

        '''

        self.the_string = a_string

    def _veryPrivateMember(self, swearing_word='silly'):
        ''' Also can list private members like this one.

        Args:
            swearing_word (string): swearing word to build the sentence with.
        
        Returns:
            string: the sentence with the swearing word.

        '''

        string = "Hey {0}, I am doing nothing".format(swearing_word)
        print string
        return string

    def execute(self):
        ''' Run the action.

        Returns:
            string: the uppercase version of the string.

        '''
        
        result = self.the_string.upper()
        return result

class B(object):
    ''' A class will be multiplying a value.

    '''

    def __init__(self, value, multiplier):
        ''' Initialise with a value and a multiplier.

        Args:
            value (int): number to multiply.
            multiplier (int): multiplier for the value.

        '''

        self.value = value
        self.multiplier = multiplier

    def execute(self):
        ''' Run the action.

        Returns:
            int: result of the multiplication.

        '''

        result = self.multiplier * self.value
        return result 


class C(object):
    ''' A class will be concatenating strings.
    '''

    def __init__(self, string1, string2, join_character):
        ''' Initialise with a strings

        Args:
            string1 (string): first string.
            string2 (string): second string.
            joing_character (string): join separator.

        '''

        self.s1 = string1
        self.s2 = string2
        self.sep = join_character

    def execute(self):
        ''' Run the action.

        Returns:
            string: concatenation.
            
        '''

        result = self.s1 + self.sep + self.s2
        return result 

