#!/usr/bin/python

import os
import sys

team = [2, 3, 4, 5, 6, 7, 8, 10, 11]

print('Cache my credential for 2 hours!')
os.system("git config --global credential.helper 'cache --timeout 7200'")

for n in team:
    print('Team: ' + str(n))
    os.system('git clone ' + 'https://github.com/hyojeonglee/osfall2019-team' + str(n) + '.git')
