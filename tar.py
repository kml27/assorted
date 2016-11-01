import os, sys, tarfile, gzip

print(sys.argv)


def untar(file):
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
        #f.list()
        f.extractall(dir)
        f.close()

if __name__ == "__main__":
    if "python" in sys.argv[0]:
        file= sys.argv[2]
    else:
        file= sys.argv[1]

    untar(file)