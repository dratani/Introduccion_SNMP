import sys
import rrdtool
import time
tiempo_actual = int(time.time())
#Grafica desde el tiempo actual menos diez minutos
tiempo_inicial = tiempo_actual - 600


ret = rrdtool.graph( "traficoRED.png",
                     "--start",str(tiempo_inicial),
                     "--end","N",
                     "--vertical-label=Bytes/s",
                     "--title=Tráfico de Red de un agente \n Usando SNMP y RRDtools",
                     "DEF:traficoEntrada=traficoRED.rrd:inoctets:AVERAGE",
                     "DEF:traficoSalida=traficoRED.rrd:outoctets:AVERAGE",
                     "CDEF:escalaIn=traficoEntrada,8,*",
                     "CDEF:escalaOut=traficoSalida,8,*",
                     "LINE3:escalaIn#FF0000:Tráfico de entrada",
                     "LINE3:escalaOut#0000FF:Tráfico de salida")
