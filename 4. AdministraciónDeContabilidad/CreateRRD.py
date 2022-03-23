#!/usr/bin/env python
import rrdtool
ret = rrdtool.create("segmentosRed.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:segmentosEntrada:COUNTER:120:U:U",
                     "DS:segmentosSalida:COUNTER:120:U:U",
                     "RRA:AVERAGE:0.5:6:5",
                     "RRA:AVERAGE:0.5:1:20")

if ret:
    print (rrdtool.error())