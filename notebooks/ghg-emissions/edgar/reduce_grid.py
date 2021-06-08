import numpy as np
from itertools import groupby
from operator import itemgetter
from statistics import mean
import itertools
import os

###### The goal of this function is to project our row data with an "old grid" of 0.1x0.1 in latitude/longitude onto a larger new grid 1x1 in latitude/longitude
###### For that, we aggregate the points and do a sum


# Define here the range of sectors, years and gas that will be projected 
list_sectors=["AWB","ENE","IND","RCO","REF_TRF", "SWD_INC","TNR_Other","TNR_Ship","TOTALS","TRO_noRES"]
list_gas=['CO2_org_short-cycle_C']

list_years=['1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982',
            '1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996'
            ,'1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009',
           '2010','2011','2012','2013','2014','2015','2016','2017','2018']
path="data/"

# Main loop
for gas in list_gas:
    for sect in list_sectors:
        for yr in list_years:

            # name of the file. Needs to follow the arborescence of edgar raw data
            namefile=path+gas+"/"+sect+"_txt/v6.0_"+gas+"_"+yr+"_"+sect+".txt"

            # check if file exists
            if os.path.isfile(namefile):

                print(yr,sect)

                # File containing the reduced data
                fileout = open("reduced/"+gas+"/"+sect+"_txt/v6.0_"+gas+"_"+yr+"_"+sect+".txt","w")

                # Copy the 3 lines header of the file
                with open(namefile,"r") as filein:
                    fileout.write(filein.readline())
                    fileout.write(filein.readline())
                    fileout.write(filein.readline())

                # get the data
                data = np.genfromtxt(namefile,delimiter=";",skip_header=3)
                data = np.transpose(data)


                # This projects the coordinates of the old grid (0.1x0.1) onto our new grid (1.0x1.0)

                data[0] = [np.floor(lat) for lat in data[0]]
                data[1] = [np.floor(lon) for lon in data[1]]
                data=np.transpose(data)


                # The idea is to create an object that has : 
                #           1) latitude of the new grid, i.e between -90 and 89 with a 1 deg step
                #           2) longitude of the new grid, i.e between -180 and 179 with a 1 deg step
                #           3) list of all emissions from old grid that are associated with the valeus of latitude and longitude of the new grid


                # Unfortunately, the function grouby needs the data to be sorted. While this is the case for the latitude in the raw data, the longitude is not. 
                # So, we do a first sorting using latitude. At the end of this step, some groups can have the same keys (because of groupby function behavior). To solve that
                # we then resort along longitude and do a second groupby to have our final aggregated groups. 

                grouper = groupby(data, key=lambda x: (x[0],x[1]))
                inter_list = [[x[0],x[1], [yi[2] for yi in y]] for x,y in grouper]
                a=sorted(inter_list,key=lambda x:x[1])
                grouper = groupby(a, key=lambda x: (x[0],x[1]))
                em_red=[[x[0],x[1], list(itertools.chain.from_iterable([yi[2] for yi in y]))] for x,y in grouper] # we make a big list with all emissions from the original list

                # We are interested in the sum of all the emissions inside the larger grid
                em_red=[[x[0],x[1],np.sum(x[2])] for x in em_red] 

                # Re-sort according to latitude (to be closer to raw data format)
                em_red = sorted(em_red,key=lambda x:x[0])

                # Write in the output file 
                for x in em_red:
                    fileout.write("{} \t {} \t {} \n".format(x[0],x[1],x[2]))

