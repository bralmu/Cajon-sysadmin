#!/usr/bin/python
#-*-  coding: utf-8 -*-
from shutil import copyfile
import os
import threading

# Configuration
SOURCEPATH = "/home/bruno/temp/"
TARGETPATH = "/home/bruno/borrame/"
CHECKPERIOD = 10 # seconds

def backup():
    files = [f for f in os.listdir(SOURCEPATH) if os.path.isfile(SOURCEPATH + f)]
    for f in files:
        source_modified_time = os.path.getmtime(SOURCEPATH + f)
        try:
            target_modified_time = os.path.getmtime(TARGETPATH + f)
        except OSError:
            target_modified_time = 0
        if source_modified_time > target_modified_time:
            copyfile(SOURCEPATH + f, TARGETPATH + f);
            print "A new version of %s has been copied." % f
    filesintargetfolder = [f for f in os.listdir(TARGETPATH) if os.path.isfile(TARGETPATH + f)]
    for f in filesintargetfolder:
        if not (f in files):
            os.remove(TARGETPATH + f)
            print "The file %s has been deleted." % f
    threading.Timer(CHECKPERIOD, backup).start()

backup()
