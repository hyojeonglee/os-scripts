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

# checkout to target branch
for n in team:
    print("cd team dir: " + str(n))
    os.system('cd ' + './osfall2019-team' + str(n) + ' ; ' + 'git checkout proj' + str(branch))
    print('checkout done!')

# cp defconfig and qemu.sh
for n in team:
    print("team dir: " + str(n))
    os.system('cp ./qemu-scripts/qemu.sh ./osfall2019-team' + str(n))
    os.system('mv ./osfall2019-team' + str(n) + '/arch/arm64/configs/tizen_bcmrpi3_defconfig bkup.tizen_bcmrpi3_defconfig')
    os.system('cp ./qemu-scripts/tizen_bcmrpi3_defconfig ./osfall2019-team' + str(n) + '/arch/arm64/configs/')
    print('cp defconfig and qemu.sh done!') 

# build
for n in team:
    print("cd team dir: " + str(n))
    os.system('cd ' + './osfall2019-team' + str(n) + ' ; ' + ' ./build-rpi3-arm64.sh')
    print('build done!')

# mkimg_and_tar.sh
for n in team:
    print("cd team dir: " + str(n))
    os.system('cd ' + './osfall2019-team' + str(n) + ' ; ' + 'sudo ./scripts/mkbootimg_rpi3.sh')
    print('mkbootimg done!')

