from intents import get_result
import sys

def displays(*args):
    return args

a = displays(sys.argv)
my_data = a[0][1]

get_result(my_data)

sys.stdout.flush()