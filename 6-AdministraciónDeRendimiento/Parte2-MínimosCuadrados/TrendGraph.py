import rrdtool
import time
rrdpath = '/home/tani/PycharmProjects/Introduccion_SNMP/6-AdministraciónDeRendimiento/RRD/'
imgpath = '/home/tani/PycharmProjects/Introduccion_SNMP/6-AdministraciónDeRendimiento/IMG/'
fname = 'trend.rrd'
ultima_lectura = int(rrdtool.last(rrdpath+fname))
tiempo_final = ultima_lectura + 600
tiempo_inicial = tiempo_final - 1500

ret = rrdtool.graph( imgpath+"trend.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_final),
                     "--vertical-label=Carga CPU",
                     "--title=Tendencia del uso del CPU",
                     "--color", "ARROW#009900",
                     '--vertical-label', "Uso de CPU (%)",
                     '--lower-limit', '0',
                     '--upper-limit', '100',
                     "DEF:carga="+rrdpath+"trend.rrd:CPUload:AVERAGE",
                     "AREA:carga#00FF00:Carga CPU",
                     "LINE10:90#ff000022",
                     "LINE10:100#ff000052",
                     "VDEF:CPUlast=carga,LAST",
                     "VDEF:CPUmin=carga,MINIMUM",
                     "VDEF:CPUavg=carga,AVERAGE",
                     "VDEF:CPUmax=carga,MAXIMUM",

                    "COMMENT:Now        Min           Avg          Max",
                     "GPRINT:CPUlast:Now-%12.0lf%s",
                     "GPRINT:CPUmin:%10.0lf%s",
                     "GPRINT:CPUavg:%13.0lf%s",
                     "GPRINT:CPUmax:%13.0lf%s",
                     "VDEF:m=carga,LSLSLOPE",
                     "VDEF:b=carga,LSLINT",
                     'CDEF:tendenciaEscalada=carga,8,*',
                     'CDEF:tendencia=carga,POP,m,COUNT,*,b,+',
                     "LINE2:tendencia#FFBB00")