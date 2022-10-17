import sys
import rrdtool
import time
tiempo_actual = int(time.time())
#Grafica desde el tiempo actual menos diez minutos
tiempo_inicial = tiempo_actual - 1800

#ret = rrdtool.graphv( "segmentosTCP.png",
                     "--start",str(tiempo_inicial),
                     "--end","N",
                     "--vertical-label=Segmentos",
                     "--title=Segmentos TCP de un agente \n Usando SNMP y RRDtools",
                     "DEF:sEntrada=segmentosRed.rrd:segmentosEntrada:AVERAGE",
                     "DEF:sSalida=segmentosRed.rrd:segmentosSalida:AVERAGE",
                      "VDEF:segEntradaLast=sEntrada,LAST",
                      "VDEF:segEntradaFirst=sEntrada,FIRST",
                      "PRINT:segEntradaLast:%6.2lf",
                      "PRINT:segEntradaFirst:%6.2lf",
                 #    "CDEF:escalaIn=traficoEntrada,8,*",
                  #   "CDEF:escalaOut=traficoSalida,8,*",
                     "LINE3:sEntrada#FF0000:Segmentros recibidos",
                     "LINE3:sSalida#0000FF:Segmentos enviados")

print(ret)