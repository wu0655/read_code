#!/usr/bin/env python3

import sys
import codecs
import shutil
import os

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

to_dir = sys.argv[2]
in_list = sys.argv[1]

print ('para number=', len(sys.argv))
print ('para=', str(sys.argv))
print ('script name=', str(sys.argv[0]))

print ('to_dir=', to_dir)


def cp_parents(files, target_dir):
    dirs = []
    for file in files:
        dirs.append(os.path.dirname(file.strip()))
    dirs.sort(reverse=True)
    for i in range(len(dirs)):
        if not dirs[i] in dirs[i-1]:
            need_dir = os.path.normpath(target_dir + dirs[i])
            print("Creating", need_dir )
            try:
                os.makedirs(need_dir)
            except IOError:
                pass
    for file in files:
        fname = file.strip()
        dest = os.path.normpath(target_dir + fname)
        print("Copying %s to %s" % (fname, dest))
        shutil.copy(fname, dest)
 

#def do_copy(name):
#    shutil.copyfile(name, to_dir)


#with open(sys.argv[1]) as file:
#    for line in file:
#        do_copy(line)


f = open(sys.argv[1],'r',encoding='utf-8')
lines = f.readlines() 
cp_parents(lines, to_dir)
f.close
