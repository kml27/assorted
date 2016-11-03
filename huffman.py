from __future__ import division

import sys, math, os

print "Calculating Huffman for", sys.argv[1]
doc = open(sys.argv[1])
#print doc

#create a dictionary to store the frequency counts for each dictionary entry, in this implementation a single char is used,
#though in many implementations this is extended to multiple bytes, possibly finding the optimal settings from within a range, and/or//
#adaptively changing keys to maximize compression per block
wc = {chr(i):0 for i in range(255)}
#e.g. phrase_count = {chr(i)+chr(j):0 for i in range (255) for j in range(255)}

#read in the original source document to be analyzed for entropy
source = doc.read()
total = len(source)

#perform frequency count
for c in source:
	wc[c]+=1

#show the source document being analyzed
print source
	
#doc.seek()

#print wc
#print total
#for k in wc.keys():
#	print wc[k]/total	
	
    
#create a relative frequency list for each value that occurred, omitting values that did not occur at all in the source
values = [[k, v/total] for k,v in wc.iteritems() if v != 0]

#create a new dictionary that will store values of those keys (characters) that occur in the source
codedict={k:0 for k,v in wc.iteritems() if v!=0}

#output statistic of unique symbols identified
print len(codedict.keys()), "unique symbols in source"

#deinterleave keys (characters) and probabilities to probabilities normalized (relative frequencies)
pnorm = zip(*values)[1]

#calculate the minimum number of bits required to represent the amount of entropy identified in the source
#-dotproduct of p and log2 of p transpose
entropy = -sum(p * math.log(p, 2.0) for p in pnorm)

#output calculated entropy
print "Source entropy (bits):", entropy

#order the keys in descending order (greatest frequency to least frequency)
values.sort(key=lambda x: x[1])

#output calculated probabilities
for v in values:
	print "symbol", repr(v[0]), "probability", v[1] 

#verify the sum of the probabilities sums to 1
totalp = sum(pnorm)

#verbose output to provide notification of any ieee 754 precision rounding introduced error in probabilities 
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
#this file format allows for 1 byte to store the maximum length of a key, by def. the most frequently used values will have the shortest keys
print "warning, max length of key exceeds 255, byte expected for maxlength" if maxlength>255 else "code dictionary entries size:", maxlength, "bytes"
codedfile.write(chr(int(maxlength)))
#write number of keys (dictionary entries)
number_keys = len(codedict.keys())
#this file format allows for 1 byte to store the number of keys, it could be modified to store more
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

unicode_bit_length = int(round(math.log(sys.maxunicode, 2.0)))
print "this version of python was compiled to use", unicode_bit_length, "bits to represent unichr"
    
codedfile.write(chr(int(unicode_bit_length/8)))
    
#write len in bits of coded source, try to give the biggest value supported (UCS2 or UCS4)
coded_bit_length = unichr(int(str(cslen).encode("UTF-8")));

if len(coded_bit_length)<unicode_bit_length:
    codedfile.write(chr(0))

codedfile.write(coded_bit_length)

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

print "written file is", os.stat(filename).st_size, "bytes"

#print codedsource
