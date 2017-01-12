inval = raw_input()

dec=0

#start with -128 if bit 7 is set
print(inval[0]+" at bit 7, starting with -128*"+inval[0])
dec-=pow(2,7) if inval[0]=="1" else 0

for i in range(7):
    bitval = pow(2, 6-i)
    print(inval[i+1]+" at bit " + str(6-i) + ", adding "+str(bitval) + "*"+str(inval[6-i]))
    dec+= bitval*(int(inval[i+1]))
 

print(str(dec))
