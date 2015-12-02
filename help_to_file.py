import sys
import pydoc

#print("first cmd line element " + sys.argv[0])
#print("second cmd line parameter " + sys.argv[1])

#import sys.argv[1]

#name = sys.argv[1] 

def help_to_file(name):
    f = open(name+".txt", 'w')
    sys.stdout = f
    pydoc.help(name)
    f.close()
    sys.stdout = sys.__stdout__
    return
	
if not "python" in sys.argv[0]:
    help_to_file(sys.argv[1])
else:
    help_to_file(sys.argv[2])