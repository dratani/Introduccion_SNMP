#!/usr/bin/env python
import rrdtool
ret = rrdtool.create("traficoRED.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:inoctets:COUNTER:120:U:U",
                     "DS:outoctets:COUNTER:120:U:U",
                     "RRA:AVERAGE:0.5:5:48",
                     "RRA:AVERAGE:0.5:1:288")
if ret:
    print (rrdtool.error())

rrdtool.dump("traficoRED.rrd","traficoRED.xml")
