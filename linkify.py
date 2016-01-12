#!/usr/bin/env python

import sys
import re

def clean(s):
    """
    Returns a cleaned up version of a string. Only [a-z0-9\_] permitted.
    """
    s = s.lower()
    s = re.sub(r'[^a-z0-9]', "_", s)
    return s

response = ""
for e in sys.argv[1:]:
    response += clean(e)
    response += "_"

print response.rstrip('_')


