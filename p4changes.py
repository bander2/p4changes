#!/usr/bin/env python

import subprocess
import re
import sys

# A branch name is mandatory
if not len(sys.argv):
    raise Exception('You must specify a branch name')

# Get the interchanges from Perforce
command = "p4 interchanges -b " + sys.argv[1] + " -l"
p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()

# Perforce gives is more info than we want so we need
# to format it more nicely
output = re.sub(r"^Change |\nChange ", "  - ", output)
output = re.sub(r" on (19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01]) by (.*)\n\n\t", ": ", output)

print output