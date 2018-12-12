#!/usr/bin/env python3.7

import os
import sys
import cg
import config

if __name__ == "__main__":
    i = ""
    if len( sys.argv ) <= 1:
        if config.log_level >= 1 and not config.omit_xrdb:
            print("[WARNING] No file specified, using default '" + config.default + "'.")

        i = config.default
    else:
        i = sys.argv[1]

    cg.init( i )
