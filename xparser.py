import os
import subprocess
import config

result = {}
cwd = os.path.dirname( os.path.realpath( __file__ ) )

def parse_file(f):
    if not config.omit_xrdb:
        subprocess.call("xrdb -merge " + f, shell = True)
    res = os.popen("xrdb -query").read()[:-1].split("\n")

    for i in res:
        fields = i.split(":")
        result[ fields[0] ] = fields[1].strip()
