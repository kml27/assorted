import math, sys, os

print "Reading", sys.argv[1], "to huffman decompress"

hcf = open(sys.argv[1])

bytes_per_dict_key = ord(hcf.read(1))
number_keys = ord(hcf.read(1))

print bytes_per_dict_key, "bytes used to store each dictionary key"

dict = {chr(c):[] for c in range(256)}

for i in range(number_keys):
    value = hcf.read(1)
    bitwidth = ord(hcf.read(1))
    format_specifier = "{0:0"+str(8)+"b}"
    #print format_specifier
    key = format_specifier.format(ord(hcf.read(bytes_per_dict_key)))
    #print key
    key = key[:bitwidth]
    print "value", value, "encoded with", bitwidth,"bits, using key", key
    dict[value] = [bitwidth, key]

min_dict = {k:v for k,v in dict.iteritems() if len(v)!=0}

print "minimal dictionary", min_dict

ucs_size = ord(hcf.read(1))
print "encoded on a system using", ucs_size, "byte unichr"
unicode = "u\"\u"
for i in range(ucs_size):
    unicode+="{0:02x}".format(ord(hcf.read(1)))
    
unicode+="\""
#print unicode
coded_length = eval("ord("+unicode+")")
print "the file was encoded using", coded_length, "bits"
length_to_read = coded_length/8 + 1 if coded_length % 8 != 0 else 0
print "the data was padded out to",length_to_read,"bytes"
codeddata = hcf.read(length_to_read)
hcf.close()

decoded_stream = ""

remaining_bits = coded_length

for c in codeddata:
    
    bits = remaining_bits if remaining_bits < 8 else 8
    bitstream_format = "{0:0"+ str(bits) +"b}"
    #print bitstream_format
    bitstream = bitstream_format.format(ord(c))[:bits]
    print bitstream
    while len(bitstream)>0:
        for k,v in min_dict.iteritems():
            #print bitstream[:v[0]], v[1], k
            if bitstream[:v[0]]==v[1]:
                decoded_stream+=k
                #print k
                bitstream = bitstream[v[0]:]
    
    remaining_bits -=8
    
print decoded_stream