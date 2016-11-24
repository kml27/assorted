#binarize
import sys
inval = int(raw_input(""))
binarystr=""

orig=inval
negative = inval < 0

if negative:
    inval *= -1
    
binarystr=""
bstrlen = 0

while inval != 0: 
    print(str(inval)+"%2=="+str(inval%2)+"(prefix "+ str(inval%2) +")")
    binarystr+=str(inval%2)
    
    
    bstrlen = len(binarystr)
    
    for i in range(8-bstrlen):
        sys.stdout.write("x")
    for i in range(bstrlen):
        sys.stdout.write(binarystr[(bstrlen-1)-i])
    
    print "\n"
    
    print(str(inval)+"/2=="+str(inval/2))
    inval = inval/2
    
print("remaining bits are 0")
    
bstrlen = len(binarystr)
for i in range(8-bstrlen):
    sys.stdout.write("0")
    binarystr+="0"
for i in range(bstrlen):
    sys.stdout.write(binarystr[(bstrlen-1)-i])

        
        
if negative:
    print("\n\nconverting to negative (2's complement)")
    negstr = ""
    print("\ninvert")

    for i in range(8):
        negstr += "0" if binarystr[7-i]=="1" else "1"
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
            
    for i in range(8):      
        sys.stdout.write(incstr[7-i])
    