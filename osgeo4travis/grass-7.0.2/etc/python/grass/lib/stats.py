'''Wrapper for stats.h

Generated with:
./ctypesgen.py --cpp clang-3.6 -E       -I/usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include -I/usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include -D__GLIBC_HAVE_LONG_LONG -lgrass_stats.7.0.2 /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/stats.h /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h -o OBJ.x86_64-unknown-linux-gnu/stats.py

Do not modify this file.
'''

__docformat__ =  'restructuredtext'


_libs = {}
_libdirs = []

from ctypes_preamble import *
from ctypes_preamble import _variadic_function
from ctypes_loader import *

add_library_search_dirs([])

# Begin libraries

_libs["grass_stats.7.0.2"] = load_library("grass_stats.7.0.2")

# 1 libraries
# End libraries

# No modules

DCELL = c_double # /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/gis.h: 566

stat_func = CFUNCTYPE(UNCHECKED(None), POINTER(DCELL), POINTER(DCELL), c_int, POINTER(None)) # /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 4

stat_func_w = CFUNCTYPE(UNCHECKED(None), POINTER(DCELL), POINTER(DCELL * 2), c_int, POINTER(None)) # /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 5

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 7
try:
    c_ave = (stat_func).in_dll(_libs['grass_stats.7.0.2'], 'c_ave')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 8
try:
    c_count = (stat_func).in_dll(_libs['grass_stats.7.0.2'], 'c_count')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 9
try:
    c_divr = (stat_func).in_dll(_libs['grass_stats.7.0.2'], 'c_divr')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 10
try:
    c_intr = (stat_func).in_dll(_libs['grass_stats.7.0.2'], 'c_intr')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 11
try:
    c_max = (stat_func).in_dll(_libs['grass_stats.7.0.2'], 'c_max')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 12
try:
    c_maxx = (stat_func).in_dll(_libs['grass_stats.7.0.2'], 'c_maxx')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 13
try:
    c_median = (stat_func).in_dll(_libs['grass_stats.7.0.2'], 'c_median')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 14
try:
    c_min = (stat_func).in_dll(_libs['grass_stats.7.0.2'], 'c_min')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 15
try:
    c_minx = (stat_func).in_dll(_libs['grass_stats.7.0.2'], 'c_minx')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 16
try:
    c_mode = (stat_func).in_dll(_libs['grass_stats.7.0.2'], 'c_mode')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 17
try:
    c_stddev = (stat_func).in_dll(_libs['grass_stats.7.0.2'], 'c_stddev')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 18
try:
    c_sum = (stat_func).in_dll(_libs['grass_stats.7.0.2'], 'c_sum')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 19
try:
    c_thresh = (stat_func).in_dll(_libs['grass_stats.7.0.2'], 'c_thresh')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 20
try:
    c_var = (stat_func).in_dll(_libs['grass_stats.7.0.2'], 'c_var')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 21
try:
    c_range = (stat_func).in_dll(_libs['grass_stats.7.0.2'], 'c_range')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 22
try:
    c_reg_m = (stat_func).in_dll(_libs['grass_stats.7.0.2'], 'c_reg_m')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 23
try:
    c_reg_c = (stat_func).in_dll(_libs['grass_stats.7.0.2'], 'c_reg_c')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 24
try:
    c_reg_r2 = (stat_func).in_dll(_libs['grass_stats.7.0.2'], 'c_reg_r2')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 25
try:
    c_reg_t = (stat_func).in_dll(_libs['grass_stats.7.0.2'], 'c_reg_t')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 26
try:
    c_quart1 = (stat_func).in_dll(_libs['grass_stats.7.0.2'], 'c_quart1')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 27
try:
    c_quart3 = (stat_func).in_dll(_libs['grass_stats.7.0.2'], 'c_quart3')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 28
try:
    c_perc90 = (stat_func).in_dll(_libs['grass_stats.7.0.2'], 'c_perc90')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 29
try:
    c_quant = (stat_func).in_dll(_libs['grass_stats.7.0.2'], 'c_quant')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 30
try:
    c_skew = (stat_func).in_dll(_libs['grass_stats.7.0.2'], 'c_skew')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 31
try:
    c_kurt = (stat_func).in_dll(_libs['grass_stats.7.0.2'], 'c_kurt')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 33
try:
    w_ave = (stat_func_w).in_dll(_libs['grass_stats.7.0.2'], 'w_ave')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 34
try:
    w_count = (stat_func_w).in_dll(_libs['grass_stats.7.0.2'], 'w_count')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 35
try:
    w_median = (stat_func_w).in_dll(_libs['grass_stats.7.0.2'], 'w_median')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 36
try:
    w_min = (stat_func_w).in_dll(_libs['grass_stats.7.0.2'], 'w_min')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 37
try:
    w_max = (stat_func_w).in_dll(_libs['grass_stats.7.0.2'], 'w_max')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 38
try:
    w_mode = (stat_func_w).in_dll(_libs['grass_stats.7.0.2'], 'w_mode')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 39
try:
    w_quart1 = (stat_func_w).in_dll(_libs['grass_stats.7.0.2'], 'w_quart1')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 40
try:
    w_quart3 = (stat_func_w).in_dll(_libs['grass_stats.7.0.2'], 'w_quart3')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 41
try:
    w_perc90 = (stat_func_w).in_dll(_libs['grass_stats.7.0.2'], 'w_perc90')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 42
try:
    w_quant = (stat_func_w).in_dll(_libs['grass_stats.7.0.2'], 'w_quant')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 43
try:
    w_reg_m = (stat_func_w).in_dll(_libs['grass_stats.7.0.2'], 'w_reg_m')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 44
try:
    w_reg_c = (stat_func_w).in_dll(_libs['grass_stats.7.0.2'], 'w_reg_c')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 45
try:
    w_reg_r2 = (stat_func_w).in_dll(_libs['grass_stats.7.0.2'], 'w_reg_r2')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 46
try:
    w_reg_t = (stat_func_w).in_dll(_libs['grass_stats.7.0.2'], 'w_reg_t')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 47
try:
    w_stddev = (stat_func_w).in_dll(_libs['grass_stats.7.0.2'], 'w_stddev')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 48
try:
    w_sum = (stat_func_w).in_dll(_libs['grass_stats.7.0.2'], 'w_sum')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 49
try:
    w_var = (stat_func_w).in_dll(_libs['grass_stats.7.0.2'], 'w_var')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 50
try:
    w_skew = (stat_func_w).in_dll(_libs['grass_stats.7.0.2'], 'w_skew')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 51
try:
    w_kurt = (stat_func_w).in_dll(_libs['grass_stats.7.0.2'], 'w_kurt')
except:
    pass

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 53
if hasattr(_libs['grass_stats.7.0.2'], 'sort_cell'):
    sort_cell = _libs['grass_stats.7.0.2'].sort_cell
    sort_cell.restype = c_int
    sort_cell.argtypes = [POINTER(DCELL), c_int]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/stats.h: 54
if hasattr(_libs['grass_stats.7.0.2'], 'sort_cell_w'):
    sort_cell_w = _libs['grass_stats.7.0.2'].sort_cell_w
    sort_cell_w.restype = c_int
    sort_cell_w.argtypes = [POINTER(DCELL * 2), c_int]

# No inserted files
