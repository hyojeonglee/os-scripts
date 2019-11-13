#!/usr/bin/python

import os
import sys

team = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11]

for n in team:
    print('cd team dir: ' + str(n))
    os.system('cd ' + './osfall2019-team' + str(n) + ' ; ' + 'sudo ./scripts/mkbootimg_rpi3.sh' + ' ; ' + \
        'tar -zcvf tizen-unified_20181024.1_iot-boot-arm64-rpi3.tar.gz boot.img modules.img')
    print('mkbootimg and tar done!')
