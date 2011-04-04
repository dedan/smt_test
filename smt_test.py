#!/usr/bin/env python
# encoding: utf-8
"""
this is a very simple python script to do some first experiments with
sumatra
"""

import sys
import os
from sumatra.parameters import build_parameters
parameter_file = sys.argv[1]
parameters = build_parameters(parameter_file)

print parameters

# output_dir = os.path.join("Data", label)
# with open(os.path.join(output_dir, "mydata.txt"), 'w') as fp:
#     fp.write(output_data)
