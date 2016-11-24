import sys

inval = raw_input("")
binarystr=inval
bstrlen = 8

print("\n\nconverting to negative (2's complement)")
negstr = ""
print("\ninvert")

for i in range(8):
    negstr += "0" if binarystr[i]=="1" else "1"
print(negstr)

incstr = ""

print("inc")

carry = 1

for i in range(8):
    if negstr[7-i]=="0" and carry:
        incstr += "1"
        carry=0
    elif negstr[7-i]=="1" and carry:
        incstr +="0"
        carry = 1
    else:
        incstr+=negstr[7-i]
    
dec =0    
for i in range(8):      
    sys.stdout.write(incstr[7-i])
    
print("\n")

#start with -128 if bit 7 is set
print(incstr[7]+" at bit 7, starting with -128")
dec-=pow(2,7) if incstr[7]=="1" else 0

for i in range(7):
    bitval = pow(2, 6-i)
    print(incstr[6-i]+" at bit " + str(6-i) + ", adding "+str(bitval) + "*"+str(incstr[6-i]))
    dec+= bitval*(int(incstr[6-i]))
 

print(str(dec))
