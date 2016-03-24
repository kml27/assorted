ascii = open("ascii_chart", "w+")

ascii.write("ascii chart\n")
for j in range(64):
 for i in range(4):
  ordinal_value = i+j*4
  ascii.write(str(ordinal_value) + " " + hex(ordinal_value) + " " + chr(ordinal_value) + "\t")
 ascii.write("\n")
ascii.close()