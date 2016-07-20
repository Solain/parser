
import zipfile as zp
import os  #Solain branch
from ui import ui
import io
from timeit import default_timer as timer  # debug
import sys

start = timer()  # debug
x = ui()
zipname = x[0]
direc = x[1]


def unzip():
    try:
        os.chdir(direc)
    except IOError:
        print("Error: could not change directory")
    else:
        try:
            zp.is_zipfile(zipname)
        except zp.BadZipfile:
            print("File is not zip")
        else:
            with zp.ZipFile(zipname, 'r') as zf:
                zf.extractall('extract')


try:
    os.chdir('extract')
except os.error:
    print("Could not change directory")
g = os.listdir(os.getcwd())

for obj in g:
    if obj == 'shapes.txt':
        continue
    print obj
    with io.open(obj, encoding='utf8') as ff:
        for line in ff:
            line = line.split()
            for word in line:
                if word == "shape_dist_traveled" or \
                                word == "drop_off_type" \
                        or word == "pickup_type" \
                        or word == "stop_sequence" \
                        or word == "start_date" \
                        or word == 'end_date' \
                        or word == "route_desc"\
                        or word == "route_type"\
                        or word == "route_color"\
                        or word == "" \
                        or word == "" \
                        or word == "" \
                        or word == "" \
                        or word == "" \
                        or word == "" \
                        or word == "" \
                        or word == "" \
                        or word == ""\
                        :
                    continue
                elif word == "":
                    pass
                elif word == "":
                    pass
                elif word == "":
                    pass
                elif word == "":
                    pass
                elif word == "":
                    pass
                elif word == "":
                    pass
                elif word == "":
                    pass
                elif word == "":
                    pass
                elif word == "":
                    pass
                elif word == "":
                    pass
                else:
                    print "CRITICAL: New unknown row type detected; exiting"
                    sys.exit()


end = timer()  # debug
print(end - start)  # debug
