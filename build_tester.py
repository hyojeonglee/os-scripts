#!/usr/bin/python

import os
import sys

team = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11]
#team = [1]

for n in team:
    print('cd team dir: ' + str(n))
    if (os.path.isfile("./osfall2019-team"+str(n)+"/test/Makefile")):
        os.system('cd ' + './osfall2019-team' + str(n) + ' ; ' + 'cd test' + ' ; ' + 'make')
    elif (os.path.isfile("./osfall2019-team"+str(n)+"/test/test.c")):
        os.system('cd ' + './osfall2019-team' + str(n) + ' ; ' + 'cd test' + ' ; ' + 'arm-linux-gnueabi-gcc -I../include test.c -o test')
    else:
	print("*** team " + str(n) + " need to do manually ***")
    print('build done!')
