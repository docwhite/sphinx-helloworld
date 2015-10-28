from letters import A
from letters import B
from letters import C

def do_something_crazy(s1, s2, s3, val, multiplier):
    ''' Runs a crazy test with classes.
    '''
    a = A(s1)
    b = B(val, multiplier)
    c = C(s1, s2, s3)
    res =  str(a.execute()) + str(b.execute()) + str(c.execute())
    return res



if __name__ == '__main__':
    r = do_something_crazy('tete', 'tonto', '-', 6, 5)
    print r