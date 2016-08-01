import sys

#print __file__

filename = sys.argv[0]
if sys.argv[0] == __file__:
	filename =sys.argv[1]

print filename
	
f = open(filename)

buf = f.read()

count=0

for c in buf:
	i = ord(c)
	sys.stdout.write(c+" "+format(i, "#02x")+"\t")
	count+=1
	if count ==5:
		count =0
		sys.stdout.write("\n")