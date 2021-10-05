#!/usr/bin/env python3

#import some tools
import shutil
import os

#set directory path
os.chdir('/home/student/mycode/')

#move/copy file
shutil.move('raynor.obj', 'ceph_storage/')

#get filename from user
xname = input('What is the new name for kerrigan.obj? ')

#move/copy file appended with inputed name
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

