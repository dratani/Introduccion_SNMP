import time
import rrdtool
from path import *

title="Deteccion de comportamiento anomalo"
fname=rrdpath+rrdname
endDate = rrdtool.last(fname) #ultimo valor del XML
begDate = endDate - 30000
DatosAyer=begDate - 86400
FinAyer=endDate - 86400
#rrdtool.tune(rrdname, '--alpha', '0.1')
ret = rrdtool.graph(pngpath+"pred.png",
                        '--start', str(begDate), '--end', str(endDate), '--title=' + title,
                        "--vertical-label=Bytes/s",
                        '--slope-mode',
                        "DEF:obs=" + fname + ":inoctets:AVERAGE",
                        "DEF:obsAyer=" + fname + ":inoctets:AVERAGE:start="+str(DatosAyer)+":end="+str(FinAyer),
                        "DEF:pred=" + fname + ":inoctets:HWPREDICT",
                        "DEF:dev=" + fname + ":inoctets:DEVPREDICT",
                        "DEF:fail=" + fname + ":inoctets:FAILURES",
                        'SHIFT:obsAyer:86400',
                    #"RRA:DEVSEASONAL:1d:0.1:2",
                    #"RRA:DEVPREDICT:5d:5",
                    #"RRA:FAILURES:1d:7:9:5""
                        "CDEF:scaledobs=obs,8,*",
                        "CDEF:scaledobsAyer=obsAyer,8,*",
                        "CDEF:upper=pred,dev,2,*,+",
                        "CDEF:lower=pred,dev,2,*,-",
                        "CDEF:scaledupper=upper,8,*",
                        "CDEF:scaledlower=lower,8,*",
                        "CDEF:scaledpred=pred,8,*",
                    "TICK:fail#FDD017:1.0: Fallas",
                    "AREA:scaledobsAyer#9C9C9C:Ayer",
                    "LINE3:scaledobs#00FF00:In traffic",
                    "LINE1:scaledpred#FF00FF:Prediccion",
                    #"LINE1:outoctets#0000FF:Out traffic",
                    "LINE1:scaledupper#ff0000:Upper Bound Average bits in",
                    "LINE1:scaledlower#0000FF:Lower Bound Average bits in")
rrdtool.dump(fname, 'pred.xml')
