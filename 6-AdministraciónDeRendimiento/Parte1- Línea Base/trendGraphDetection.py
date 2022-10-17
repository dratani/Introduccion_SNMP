import sys
import rrdtool
from  Notify import send_alert_attached
import time
rrdpath = '/home/tani/PycharmProjects/Introduccion_SNMP/6-AdministraciónDeRendimiento/RRD/'
imgpath = '/home/tani/PycharmProjects/Introduccion_SNMP/6-AdministraciónDeRendimiento/IMG/'

ultima_lectura = int(rrdtool.last(rrdpath+"trend.rrd"))
tiempo_final = ultima_lectura
tiempo_inicial = tiempo_final - 1800

ret = rrdtool.graphv( imgpath+"deteccion.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_final),
                     "--vertical-label=Cpu load",
                    '--lower-limit', '0',
                    '--upper-limit', '100',
                    "--title=Carga del CPU del agente Usando SNMP y RRDtools \n Detección de umbrales",
                    "DEF:cargaCPU="+rrdpath+"trend.rrd:CPUload:AVERAGE",
                     "VDEF:cargaMAX=cargaCPU,MAXIMUM",
                     "VDEF:cargaMIN=cargaCPU,MINIMUM",
                     "VDEF:cargaSTDEV=cargaCPU,STDEV",
                     "VDEF:cargaLAST=cargaCPU,LAST",
                 #   "CDEF:cargaEscalada=cargaCPU,8,*",
                     "CDEF:umbral10=cargaCPU,20,LT,0,cargaCPU,IF",
                     "AREA:cargaCPU#00FF00:Carga del CPU",
                     "AREA:umbral10#FF9F00:Carga CPU mayor que 10",
                     "HRULE:20#FF0000:Umbral 10 - 5%",
                     "PRINT:cargaLAST:%6.2lf",
                     "GPRINT:cargaMIN:%6.2lf %SMIN",
                     "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                     "GPRINT:cargaLAST:%6.2lf %SLAST" )
print (ret)

ultimo_valor=float(ret['print[0]'])
if ultimo_valor>10:
    send_alert_attached("Sobrepasa Umbral línea base")
    print("Sobrepasa Umbral línea base")