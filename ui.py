
def read_cache():
    with open("cache.txt", "r+") as f:
        byt = f.read()
        byt = byt.split()
        return byt


def write_cache(a, b):
    with open("cache.txt", "w") as f:
        f.write(a + "\n" + b)


def ui():
    g = raw_input("Use cache file? (y/n): ")

    while g != 'y' and g != 'n':
        g = raw_input( "Error: Please input a valid (y/n): ")

    if g == "y":
        i = read_cache()
        return i

    elif g == "n":
        zipname = raw_input("Zip file name: ")
        direc = raw_input("Zip file folder directory: ")
        write_cache(zipname, direc)
        i = [zipname, direc]
        return i
