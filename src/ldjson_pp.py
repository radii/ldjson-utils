#!/usr/bin/env python

# Copyright 2014-2015 Andrew Isaacson <adi@hexapodia.org>
#
# GPLv3

import json
import sys

for a in sys.stdin.readlines():
    a = a.strip()
    if not a: continue
    x = json.loads(a)
    print json.dumps(x, sort_keys=True,indent=2)
