
import zipfile as zp
import os
from ui import ui
import io
from timeit import default_timer as timer  # debug
import sys
#test
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
g = os.listdir('extract')


routes = {"route_id": 0, "agency_id": 1, "route_short_name": 2, "route_long_name": 3, "route_type": 5}

stop_times = {"trip_id": 0, "arrival_time": 1, "departure_time": 2,
              "stop_id": 3, "pickup_type": 5, "drop_off_type": 6}

stops = {"stop_id": 0,  "stop_name": 2, "stop_lat": 4, "stop_lon": 5}

trips = {"route_id": 0, "service_id": 1, "trip_id": 2}

agency = {"agency_id": 0, "agency_name": 1}

calendar = {"service_id": 0, "sunday": 1, "monday": 2, "tuesday": 3, "wednesday": 4,
            "thursday": 5, "friday": 6, "saturday": 7}


agency_ff = io.open(g[0], encoding='utf8')
calendar_ff = io.open(g[1], encoding='utf8')
routes_ff = io.open(g[2], encoding='utf8')
stop_times_ff = io.open(g[4], encoding='utf8')
stops_ff = io.open(g[5], encoding='utf8')
translations_ff = io.open(g[6], encoding='utf8')
trips_ff = io.open(g[7], encoding='utf8')

for obj in g:
    print obj  # debug
    if obj == 'shapes.txt':  # add translations to exclusion list if needed
        continue

    elif obj == 'routes.txt':
        for line in routes_ff:
            if line == line[0]:
                continue
            else:
                word = line.split(",")
                if word[5] == "3":
                    word[0] #thats route_id, Paste In Sqldb (or PIS)
                    word[1] #that's agency id, PIS
                    word[2] # short name, PIS
                    word[3] # long name, PIS
                    for line2 in trips_ff:
                        if line2 == line2[0]:
                            continue
                        else:
                            word2 = line2.split(",")
                            if word2[0] == word[0]
                                word2[2] # trip_id, PIS
                            else:
                                continue
        # for line in ff:  # change to skip first line
        #     line = line.split(",")
        #     for word in line:
        #         if


end = timer()  # debug
print(end - start)  # debug
