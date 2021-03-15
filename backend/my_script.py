from epp import display
import sys

def displays(*args):
    return args

a = displays(sys.argv)
my_data = a[0][1]

display(my_data)

sys.stdout.flush()
