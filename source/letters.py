
class A(object):
    ''' A class will be converting from lower to uppercase. This is just for
    testing how Sphinx works, I am not that silly to do a class like this, man.
    '''

    def __init__(self, a_string):
        ''' Initialise with a string.

        :param a_string: a string that will be stored as internal attribute.
        :type a_string: string
        '''

        self.the_string = a_string

    def _veryPrivateMember(self, swearing_word='silly'):
        ''' Also can list private members like this one.

        :param swearing_word: swearing word to build the sentence with.
        :type swearing_word: string
        :return: the sentence with the swearing word.
        :rtype: ``string``
        '''

        string = "Hey {0}, I am doing nothing".format(swearing_word)
        print string
        return string

    def execute(self):
        ''' Run the action.

        :return: the uppercase version of the string.
        :rtype: ``string``
        '''
        
        result = self.the_string.upper()
        return result

class B(object):
    ''' A class will be multiplying a value.
    '''

    def __init__(self, value, multiplier):
        ''' Initialise with a value and a multiplier.

        :param value: number to multiply.
        :param multiplier: multiplier for the value.
        :type value: int
        :type multiplier: int
        '''

        self.value = value
        self.multiplier = multiplier

    def execute(self):
        ''' Run the action.

        :return: result of the multiplication
        :rtype: `int`
        '''

        result = self.multiplier * self.value
        return result 


class C(object):
    ''' A class will be concatenating strings.
    '''

    def __init__(self, string1, string2, join_character):
        ''' Initialise with a strings

        :param string1: first string.
        :param string2: second string.
        :param join_character: character that will join the strings.
        :type string1: string
        :type string2: string
        :type join_character: string
        '''

        self.s1 = string1
        self.s2 = string2
        self.sep = join_character

    def execute(self):
        ''' Run the action.

        :return: concatenation.
        :rtype: ``string``
        '''

        result = self.s1 + self.sep + self.s2
        return result 

