#!/usr/bin/env python3

"""jayze command line interface.
"""

import os
import sys

jayze_app_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
jayze_lib_dirs = [
    os.path.join(jayze_app_dir, 'lib', 'vendor'),
    os.path.join(jayze_app_dir, 'lib'),
    jayze_app_dir,
]

for d in jayze_lib_dirs:
    if not d in sys.path:
        sys.path.insert(1, d)

from lib.conf import jayze_conf
from lib.engine import JayzeEngine
from lib.vendor.cliparser import CLIParser




if __name__ == '__main__':
    try:
        args = CLIParser(conf=jayze_conf['args']).parse_args()
        app  = JayzeEngine(conf=jayze_conf, args=args)
        app.main()
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.flush()
