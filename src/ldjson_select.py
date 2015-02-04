#!/usr/bin/env python

# Copyright 2014-2015 Andrew Isaacson <adi@hexapodia.org>
#
# GPLv3

import argparse
import json
import sys

def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dump', action='store_true', help='dump json object (default is just print value)')
    parser.add_argument('field', nargs='+')
    opts = parser.parse_args(args)

    if opts.dump:
        func = lambda x: sys.stdout.write('%s\n' % x)
    else:
        func = lambda x: sys.stdout.write('%s\n' % json.dumps(x))

    for a in sys.stdin.readlines():
        a = a.strip()
        if not a: continue
        x = json.loads(a)
        for f in opts.field:
            if f in x:
                func(x[f])

if __name__ == '__main__':
    main(sys.argv[1:])
