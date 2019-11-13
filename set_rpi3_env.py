#!/usr/bin/python

import os
import sys

team = [2, 3, 4, 5, 6, 7, 8, 10, 11]
branch = 2

# clone_all_projs.py
print('Cache my credential for 2 hours!')
os.system("git config --global credential.helper 'cache --timeout 7200'")

for n in team:
    print('Team: ' + str(n))
    os.system('git clone ' + 'https://github.com/hyojeonglee/osfall2019-team' + str(n) + '.git')

# checkout_and_build.py
for n in team:
    print("cd team dir: " + str(n))
    os.system('cd ' + './osfall2019-team' + str(n) + ' ; ' + 'git checkout proj' + str(branch) + ' ; ' + ' ./build-rpi3-arm64.sh')
    print('build done!')

# mkimg_and_tar.sh
for n in team:
    print("cd team dir: " + str(n))
    os.system('cd ' + './osfall2019-team' + str(n) + ' ; ' + 'sudo ./scripts/mkbootimg_rpi3.sh' + ' ; ' + \
	'tar -zcvf tizen-unified_20181024.1_iot-boot-arm64-rpi3.tar.gz boot.img modules.img')
    print('mkbootimg and tar done!')


