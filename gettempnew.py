#!/usr/bin/python

import os
import glob
import time

# These  lines mount the device:
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
# Get all the filenames begin with 28 in the path base_dir.
device_folder = glob.glob(base_dir + '10*')[0]
device_folder1 = glob.glob(base_dir + '10*')[1]
device_folder2 = glob.glob(base_dir + '10*')[2]
device_folder3 = glob.glob(base_dir + '10*')[3]


device_file = device_folder + '/w1_slave'
device_file1 = device_folder1 + '/w1_slave'
device_file2 = device_folder2 + '/w1_slave'
device_file3 = device_folder3 + '/w1_slave'


def read_rom():
    name_file = device_folder+'/name'
    f = open(name_file,'r')
    #print('f:',f)
    return f.readline()


def read_rom1():
    name_file1 = device_folder1+'/name'
    g = open(name_file1,'r')
    #print('g:',g)
    return g.readline()

def read_rom2():
    name_file2 = device_folder2+'/name'
    h = open(name_file2,'r')
    #print('h:',h)
    return h.readline()

def read_rom3():
    name_file3 = device_folder3+'/name'
    i = open(name_file3,'r')
    #print('i:',i)
    return i.readline()


#reading temperature from folder

 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    #print('raw_f',lines)
    f.close()
    return lines

def read_temp_raw1():
    g = open(device_file1, 'r')
    lines1 = g.readlines()
    #print('raw_g',lines1)
    g.close()
    return lines1

def read_temp_raw2():
    h = open(device_file2, 'r')
    lines2 = h.readlines()
    #print('raw_h',lines2)
    h.close()
    return lines2

def read_temp_raw3():
    i = open(device_file3, 'r')
    lines3 = i.readlines()
    #print('raw_i',lines3)
    i.close()
    return lines3


#converting the temperature data to human readable form

def read_temp():
    lines = read_temp_raw()
    while lines[1].strip()[-3:] != 'YES':
        lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

def read_temp1():
    lines1 = read_temp_raw1()
    while lines1[1].strip()[-3:] != 'YES':
        lines1 = read_temp_raw1()
        equals_pos1 = lines1[1].find('t=')
        temp_string1 = lines1[1][equals_pos1 +2:]
        temp_c1 = float(temp_string1) / 1000.0
        temp_f1 = temp_c1 * 9.0 / 5.0 + 32.0
        return temp_c1, temp_f1

def read_temp2():
    lines2 = read_temp_raw2()
    while lines2[1].strip()[-3:] != 'YES':
        lines2 = read_temp_raw2()
        equals_pos2 = lines2[1].find('t=')
        temp_string2 = lines2[1][equals_pos2 +2:]
        temp_c2 = float(temp_string2) / 1000.0
        temp_f2 = temp_c2 * 9.0 / 5.0 + 32.0
        return temp_c2, temp_f2

def read_temp3():
    lines3 = read_temp_raw3()
    while lines3[1].strip()[-3:] != 'YES':
        lines3 = read_temp_raw3()
        equals_pos3 = lines3[1].find('t=')
        temp_string3 = lines3[1][equals_pos3 +2:]
        temp_c3 = float(temp_string3) / 1000.0
        temp_f3 = temp_c3 * 9.0 / 5.0 + 32.0
        return temp_c3, temp_f3


while True:
    #READING TEMPERATURE DATA AND PRINTINTING THE VALUES OF INDIVIDUAL SENSOR
    print(' C1=%3.3f  F1=%3.3f'% read_temp())
    print(' C2=%3.3f  F2=%3.3f'% read_temp1())
    print(' C3=%3.3f  F3=%3.3f'% read_temp2())
    print(' C4=%3.3f  F4=%3.3f'% read_temp3())
    time.sleep(1)

