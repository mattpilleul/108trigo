#!/usr/bin/env python3

import sys
import math
from utils_matrix import *
from calc_matrix import *
from fonction_matrix import *


if (len(sys.argv) >= 2):
    if (sys.argv[1] == "-h"):
        man_help()
    elif (sys.argv[1] == "--help"):
        man_help()

check_param()
arg = error_management()
matrix = []
for i in range(int(arg)):
    matrix.append([])
    for j in range(int(arg)):
        matrix[i].append(sys.argv[i * int(arg) + j + 2])
run_calcul(matrix)
