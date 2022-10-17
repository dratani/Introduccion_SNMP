import time
import rrdtool
from getSNMP import consultaSNMP
#from Notify import check_aberration
total_input_traffic = 0
from path import *

fname=rrdpath+rrdname
# Generate charts for last 24 hours
endDate = rrdtool.last(fname) #ultimo valor del XML
begDate = endDate - 3600
while 1:
    total_input_traffic = int(consultaSNMP('SNMPcom','localhost','1.3.6.1.2.1.2.2.1.10.1'))

    valor = rrdtool.lastupdate(fname)+1 + str(total_input_traffic)
    print (valor)
    ret = rrdtool.update(fname, valor)
    rrdtool.dump(fname,'pred.xml')
    time.sleep(1)
#    print (check_aberration(rrdpath,rrdname))
if ret:
    print (rrdtool.error())
    time.sleep(300)
