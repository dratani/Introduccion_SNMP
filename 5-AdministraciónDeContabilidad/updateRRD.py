import time
import rrdtool
from getSNMP import consultaSNMP
while 1:
    tcp_in_segments = int(
        consultaSNMP('comunidadSNMP','localhost',
                     '1.3.6.1.2.1.6.10.0'))
    tcp_out_segments = int(
        consultaSNMP('comunidadSNMP','localhost',
                     '1.3.6.1.2.1.6.11.0'))
    valor = "N:" + str(tcp_in_segments) + ':' + str(tcp_out_segments)
    print (valor)
    rrdtool.update('segmentosRed.rrd', valor)
   # rrdtool.dump('traficoRED.rrd','traficoRED.xml')
    time.sleep(1)

if ret:
    print (rrdtool.error())
    time.sleep(300)