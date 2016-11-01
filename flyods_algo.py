params = [int(i) for i in raw_input("Input lcg a,b,c, m and number of output values n e.g. 22 1 0 72 20\n").split()]

n = params[4]

a = params[0]
b = params[1]
c = params[2]
m = params[3]

l = [c]
l2 = [c]
begin = -1
period = 0
period_found = False



for i in range(n):
    l.append((a*l[-1]+b)%m)
    
    l2.append((a*l2[-1]+b)%m)
    l2[-1]=(a*l2[-1]+b)%m
    
    if begin == l[-1]:
        period_found = True
        break
        
    if l[-1]==l2[-1]:
        begin = l[-1]
        
    if begin!=-1:
        period+=1

    
print l
print l2
print period if period_found else n