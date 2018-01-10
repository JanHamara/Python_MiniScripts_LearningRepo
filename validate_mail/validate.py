#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Program entry point"""

import re

def validate(argv):
    mail = argv
    pattern = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
    valid = False

    if re.search(pattern, mail):
        valid = True

    return valid




