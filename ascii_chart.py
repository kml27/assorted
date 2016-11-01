import sys
ascii = open("ascii_chart", "w+")

known_replace = {0x0:"<null>", 0x7:"<bell>", 0x8:"<bkspace>", 0x9:"<tab>", 0xa:"<cr>", 0xd:"<lf>", 0x7F:"<del>", 0xff:"<nbsp>"}

replace = {i:None if not i in known_replace.keys() else known_replace[i] for i in range(0x100) }

ascii.write("ascii chart\n")

istty = sys.stdin.isatty()

for j in range(64):
 for i in range(4):
  ordinal_value = i+j*4
  strrep = chr(ordinal_value)
  if replace[ordinal_value] is not None:
    strrep = replace[ordinal_value]
  charcode = str(ordinal_value) + " " + hex(ordinal_value) + " " + strrep + "\t"
  
  #sys.stdout.write("\x1b[6n")
  #pos = sys.stdin.read(10)
  #print pos
  #sys.stdout.write()
  
  sys.stdout.write(charcode)
  ascii.write(charcode)
 ascii.write("\n")
 sys.stdout.write("\n")
ascii.close()