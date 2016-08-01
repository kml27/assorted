from __future__ import division

import sys, math, os

print "Calculating Huffman for", sys.argv[1]
doc = open(sys.argv[1])
#print doc

wc = {chr(i):0 for i in range(255)}

source = doc.read()
total = len(source)
for c in source:
	wc[c]+=1

print source
	
#doc.seek()

#print wc
#print total
#for k in wc.keys():
#	print wc[k]/total	
	
values = [[k, v/total] for k,v in wc.iteritems() if v != 0]
codedict={k:0 for k,v in wc.iteritems() if v!=0}

print len(codedict.keys()), "unique symbols in source"

pnorm = zip(*values)[1]

#-dotproduct of p and log2 of p transpose
entropy = -sum(p * math.log(p, 2.0) for p in pnorm)

print "Source entropy (bits):", entropy

values.sort(key=lambda x: x[1])

for v in values:
	print "symbol", repr(v[0]), "probability", v[1] 

totalp = sum(pnorm)
	
print "as expected" if totalp == 1.0 else "warning","Probabilities sum to", "{0:.26f}".format(totalp)
	
iteration =0
	
while len(values)>1:
	#print iteration,"pass"
	values[0] = [values[0][0]+values[1][0], values[0][1]+values[1][1], [values[0], values[1]]]
	del values[1]
	#print values[0]
	values.sort(key=lambda x: x[1])
	iteration+=1
	
#print values

def define_code(tree, code, codedict):
	
	if len(tree[0]) < 2:
		print repr(tree[0]),"\t", code
		codedict[tree[0]]=code
		return
	
	branches = tree[2]
	
	#print 'left branch', branches[0]
	#print 'right branch', branches[1]
	
		
	#if both_leaf:
	#	return
	
	#print tree
	
	for i in range(2):
		#print i
		code+=str(i)
		#print code
		#print tree
		#print i, len(tree), len(tree[2])
		define_code(branches[i], code, codedict)
		code=code[:len(code)-1]

		
code=''
define_code(values[0], code, codedict)

#print codedict

print "size of original source:", len(source), "bytes"

codedsourcelist = [[v for k,v in codedict.iteritems() if k==c] for c in source]

codedsource = ""
for s in codedsourcelist:
	codedsource+=s[0]
	
cslen = len(codedsource)
print "size of coded source:", cslen/8, "bytes"

maxlength=entropy
for v in codedict.values():
	lenk=len(v)
	#print v, lenk
	if lenk > maxlength:
		maxlength = lenk

print "using", maxlength, "bits"
		
if maxlength%8 != 0:
	print "adjusting code to integer sized multiple of 8bits"
	maxlength =(maxlength-maxlength%8)/8 + 1

maxlength=int(maxlength)
filename = sys.argv[1]+".hcf"
codedfile = open(filename, "wb+")
#write length of keys when stored in file
print "warning, max length of key exceeds 255, byte expected for maxlength" if maxlength>255 else "code dictionary entries size:", maxlength, "bytes"
codedfile.write(chr(int(maxlength)))
#write number of keys (dictionary entries)
number_keys = len(codedict.keys())
print "number of keys exceeds 255, byte expected for number of keys" if number_keys>255 else number_keys, "keys"
codedfile.write(chr(number_keys))

#write all keys padded to maxlength
for k,v in codedict.iteritems():
	#print k,v
	#value matching this key
	codedfile.write(k)
	#original length of key in bits
	#print type(v)
	codedfile.write(chr(len(v)))
	#start the padded key value with the original bit string
	padv=v
	for i in range(int((maxlength*8)-len(v))):
		padv += "0"
	print len(padv)
	paddedkey=chr(int(padv,2))
	print padv, "written in dictionary", paddedkey
	
	codedfile.write(paddedkey)
		
#write len in bits of coded source, try to give the biggest value supported (UCS2 or UCS4)
codedfile.write(str(cslen).encode("UTF-8"))

print codedsource

#pad coded source with trailing zeros to write bytes
print "originally", cslen, "bits", (cslen%8), "trailing bit(s)"
for i in range(8-cslen%8):
	codedsource+="0"

print "padded to", codedsource
	
#write padded coded source to file
bytelength = int(len(codedsource)/8)
print "writing", bytelength, "bytes"
for i in range(bytelength):
	offset = i*8
	bits =codedsource[offset:offset+8]
	print i, bits
	codedfile.write(chr(int(bits,2)))
#close file
codedfile.close()

print "written file is", os.stat(filename).st_size

#print codedsource
