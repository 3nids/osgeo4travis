'''Wrapper for temporal.h

Generated with:
./ctypesgen.py --cpp clang-3.6 -E       -I/usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include -I/usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include -D__GLIBC_HAVE_LONG_LONG -lgrass_temporal.7.0.4 /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h -o OBJ.x86_64-pc-linux-gnu/temporal.py

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

_libs["grass_temporal.7.0.4"] = load_library("grass_temporal.7.0.4")

# 1 libraries
# End libraries

# No modules

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/datetime.h: 27
class struct_DateTime(Structure):
    pass

struct_DateTime.__slots__ = [
    'mode',
    '_from',
    'to',
    'fracsec',
    'year',
    'month',
    'day',
    'hour',
    'minute',
    'second',
    'positive',
    'tz',
]
struct_DateTime._fields_ = [
    ('mode', c_int),
    ('_from', c_int),
    ('to', c_int),
    ('fracsec', c_int),
    ('year', c_int),
    ('month', c_int),
    ('day', c_int),
    ('hour', c_int),
    ('minute', c_int),
    ('second', c_double),
    ('positive', c_int),
    ('tz', c_int),
]

DateTime = struct_DateTime # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/datetime.h: 27

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/gis.h: 556
class struct_TimeStamp(Structure):
    pass

struct_TimeStamp.__slots__ = [
    'dt',
    'count',
]
struct_TimeStamp._fields_ = [
    ('dt', DateTime * 2),
    ('count', c_int),
]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/dbmi.h: 304
class struct__db_connection(Structure):
    pass

struct__db_connection.__slots__ = [
    'driverName',
    'hostName',
    'databaseName',
    'schemaName',
    'port',
    'user',
    'password',
    'keycol',
    'group',
]
struct__db_connection._fields_ = [
    ('driverName', String),
    ('hostName', String),
    ('databaseName', String),
    ('schemaName', String),
    ('port', String),
    ('user', String),
    ('password', String),
    ('keycol', String),
    ('group', String),
]

dbConnection = struct__db_connection # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/dbmi.h: 304

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 14
if hasattr(_libs['grass_temporal.7.0.4'], 'tgis_set_connection'):
    tgis_set_connection = _libs['grass_temporal.7.0.4'].tgis_set_connection
    tgis_set_connection.restype = c_int
    tgis_set_connection.argtypes = [POINTER(dbConnection)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 15
if hasattr(_libs['grass_temporal.7.0.4'], 'tgis_get_connection'):
    tgis_get_connection = _libs['grass_temporal.7.0.4'].tgis_get_connection
    tgis_get_connection.restype = c_int
    tgis_get_connection.argtypes = [POINTER(dbConnection)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 16
if hasattr(_libs['grass_temporal.7.0.4'], 'tgis_get_default_driver_name'):
    tgis_get_default_driver_name = _libs['grass_temporal.7.0.4'].tgis_get_default_driver_name
    tgis_get_default_driver_name.restype = ReturnString
    tgis_get_default_driver_name.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 17
if hasattr(_libs['grass_temporal.7.0.4'], 'tgis_get_default_database_name'):
    tgis_get_default_database_name = _libs['grass_temporal.7.0.4'].tgis_get_default_database_name
    tgis_get_default_database_name.restype = ReturnString
    tgis_get_default_database_name.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 18
if hasattr(_libs['grass_temporal.7.0.4'], 'tgis_get_driver_name'):
    tgis_get_driver_name = _libs['grass_temporal.7.0.4'].tgis_get_driver_name
    tgis_get_driver_name.restype = ReturnString
    tgis_get_driver_name.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 19
if hasattr(_libs['grass_temporal.7.0.4'], 'tgis_get_database_name'):
    tgis_get_database_name = _libs['grass_temporal.7.0.4'].tgis_get_database_name
    tgis_get_database_name.restype = ReturnString
    tgis_get_database_name.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 20
if hasattr(_libs['grass_temporal.7.0.4'], 'tgis_get_mapset_driver_name'):
    tgis_get_mapset_driver_name = _libs['grass_temporal.7.0.4'].tgis_get_mapset_driver_name
    tgis_get_mapset_driver_name.restype = ReturnString
    tgis_get_mapset_driver_name.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 21
if hasattr(_libs['grass_temporal.7.0.4'], 'tgis_get_mapset_database_name'):
    tgis_get_mapset_database_name = _libs['grass_temporal.7.0.4'].tgis_get_mapset_database_name
    tgis_get_mapset_database_name.restype = ReturnString
    tgis_get_mapset_database_name.argtypes = [String]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 22
if hasattr(_libs['grass_temporal.7.0.4'], 'tgis_set_default_connection'):
    tgis_set_default_connection = _libs['grass_temporal.7.0.4'].tgis_set_default_connection
    tgis_set_default_connection.restype = c_int
    tgis_set_default_connection.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 49
class struct__tgisMap(Structure):
    pass

struct__tgisMap.__slots__ = [
    'name',
    'mapset',
    'ts',
]
struct__tgisMap._fields_ = [
    ('name', String),
    ('mapset', String),
    ('ts', struct_TimeStamp),
]

tgisMap = struct__tgisMap # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 49

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 71
class struct__tgisMapList(Structure):
    pass

struct__tgisMapList.__slots__ = [
    'values',
    'n_values',
    'alloc_values',
]
struct__tgisMapList._fields_ = [
    ('values', POINTER(POINTER(tgisMap))),
    ('n_values', c_int),
    ('alloc_values', c_int),
]

tgisMapList = struct__tgisMapList # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 71

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 74
if hasattr(_libs['grass_temporal.7.0.4'], 'tgis_init_map_list'):
    tgis_init_map_list = _libs['grass_temporal.7.0.4'].tgis_init_map_list
    tgis_init_map_list.restype = None
    tgis_init_map_list.argtypes = [POINTER(tgisMapList)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 75
if hasattr(_libs['grass_temporal.7.0.4'], 'tgis_free_map_list'):
    tgis_free_map_list = _libs['grass_temporal.7.0.4'].tgis_free_map_list
    tgis_free_map_list.restype = None
    tgis_free_map_list.argtypes = [POINTER(tgisMapList)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 76
if hasattr(_libs['grass_temporal.7.0.4'], 'tgis_new_map_list'):
    tgis_new_map_list = _libs['grass_temporal.7.0.4'].tgis_new_map_list
    tgis_new_map_list.restype = POINTER(tgisMapList)
    tgis_new_map_list.argtypes = []

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 78
if hasattr(_libs['grass_temporal.7.0.4'], 'tgis_map_list_insert'):
    tgis_map_list_insert = _libs['grass_temporal.7.0.4'].tgis_map_list_insert
    tgis_map_list_insert.restype = None
    tgis_map_list_insert.argtypes = [POINTER(tgisMapList), String, String, POINTER(struct_TimeStamp)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 80
if hasattr(_libs['grass_temporal.7.0.4'], 'tgis_map_list_add'):
    tgis_map_list_add = _libs['grass_temporal.7.0.4'].tgis_map_list_add
    tgis_map_list_add.restype = None
    tgis_map_list_add.argtypes = [POINTER(tgisMapList), POINTER(tgisMap)]

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 103
class struct__tgisExtent(Structure):
    pass

struct__tgisExtent.__slots__ = [
    'start',
    'end',
    'has_end',
    'north',
    'south',
    'east',
    'west',
    'top',
    'bottom',
]
struct__tgisExtent._fields_ = [
    ('start', c_double),
    ('end', c_double),
    ('has_end', c_char),
    ('north', c_double),
    ('south', c_double),
    ('east', c_double),
    ('west', c_double),
    ('top', c_double),
    ('bottom', c_double),
]

tgisExtent = struct__tgisExtent # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 103

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 133
class struct__tgisDataset(Structure):
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 128
class struct__tgisDatasetList(Structure):
    pass

struct__tgisDatasetList.__slots__ = [
    'values',
    'n_values',
    'alloc_values',
]
struct__tgisDatasetList._fields_ = [
    ('values', POINTER(POINTER(struct__tgisDataset))),
    ('n_values', c_int),
    ('alloc_values', c_int),
]

tgisDatasetList = struct__tgisDatasetList # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 128

struct__tgisDataset.__slots__ = [
    'name',
    'mapset',
    'creator',
    'creation_time',
    'temporal_type',
    'ts',
    'extent',
    'metadata',
    'dataset_type',
    'is_stds',
    'next',
    'prev',
    'equal',
    'follows',
    'precedes',
    'overlaps',
    'overlapped',
    'during',
    'contains',
    'starts',
    'started',
    'finishes',
    'finished',
    'equivalent',
    'cover',
    'covered',
    'overlap',
    '_in',
    'contain',
    'meet',
]
struct__tgisDataset._fields_ = [
    ('name', String),
    ('mapset', String),
    ('creator', String),
    ('creation_time', DateTime),
    ('temporal_type', c_char),
    ('ts', struct_TimeStamp),
    ('extent', tgisExtent),
    ('metadata', POINTER(None)),
    ('dataset_type', c_char),
    ('is_stds', c_char),
    ('next', POINTER(struct__tgisDataset)),
    ('prev', POINTER(struct__tgisDataset)),
    ('equal', tgisDatasetList),
    ('follows', tgisDatasetList),
    ('precedes', tgisDatasetList),
    ('overlaps', tgisDatasetList),
    ('overlapped', tgisDatasetList),
    ('during', tgisDatasetList),
    ('contains', tgisDatasetList),
    ('starts', tgisDatasetList),
    ('started', tgisDatasetList),
    ('finishes', tgisDatasetList),
    ('finished', tgisDatasetList),
    ('equivalent', tgisDatasetList),
    ('cover', tgisDatasetList),
    ('covered', tgisDatasetList),
    ('overlap', tgisDatasetList),
    ('_in', tgisDatasetList),
    ('contain', tgisDatasetList),
    ('meet', tgisDatasetList),
]

tgisDataset = struct__tgisDataset # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 174

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 178
for _lib in _libs.values():
    if hasattr(_lib, 'tgis_init_dataset_list'):
        tgis_init_dataset_list = _lib.tgis_init_dataset_list
        tgis_init_dataset_list.restype = None
        tgis_init_dataset_list.argtypes = [POINTER(tgisDatasetList)]
        break

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 179
for _lib in _libs.values():
    if hasattr(_lib, 'tgis_free_dataset_list'):
        tgis_free_dataset_list = _lib.tgis_free_dataset_list
        tgis_free_dataset_list.restype = None
        tgis_free_dataset_list.argtypes = [POINTER(tgisDatasetList)]
        break

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 180
for _lib in _libs.values():
    if hasattr(_lib, 'tgis_new_dataset_list'):
        tgis_new_dataset_list = _lib.tgis_new_dataset_list
        tgis_new_dataset_list.restype = POINTER(tgisDatasetList)
        tgis_new_dataset_list.argtypes = []
        break

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 182
for _lib in _libs.values():
    if hasattr(_lib, 'tgis_dataset_list_insert'):
        tgis_dataset_list_insert = _lib.tgis_dataset_list_insert
        tgis_dataset_list_insert.restype = None
        tgis_dataset_list_insert.argtypes = [POINTER(tgisDatasetList), String, String, String, POINTER(DateTime), c_char, POINTER(struct_TimeStamp), POINTER(tgisExtent), POINTER(None), c_char, c_char]
        break

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 187
for _lib in _libs.values():
    if hasattr(_lib, 'tgis_dataset_list_add'):
        tgis_dataset_list_add = _lib.tgis_dataset_list_add
        tgis_dataset_list_add.restype = None
        tgis_dataset_list_add.argtypes = [POINTER(tgisDataset)]
        break

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 191
for _lib in _libs.values():
    if hasattr(_lib, 'tgis_build_topology'):
        tgis_build_topology = _lib.tgis_build_topology
        tgis_build_topology.restype = c_int
        tgis_build_topology.argtypes = [POINTER(tgisDatasetList), c_char]
        break

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 194
for _lib in _libs.values():
    if hasattr(_lib, 'tgis_build_topology2'):
        tgis_build_topology2 = _lib.tgis_build_topology2
        tgis_build_topology2.restype = c_int
        tgis_build_topology2.argtypes = [POINTER(tgisDatasetList), POINTER(tgisDatasetList), c_char]
        break

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 202
for _lib in _libs.values():
    if hasattr(_lib, 'tgis_create_stds'):
        tgis_create_stds = _lib.tgis_create_stds
        tgis_create_stds.restype = c_int
        tgis_create_stds.argtypes = [String, c_char, c_char, String, String, String, String]
        break

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 206
for _lib in _libs.values():
    if hasattr(_lib, 'tgis_modify_stds'):
        tgis_modify_stds = _lib.tgis_modify_stds
        tgis_modify_stds.restype = c_int
        tgis_modify_stds.argtypes = [String, c_char, String, String, String, String]
        break

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 211
for _lib in _libs.values():
    if hasattr(_lib, 'tgis_remove_stds'):
        tgis_remove_stds = _lib.tgis_remove_stds
        tgis_remove_stds.restype = c_int
        tgis_remove_stds.argtypes = [String, c_char, c_char]
        break

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 214
for _lib in _libs.values():
    if hasattr(_lib, 'tgis_update_stds'):
        tgis_update_stds = _lib.tgis_update_stds
        tgis_update_stds.restype = c_int
        tgis_update_stds.argtypes = [String, c_char]
        break

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 218
for _lib in _libs.values():
    if hasattr(_lib, 'tgis_register_map'):
        tgis_register_map = _lib.tgis_register_map
        tgis_register_map.restype = c_int
        tgis_register_map.argtypes = [POINTER(tgisMap), c_char, String]
        break

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 221
for _lib in _libs.values():
    if hasattr(_lib, 'tgis_unregister_map'):
        tgis_unregister_map = _lib.tgis_unregister_map
        tgis_unregister_map.restype = c_int
        tgis_unregister_map.argtypes = [POINTER(tgisMap), c_char, String]
        break

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 224
for _lib in _libs.values():
    if hasattr(_lib, 'tgis_register_maps'):
        tgis_register_maps = _lib.tgis_register_maps
        tgis_register_maps.restype = c_int
        tgis_register_maps.argtypes = [POINTER(tgisMapList), c_char, String]
        break

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 227
for _lib in _libs.values():
    if hasattr(_lib, 'tgis_unregister_maps'):
        tgis_unregister_maps = _lib.tgis_unregister_maps
        tgis_unregister_maps.restype = c_int
        tgis_unregister_maps.argtypes = [POINTER(tgisMapList), c_char, String]
        break

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 230
for _lib in _libs.values():
    if hasattr(_lib, 'tgis_get_registered_maps'):
        tgis_get_registered_maps = _lib.tgis_get_registered_maps
        tgis_get_registered_maps.restype = POINTER(tgisDatasetList)
        tgis_get_registered_maps.argtypes = [String, String, c_char, String, String]
        break

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 236
for _lib in _libs.values():
    if hasattr(_lib, 'tgis_get_registered_stds'):
        tgis_get_registered_stds = _lib.tgis_get_registered_stds
        tgis_get_registered_stds.restype = POINTER(tgisDatasetList)
        tgis_get_registered_stds.argtypes = [String, String, c_char, c_char, String, String]
        break

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 241
for _lib in _libs.values():
    if hasattr(_lib, 'tgis_get_stds_info'):
        tgis_get_stds_info = _lib.tgis_get_stds_info
        tgis_get_stds_info.restype = POINTER(tgisDataset)
        tgis_get_stds_info.argtypes = [String, String, c_char]
        break

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 9
try:
    TGISDB_DEFAULT_DRIVER = 'sqlite'
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 10
try:
    TGISDB_DEFAULT_SQLITE_PATH = 'tgis/sqlite.db'
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 31
try:
    TGIS_TYPE_MAP = 0
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 31
try:
    TGIS_TYPE_STDS = 1
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 32
try:
    TGIS_RASTER_MAP = 1
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 32
try:
    TGIS_RASTER3D_MAP = 2
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 32
try:
    TGIS_VECTOR_MAP = 3
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 32
try:
    TGIS_STRDS = 4
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 32
try:
    TGIS_STVDS = 6
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 33
try:
    TGIS_ABSOLUTE_TIME = 0
except:
    pass

# /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 33
try:
    TGIS_RELATIVE_TIME = 1
except:
    pass

_tgisMap = struct__tgisMap # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 49

_tgisMapList = struct__tgisMapList # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 71

_tgisExtent = struct__tgisExtent # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 103

_tgisDataset = struct__tgisDataset # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 133

_tgisDatasetList = struct__tgisDatasetList # /usr/src/grass-7.0.4/dist.x86_64-pc-linux-gnu/include/grass/temporal.h: 128

# No inserted files
