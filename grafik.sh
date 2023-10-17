rrdtool graph tempday.png \
  -w 785 -h 180 -a PNG \
  -s 'now - 1 day' -e 'now' \
  --vertical-label "temperature (°C)" \
  DEF:temp0=nuos.rrd:temp0:AVERAGE \
  LINE2:temp0#00FF00:Nuos \
  DEF:temp1=nuos.rrd:temp1:AVERAGE \
  LINE2:temp1#0000FF:Outside

rrdtool graph tempweek.png \
  -w 785 -h 180 -a PNG \
  -s 'now - 1 week' -e 'now' \
  --vertical-label "temperature (°C)" \
  DEF:temp0=nuos.rrd:temp0:AVERAGE \
  LINE2:temp0#00FF00:Nuos \
  DEF:temp1=nuos.rrd:temp1:AVERAGE \
  LINE2:temp1#0000FF:Outside

rrdtool graph tempmonth.png \
  -w 785 -h 120 -a PNG \
  -s 'now - 1 month' -e 'now' \
  --vertical-label "temperature (°C)" \
  DEF:temp0=nuos.rrd:temp0:AVERAGE \
  LINE2:temp0#00FF00:Nuos \
  DEF:temp1=nuos.rrd:temp1:AVERAGE \
  LINE2:temp1#0000FF:Outside
  
cp -p /home/pi/nuos/tempday.png /var/www/nuos/  
cp -p /home/pi/nuos/tempweek.png /var/www/nuos/  
cp -p /home/pi/nuos/tempmonth.png /var/www/nuos/  
