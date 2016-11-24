# msb means most significant bit
# lsb means least significant bit
#  1 8       23 ... widths
# +-+-------+-----------------------+
# |s| e     |                     f |
# +-+-------+-----------------------+
#  msb lsb msb lsb ... order


sign_exponent = 0
exponent = 0
#mantissa
fraction = 0

single_exponent_bitwidth = 8
single_mantissa_bitwidth = 23

double_exponent_bitwidth = 11
double_mantissa_bitwidth = 52

single_bias = 127
double_bias = 1203

print("total single bits: "+str(1+single_exponent_bitwidth+single_mantissa_bitwidth))

print("total double bits: "+str(1+double_exponent_bitwidth+double_mantissa_bitwidth))


#special exponent/fractions
zero_exponent = "0"*single_exponent_bitwidth
special_values_exponent = "1"*single_exponent_bitwidth
inf_mantissa = "0"*single_mantissa_bitwidth
NaN_mantissa = "0"*(single_mantissa_bitwidth-1)+"1"
#Not a Number is any value other than 0 after the "special fraction exponent" 
#NaN = ""
sz_inf="Inf"
sz_NaN="NaN"

#special exponent for inf and nan, mantissa matters, required/default mantissa
special_str = {sz_inf:[special_values_exponent, True, inf_mantissa], sz_NaN:[special_values_exponent, False, NaN_mantissa]}

sz_bits = ""
sz_exponent = ""
sz_fraction = ""

sz_float = raw_input("enter single precision float decimal: ")

sz_float = sz_float.strip().lower()
sz_bits = "1" if sz_float[0]=="-" else "0"

find_bits = True

for sym in special_str.keys():
    print("testing for " + sym)
    if sym.lower() in sz_float:
        print("found "+sym)
        sz_exponent = special_str[sym][0]
        sz_fraction = special_str[sym][2]
        find_bits = False

if find_bits:
    point_index = sz_float.find(".", 1)

    sz_integer_part = sz_float[1:]
    sz_fractional_part = "0"
    
    if point_index != -1:
        sz_integer_part = sz_float[1:point_index+1]
        sz_fractional_part = sz_float[point_index+1:]

    print ("parsed "+ sz_integer_part+"."+sz_fractional_part)
    
    integer_part = int(sz_integer_part)
    fractional_part = int(sz_fractional_part)
    if integer_part == 0 and fractional_part == 0:
        sz_exponent = zero_exponent
        sz_fraction = inf_mantissa
    else:
        integer_part -= 1;
        sz_integer_part = str(integer_part)    

sz_bits += sz_exponent + sz_fraction

print sz_bits

sz = raw_input("enter single precision float bits: ")
if len(sz):
    sz_bits = sz

sign_exponent = 1 if sz_bits[0]=="1" else 0

sz_exponent = sz_bits[1:1+single_exponent_bitwidth]
sz_fraction = sz_bits[10:]

process_bits = True

sz_float = "-" if sign_exponent else ""

for sym in special_str.keys():
    if special_str[sym][0]==sz_exponent and (not special_str[sym][2] or (sz_fraction == special_str[sym][1])):
        sz_float += sym
        process_bits = False
        break

if process_bits:        
    exponent = int(sz_exponent, 2)
    fraction = int(sz_fraction, 2)

    print "e, m: ", exponent, fraction

    if exponent == 0:
        fraction = -1 
    
    print "finding value", 
    #pow(-1, sign_exponent)*(1+fraction)*pow(2, exponent-single_bias)
    sz_float += str((1+fraction)*pow(2, exponent-single_bias))
   
print "bits to float: " + sz_float