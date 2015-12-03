import os, sys, tarfile, gzip

print(sys.argv)

if "python" in sys.argv[0]:
    file= sys.argv[2]
else:
    file= sys.argv[1]

delim = ".tar"
if "tgz" in file:
    delim=".tgz"

dir = os.path.basename(file).split(delim)[0]

print("Extracting to " + dir)

mode = "r"

#if "gz" in file:
#    mode = "r:gz"

os.mkdir(dir)

with tarfile.open(file, mode) as f:
    f.extractall(dir)
    f.close()