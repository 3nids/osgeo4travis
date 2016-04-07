'''Wrapper for segment.h

Generated with:
./ctypesgen.py --cpp clang-3.6 -E       -I/usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include -I/usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include -D__GLIBC_HAVE_LONG_LONG -lgrass_segment.7.0.2 /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/segment.h /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/segment.h -o OBJ.x86_64-unknown-linux-gnu/segment.py

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

_libs["grass_segment.7.0.2"] = load_library("grass_segment.7.0.2")

# 1 libraries
# End libraries

# No modules

__off_t = c_long # /usr/include/x86_64-linux-gnu/bits/types.h: 141

off_t = __off_t # /usr/include/stdio.h: 91

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/segment.h: 14
class struct_aq(Structure):
    pass

struct_aq.__slots__ = [
    'cur',
    'younger',
    'older',
]
struct_aq._fields_ = [
    ('cur', c_int),
    ('younger', POINTER(struct_aq)),
    ('older', POINTER(struct_aq)),
]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/segment.h: 45
class struct_scb(Structure):
    pass

struct_scb.__slots__ = [
    'buf',
    'dirty',
    'age',
    'n',
]
struct_scb._fields_ = [
    ('buf', String),
    ('dirty', c_char),
    ('age', POINTER(struct_aq)),
    ('n', c_int),
]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/segment.h: 61
class struct_anon_27(Structure):
    pass

struct_anon_27.__slots__ = [
    'open',
    'nrows',
    'ncols',
    'len',
    'srows',
    'scols',
    'srowscols',
    'size',
    'spr',
    'spill',
    'fast_adrs',
    'scolbits',
    'srowbits',
    'segbits',
    'fast_seek',
    'lenbits',
    'sizebits',
    'address',
    'seek',
    'fname',
    'fd',
    'scb',
    'load_idx',
    'nfreeslots',
    'freeslot',
    'agequeue',
    'youngest',
    'oldest',
    'nseg',
    'cur',
    'offset',
]
struct_anon_27._fields_ = [
    ('open', c_int),
    ('nrows', off_t),
    ('ncols', off_t),
    ('len', c_int),
    ('srows', c_int),
    ('scols', c_int),
    ('srowscols', c_int),
    ('size', c_int),
    ('spr', c_int),
    ('spill', c_int),
    ('fast_adrs', c_int),
    ('scolbits', off_t),
    ('srowbits', off_t),
    ('segbits', off_t),
    ('fast_seek', c_int),
    ('lenbits', c_int),
    ('sizebits', c_int),
    ('address', CFUNCTYPE(UNCHECKED(c_int), )),
    ('seek', CFUNCTYPE(UNCHECKED(c_int), )),
    ('fname', String),
    ('fd', c_int),
    ('scb', POINTER(struct_scb)),
    ('load_idx', POINTER(c_int)),
    ('nfreeslots', c_int),
    ('freeslot', POINTER(c_int)),
    ('agequeue', POINTER(struct_aq)),
    ('youngest', POINTER(struct_aq)),
    ('oldest', POINTER(struct_aq)),
    ('nseg', c_int),
    ('cur', c_int),
    ('offset', c_int),
]

SEGMENT = struct_anon_27 # /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/segment.h: 61

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/segment.h: 4
if hasattr(_libs['grass_segment.7.0.2'], 'Segment_open'):
    Segment_open = _libs['grass_segment.7.0.2'].Segment_open
    Segment_open.restype = c_int
    Segment_open.argtypes = [POINTER(SEGMENT), String, off_t, off_t, c_int, c_int, c_int, c_int]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/segment.h: 5
if hasattr(_libs['grass_segment.7.0.2'], 'Segment_close'):
    Segment_close = _libs['grass_segment.7.0.2'].Segment_close
    Segment_close.restype = c_int
    Segment_close.argtypes = [POINTER(SEGMENT)]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/segment.h: 6
if hasattr(_libs['grass_segment.7.0.2'], 'Segment_flush'):
    Segment_flush = _libs['grass_segment.7.0.2'].Segment_flush
    Segment_flush.restype = c_int
    Segment_flush.argtypes = [POINTER(SEGMENT)]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/segment.h: 7
if hasattr(_libs['grass_segment.7.0.2'], 'Segment_format'):
    Segment_format = _libs['grass_segment.7.0.2'].Segment_format
    Segment_format.restype = c_int
    Segment_format.argtypes = [c_int, off_t, off_t, c_int, c_int, c_int]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/segment.h: 8
if hasattr(_libs['grass_segment.7.0.2'], 'Segment_format_nofill'):
    Segment_format_nofill = _libs['grass_segment.7.0.2'].Segment_format_nofill
    Segment_format_nofill.restype = c_int
    Segment_format_nofill.argtypes = [c_int, off_t, off_t, c_int, c_int, c_int]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/segment.h: 9
if hasattr(_libs['grass_segment.7.0.2'], 'Segment_get'):
    Segment_get = _libs['grass_segment.7.0.2'].Segment_get
    Segment_get.restype = c_int
    Segment_get.argtypes = [POINTER(SEGMENT), POINTER(None), off_t, off_t]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/segment.h: 10
if hasattr(_libs['grass_segment.7.0.2'], 'Segment_get_row'):
    Segment_get_row = _libs['grass_segment.7.0.2'].Segment_get_row
    Segment_get_row.restype = c_int
    Segment_get_row.argtypes = [POINTER(SEGMENT), POINTER(None), off_t]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/segment.h: 11
if hasattr(_libs['grass_segment.7.0.2'], 'Segment_init'):
    Segment_init = _libs['grass_segment.7.0.2'].Segment_init
    Segment_init.restype = c_int
    Segment_init.argtypes = [POINTER(SEGMENT), c_int, c_int]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/segment.h: 12
if hasattr(_libs['grass_segment.7.0.2'], 'Segment_put'):
    Segment_put = _libs['grass_segment.7.0.2'].Segment_put
    Segment_put.restype = c_int
    Segment_put.argtypes = [POINTER(SEGMENT), POINTER(None), off_t, off_t]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/segment.h: 13
if hasattr(_libs['grass_segment.7.0.2'], 'Segment_put_row'):
    Segment_put_row = _libs['grass_segment.7.0.2'].Segment_put_row
    Segment_put_row.restype = c_int
    Segment_put_row.argtypes = [POINTER(SEGMENT), POINTER(None), off_t]

# /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/defs/segment.h: 14
if hasattr(_libs['grass_segment.7.0.2'], 'Segment_release'):
    Segment_release = _libs['grass_segment.7.0.2'].Segment_release
    Segment_release.restype = c_int
    Segment_release.argtypes = [POINTER(SEGMENT)]

aq = struct_aq # /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/segment.h: 14

scb = struct_scb # /usr/src/grass-7.0.2/dist.x86_64-unknown-linux-gnu/include/grass/segment.h: 45

# No inserted files

