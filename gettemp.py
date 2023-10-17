#!/usr/bin/python
# -*- coding: utf-8 -*-

import re, os, rrdtool, time

# function: read and parse sensor data file
def read_sensor(path):
  value = "U"
  try:
    f = open(path, "r")
    line = f.readline()
    if re.match(r"([0-9a-f]{2} ){9}: crc=[0-9a-f]{2} YES", line):
      line = f.readline()
      m = re.match(r"([0-9a-f]{2} ){9}t=([+-]?[0-9]+)", line)
      if m:
        value = str(float(m.group(2)) / 1000.0)
    f.close()
  except (IOError)as e:
     print (time.strftime("%x %X"), "Error reading", path, ": ", e)
  return value

# define pathes to 1-wire sensor data
pathes = (
  "/sys/bus/w1/devices/10-0008030e3832/w1_slave",
  "/sys/bus/w1/devices/10-0008030ec5ed/w1_slave"
)

# read sensor data
data = 'N'
for path in pathes:
  data += ':'
  data += read_sensor(path)
  time.sleep(1)

# insert data into round-robin-database
rrdtool.update(
  "%s/nuos.rrd" % (os.path.dirname(os.path.abspath(__file__))),
  data)

#Grafik erzeugen
os.system("/home/pi/nuos/grafik.sh")

