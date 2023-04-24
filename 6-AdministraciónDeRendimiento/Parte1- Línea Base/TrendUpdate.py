import time
import rrdtool
from getSNMP import consultaSNMP
rrdpath = '/home/tani/PycharmProjects/Introduccion_SNMP/6-AdministraciónDeRendimiento/RRD/'
carga_CPU = 0

while 1:
    carga_CPU = int(consultaSNMP('comunidadSNMP','localhost','1.3.6.1.2.1.25.3.3.1.2.196608'))
    valor = "N:" + str(carga_CPU)
    print (valor)
    rrdtool.update(rrdpath+'trend.rrd', valor)
    time.sleep(5)