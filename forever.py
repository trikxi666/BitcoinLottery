#!/usr/bin/python
from subprocess import Popen
import sys

# filename = sys.argv[1]
filename = "test.py"

while True:
    print("\nStarting " + filename)
    p = Popen("python " + filename, shell=True)
    p.wait()