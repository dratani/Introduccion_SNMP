import rrdtool
ret = rrdtool.create("/home/tani/PycharmProjects/Introduccion_SNMP/6-AdministraciónDeRendimiento/RRD/trend.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:CPUload:GAUGE:60:0:100",
                     "RRA:AVERAGE:0.5:1:2400")
if ret:
    print (rrdtool.error())
