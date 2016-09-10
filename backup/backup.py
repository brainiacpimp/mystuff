# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
import os
import os.path
import shutil
from datetime import date

print('Creating timestamp.......\n')
BU_DIR_NAME = 'bu_' + str(date.today())

print('Checking platform to get home directory.......')
if sys.platform.startswith('linux'):
    HOME_DIR = os.path.expandvars('${HOME}')
elif sys.platform.startswith('win32'):
    HOME_DIR = os.path.expandvars('%HOME')    #fill in for windows
elif sys.platform.startswith('darwin'):
    HOME_DIR = os.path.expandvars('${HOME}')   #fill in for mac/ios

print('Platform found!!\nUsing {}\n'.format(sys.platform))
BU_PATH = os.path.join(HOME_DIR, BU_DIR_NAME)

print('Creating backup archive of {}\n'.format(HOME_DIR))
shutil.make_archive(BU_PATH, 'gztar', HOME_DIR)

print('Backup successful!')
