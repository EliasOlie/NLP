from Natural_Language import NLP
import sys

def displays(*args):
    return args

a = displays(sys.argv)
my_data = a[0][1]

res = NLP(my_data)
print(res.process)

sys.stdout.flush()