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
                     "DEF:inoctets=traficoRED.rrd:inoctets:AVERAGE",
                     "DEF:outoctets=traficoRED.rrd:outoctets:AVERAGE",
                     "AREA:inoctets#00FF00:Tráfico de entrada",
                     "LINE3:outoctets#0000FF:Tráfico de salida")
