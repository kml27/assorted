#LCG
from collections import Counter
import time

#period determined by modulus and multiplier, full modulus period if:
#Hull-Dobell Theorem
#modulus and increment are coprime(share no factor besides 1)
#multiplier - 1 is divisible by all prime factors of modulus
#multiplier - 1 is divisible by 4 if modulus is divisible by 4

#52
modulus = 104
#multiplier is always less than modulus (period of 52 desired, to meet)
multiplier = 53
#set increment to 0 for MCG
increment = 1
seed = int(time.time()*10000)

def lcg():
    next_prn = seed

    while True:
        next_prn = (next_prn*multiplier+increment)%modulus
        yield next_prn

output = []
prng = lcg()

print seed

for i in range(modulus):
    out = prng.next()
    print i, out
    output.append(out)

c= Counter(output)
print "len of unique count:",len(c),"\n",c