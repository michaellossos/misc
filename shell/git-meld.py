#! /opt/local/Library/Frameworks/Python.framework/Versions/2.7/bin/python 
#!/usr/bin/python

import sys
import os

os.system('meld "%s" "%s"' % (sys.argv[2], sys.argv[5]))

