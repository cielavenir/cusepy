# generated by 'xml2py'
# flags '-c -d -v /tmp/tmpzom1aE -o /home/vagrant/cusepy/cuse/cuse_api.py -l fuse -r ^FUSE_SET_.* -r ^XATTR_.* -r fuse_reply_.* -r cuse_.* -r CUSE_.* -r fuse_chan.* -s fuse_set_signal_handlers -s fuse_session_add_chan -s fuse_session_loop_mt -s fuse_session_remove_chan -s fuse_remove_signal_handlers -s fuse_session_destroy -s fuse_req_ctx -s fuse_session_loop -s ENOATTR -s ENOTSUP -s fuse_version -s fuse_kern_chan_new -s fuse_lowlevel_notify_poll -s fuse_pollhandle_destroy'
from ctypes import *

_libraries = {}
_libraries['libfuse.so.2'] = CDLL('libfuse.so.2')


EOPNOTSUPP = 95 # Variable c_int '95'
ENOTSUP = EOPNOTSUPP # alias
ENODATA = 61 # Variable c_int '61'
ENOATTR = ENODATA # alias
FUSE_SET_ATTR_MODE = 1 # Variable c_int '1'
XATTR_REPLACE = 2 # Variable c_int '2'
FUSE_SET_ATTR_GID = 4 # Variable c_int '4'
FUSE_SET_ATTR_ATIME_NOW = 128 # Variable c_int '128'
FUSE_SET_ATTR_MTIME_NOW = 256 # Variable c_int '256'
FUSE_SET_ATTR_ATIME = 16 # Variable c_int '16'
FUSE_SET_ATTR_MTIME = 32 # Variable c_int '32'
XATTR_CREATE = 1 # Variable c_int '1'
FUSE_SET_ATTR_UID = 2 # Variable c_int '2'
CUSE_UNRESTRICTED_IOCTL = 1 # Variable c_int '1'
FUSE_SET_ATTR_SIZE = 8 # Variable c_int '8'
# /usr/include/fuse/cuse_lowlevel.h 33
class cuse_info(Structure):
    pass
cuse_info._fields_ = [
    # /usr/include/fuse/cuse_lowlevel.h 33
    ('dev_major', c_uint),
    ('dev_minor', c_uint),
    ('dev_info_argc', c_uint),
    ('dev_info_argv', POINTER(POINTER(c_char))),
    ('flags', c_uint),
]
# /usr/include/fuse/cuse_lowlevel.h 49
class cuse_lowlevel_ops(Structure):
    pass
# /usr/include/fuse/fuse_common.h 140
class fuse_conn_info(Structure):
    pass
# /usr/include/fuse/fuse_lowlevel.h 50
class fuse_req(Structure):
    pass
fuse_req_t = POINTER(fuse_req)
# /usr/include/fuse/fuse_common.h 45
class fuse_file_info(Structure):
    pass
size_t = c_ulong
__off64_t = c_long
off_t = __off64_t
# /usr/include/fuse/fuse_common.h 194
class fuse_pollhandle(Structure):
    pass
cuse_lowlevel_ops._fields_ = [
    # /usr/include/fuse/cuse_lowlevel.h 49
    ('init', CFUNCTYPE(None, c_void_p, POINTER(fuse_conn_info))),
    ('init_done', CFUNCTYPE(None, c_void_p)),
    ('destroy', CFUNCTYPE(None, c_void_p)),
    ('open', CFUNCTYPE(None, fuse_req_t, POINTER(fuse_file_info))),
    ('read', CFUNCTYPE(None, fuse_req_t, size_t, off_t, POINTER(fuse_file_info))),
    ('write', CFUNCTYPE(None, fuse_req_t, POINTER(c_char), size_t, off_t, POINTER(fuse_file_info))),
    ('flush', CFUNCTYPE(None, fuse_req_t, POINTER(fuse_file_info))),
    ('release', CFUNCTYPE(None, fuse_req_t, POINTER(fuse_file_info))),
    ('fsync', CFUNCTYPE(None, fuse_req_t, c_int, POINTER(fuse_file_info))),
    ('ioctl', CFUNCTYPE(None, fuse_req_t, c_int, c_void_p, POINTER(fuse_file_info), c_uint, c_void_p, size_t, size_t)),
    ('poll', CFUNCTYPE(None, fuse_req_t, POINTER(fuse_file_info), POINTER(fuse_pollhandle))),
]
# /usr/include/fuse/fuse_common.h 192
class fuse_session(Structure):
    pass
# /usr/include/fuse/fuse_opt.h 108
class fuse_args(Structure):
    pass
# /usr/include/fuse/cuse_lowlevel.h 71
cuse_lowlevel_new = _libraries['libfuse.so.2'].cuse_lowlevel_new
cuse_lowlevel_new.restype = POINTER(fuse_session)
# cuse_lowlevel_new(args, ci, clop, userdata)
cuse_lowlevel_new.argtypes = [POINTER(fuse_args), POINTER(cuse_info), POINTER(cuse_lowlevel_ops), c_void_p]
cuse_lowlevel_new.__doc__ = \
"""fuse_session * cuse_lowlevel_new(fuse_args * args, unknown * ci, unknown * clop, void * userdata)
/usr/include/fuse/cuse_lowlevel.h:71"""
# /usr/include/fuse/cuse_lowlevel.h 76
cuse_lowlevel_setup = _libraries['libfuse.so.2'].cuse_lowlevel_setup
cuse_lowlevel_setup.restype = POINTER(fuse_session)
# cuse_lowlevel_setup(argc, argv, ci, clop, multithreaded, userdata)
cuse_lowlevel_setup.argtypes = [c_int, POINTER(POINTER(c_char)), POINTER(cuse_info), POINTER(cuse_lowlevel_ops), POINTER(c_int), c_void_p]
cuse_lowlevel_setup.__doc__ = \
"""fuse_session * cuse_lowlevel_setup(int argc, char * * argv, unknown * ci, unknown * clop, int * multithreaded, void * userdata)
/usr/include/fuse/cuse_lowlevel.h:76"""
# /usr/include/fuse/cuse_lowlevel.h 78
cuse_lowlevel_teardown = _libraries['libfuse.so.2'].cuse_lowlevel_teardown
cuse_lowlevel_teardown.restype = None
# cuse_lowlevel_teardown(se)
cuse_lowlevel_teardown.argtypes = [POINTER(fuse_session)]
cuse_lowlevel_teardown.__doc__ = \
"""void cuse_lowlevel_teardown(fuse_session * se)
/usr/include/fuse/cuse_lowlevel.h:78"""
# /usr/include/fuse/cuse_lowlevel.h 81
cuse_lowlevel_main = _libraries['libfuse.so.2'].cuse_lowlevel_main
cuse_lowlevel_main.restype = c_int
# cuse_lowlevel_main(argc, argv, ci, clop, userdata)
cuse_lowlevel_main.argtypes = [c_int, POINTER(POINTER(c_char)), POINTER(cuse_info), POINTER(cuse_lowlevel_ops), c_void_p]
cuse_lowlevel_main.__doc__ = \
"""int cuse_lowlevel_main(int argc, char * * argv, unknown * ci, unknown * clop, void * userdata)
/usr/include/fuse/cuse_lowlevel.h:81"""
# /usr/include/fuse/fuse_common.h 193
class fuse_chan(Structure):
    pass
fuse_chan._fields_ = [
    # /usr/include/fuse/fuse_common.h 193
]
# /usr/include/fuse/fuse_common.h 253
fuse_version = _libraries['libfuse.so.2'].fuse_version
fuse_version.restype = c_int
# fuse_version()
fuse_version.argtypes = []
fuse_version.__doc__ = \
"""int fuse_version()
/usr/include/fuse/fuse_common.h:253"""
# /usr/include/fuse/fuse_common.h 260
fuse_pollhandle_destroy = _libraries['libfuse.so.2'].fuse_pollhandle_destroy
fuse_pollhandle_destroy.restype = None
# fuse_pollhandle_destroy(ph)
fuse_pollhandle_destroy.argtypes = [POINTER(fuse_pollhandle)]
fuse_pollhandle_destroy.__doc__ = \
"""void fuse_pollhandle_destroy(fuse_pollhandle * ph)
/usr/include/fuse/fuse_common.h:260"""
# /usr/include/fuse/fuse_common.h 455
fuse_set_signal_handlers = _libraries['libfuse.so.2'].fuse_set_signal_handlers
fuse_set_signal_handlers.restype = c_int
# fuse_set_signal_handlers(se)
fuse_set_signal_handlers.argtypes = [POINTER(fuse_session)]
fuse_set_signal_handlers.__doc__ = \
"""int fuse_set_signal_handlers(fuse_session * se)
/usr/include/fuse/fuse_common.h:455"""
# /usr/include/fuse/fuse_common.h 465
fuse_remove_signal_handlers = _libraries['libfuse.so.2'].fuse_remove_signal_handlers
fuse_remove_signal_handlers.restype = None
# fuse_remove_signal_handlers(se)
fuse_remove_signal_handlers.argtypes = [POINTER(fuse_session)]
fuse_remove_signal_handlers.__doc__ = \
"""void fuse_remove_signal_handlers(fuse_session * se)
/usr/include/fuse/fuse_common.h:465"""
# /usr/include/fuse/fuse_lowlevel.h 1034
fuse_reply_err = _libraries['libfuse.so.2'].fuse_reply_err
fuse_reply_err.restype = c_int
# fuse_reply_err(req, err)
fuse_reply_err.argtypes = [fuse_req_t, c_int]
fuse_reply_err.__doc__ = \
"""int fuse_reply_err(fuse_req_t req, int err)
/usr/include/fuse/fuse_lowlevel.h:1034"""
# /usr/include/fuse/fuse_lowlevel.h 1044
fuse_reply_none = _libraries['libfuse.so.2'].fuse_reply_none
fuse_reply_none.restype = None
# fuse_reply_none(req)
fuse_reply_none.argtypes = [fuse_req_t]
fuse_reply_none.__doc__ = \
"""void fuse_reply_none(fuse_req_t req)
/usr/include/fuse/fuse_lowlevel.h:1044"""
# /usr/include/fuse/fuse_lowlevel.h 68
class fuse_entry_param(Structure):
    pass
fuse_ino_t = c_ulong
# /usr/include/x86_64-linux-gnu/bits/stat.h 47
class stat(Structure):
    pass
__dev_t = c_ulong
__ino_t = c_ulong
__nlink_t = c_ulong
__mode_t = c_uint
__uid_t = c_uint
__gid_t = c_uint
__off_t = c_long
__blksize_t = c_long
__blkcnt_t = c_long
# /usr/include/time.h 121
class timespec(Structure):
    pass
__time_t = c_long
__syscall_slong_t = c_long
timespec._fields_ = [
    # /usr/include/time.h 121
    ('tv_sec', __time_t),
    ('tv_nsec', __syscall_slong_t),
]
stat._fields_ = [
    # /usr/include/x86_64-linux-gnu/bits/stat.h 47
    ('st_dev', __dev_t),
    ('st_ino', __ino_t),
    ('st_nlink', __nlink_t),
    ('st_mode', __mode_t),
    ('st_uid', __uid_t),
    ('st_gid', __gid_t),
    ('__pad0', c_int),
    ('st_rdev', __dev_t),
    ('st_size', __off_t),
    ('st_blksize', __blksize_t),
    ('st_blocks', __blkcnt_t),
    ('st_atim', timespec),
    ('st_mtim', timespec),
    ('st_ctim', timespec),
    ('__glibc_reserved', __syscall_slong_t * 3),
]
fuse_entry_param._fields_ = [
    # /usr/include/fuse/fuse_lowlevel.h 68
    ('ino', fuse_ino_t),
    ('generation', c_ulong),
    ('attr', stat),
    ('attr_timeout', c_double),
    ('entry_timeout', c_double),
]
# /usr/include/fuse/fuse_lowlevel.h 1059
fuse_reply_entry = _libraries['libfuse.so.2'].fuse_reply_entry
fuse_reply_entry.restype = c_int
# fuse_reply_entry(req, e)
fuse_reply_entry.argtypes = [fuse_req_t, POINTER(fuse_entry_param)]
fuse_reply_entry.__doc__ = \
"""int fuse_reply_entry(fuse_req_t req, unknown * e)
/usr/include/fuse/fuse_lowlevel.h:1059"""
uint64_t = c_uint64
fuse_file_info._fields_ = [
    # /usr/include/fuse/fuse_common.h 45
    ('flags', c_int),
    ('fh_old', c_ulong),
    ('writepage', c_int),
    ('direct_io', c_uint, 1),
    ('keep_cache', c_uint, 1),
    ('flush', c_uint, 1),
    ('nonseekable', c_uint, 1),
    ('flock_release', c_uint, 1),
    ('padding', c_uint, 27),
    ('fh', uint64_t),
    ('lock_owner', uint64_t),
]
# /usr/include/fuse/fuse_lowlevel.h 1079
fuse_reply_create = _libraries['libfuse.so.2'].fuse_reply_create
fuse_reply_create.restype = c_int
# fuse_reply_create(req, e, fi)
fuse_reply_create.argtypes = [fuse_req_t, POINTER(fuse_entry_param), POINTER(fuse_file_info)]
fuse_reply_create.__doc__ = \
"""int fuse_reply_create(fuse_req_t req, unknown * e, unknown * fi)
/usr/include/fuse/fuse_lowlevel.h:1079"""
# /usr/include/fuse/fuse_lowlevel.h 1093
fuse_reply_attr = _libraries['libfuse.so.2'].fuse_reply_attr
fuse_reply_attr.restype = c_int
# fuse_reply_attr(req, attr, attr_timeout)
fuse_reply_attr.argtypes = [fuse_req_t, POINTER(stat), c_double]
fuse_reply_attr.__doc__ = \
"""int fuse_reply_attr(fuse_req_t req, unknown * attr, double attr_timeout)
/usr/include/fuse/fuse_lowlevel.h:1093"""
# /usr/include/fuse/fuse_lowlevel.h 1105
fuse_reply_readlink = _libraries['libfuse.so.2'].fuse_reply_readlink
fuse_reply_readlink.restype = c_int
# fuse_reply_readlink(req, link)
fuse_reply_readlink.argtypes = [fuse_req_t, POINTER(c_char)]
fuse_reply_readlink.__doc__ = \
"""int fuse_reply_readlink(fuse_req_t req, unknown * link)
/usr/include/fuse/fuse_lowlevel.h:1105"""
# /usr/include/fuse/fuse_lowlevel.h 1120
fuse_reply_open = _libraries['libfuse.so.2'].fuse_reply_open
fuse_reply_open.restype = c_int
# fuse_reply_open(req, fi)
fuse_reply_open.argtypes = [fuse_req_t, POINTER(fuse_file_info)]
fuse_reply_open.__doc__ = \
"""int fuse_reply_open(fuse_req_t req, unknown * fi)
/usr/include/fuse/fuse_lowlevel.h:1120"""
# /usr/include/fuse/fuse_lowlevel.h 1132
fuse_reply_write = _libraries['libfuse.so.2'].fuse_reply_write
fuse_reply_write.restype = c_int
# fuse_reply_write(req, count)
fuse_reply_write.argtypes = [fuse_req_t, size_t]
fuse_reply_write.__doc__ = \
"""int fuse_reply_write(fuse_req_t req, size_t count)
/usr/include/fuse/fuse_lowlevel.h:1132"""
# /usr/include/fuse/fuse_lowlevel.h 1145
fuse_reply_buf = _libraries['libfuse.so.2'].fuse_reply_buf
fuse_reply_buf.restype = c_int
# fuse_reply_buf(req, buf, size)
fuse_reply_buf.argtypes = [fuse_req_t, POINTER(c_char), size_t]
fuse_reply_buf.__doc__ = \
"""int fuse_reply_buf(fuse_req_t req, unknown * buf, size_t size)
/usr/include/fuse/fuse_lowlevel.h:1145"""
# /usr/include/fuse/fuse_common.h 386
class fuse_bufvec(Structure):
    pass

# values for enumeration 'fuse_buf_copy_flags'
FUSE_BUF_NO_SPLICE = 2
FUSE_BUF_FORCE_SPLICE = 4
FUSE_BUF_SPLICE_MOVE = 8
FUSE_BUF_SPLICE_NONBLOCK = 16
fuse_buf_copy_flags = c_int # enum
# /usr/include/fuse/fuse_lowlevel.h 1159
fuse_reply_data = _libraries['libfuse.so.2'].fuse_reply_data
fuse_reply_data.restype = c_int
# fuse_reply_data(req, bufv, flags)
fuse_reply_data.argtypes = [fuse_req_t, POINTER(fuse_bufvec), fuse_buf_copy_flags]
fuse_reply_data.__doc__ = \
"""int fuse_reply_data(fuse_req_t req, fuse_bufvec * bufv, fuse_buf_copy_flags flags)
/usr/include/fuse/fuse_lowlevel.h:1159"""
# /usr/include/x86_64-linux-gnu/bits/uio.h 44
class iovec(Structure):
    pass
iovec._fields_ = [
    # /usr/include/x86_64-linux-gnu/bits/uio.h 44
    ('iov_base', c_void_p),
    ('iov_len', size_t),
]
# /usr/include/fuse/fuse_lowlevel.h 1172
fuse_reply_iov = _libraries['libfuse.so.2'].fuse_reply_iov
fuse_reply_iov.restype = c_int
# fuse_reply_iov(req, iov, count)
fuse_reply_iov.argtypes = [fuse_req_t, POINTER(iovec), c_int]
fuse_reply_iov.__doc__ = \
"""int fuse_reply_iov(fuse_req_t req, unknown * iov, int count)
/usr/include/fuse/fuse_lowlevel.h:1172"""
# /usr/include/x86_64-linux-gnu/bits/statvfs.h 30
class statvfs(Structure):
    pass
__fsblkcnt64_t = c_ulong
__fsfilcnt64_t = c_ulong
statvfs._fields_ = [
    # /usr/include/x86_64-linux-gnu/bits/statvfs.h 30
    ('f_bsize', c_ulong),
    ('f_frsize', c_ulong),
    ('f_blocks', __fsblkcnt64_t),
    ('f_bfree', __fsblkcnt64_t),
    ('f_bavail', __fsblkcnt64_t),
    ('f_files', __fsfilcnt64_t),
    ('f_ffree', __fsfilcnt64_t),
    ('f_favail', __fsfilcnt64_t),
    ('f_fsid', c_ulong),
    ('f_flag', c_ulong),
    ('f_namemax', c_ulong),
    ('__f_spare', c_int * 6),
]
# /usr/include/fuse/fuse_lowlevel.h 1184
fuse_reply_statfs = _libraries['libfuse.so.2'].fuse_reply_statfs
fuse_reply_statfs.restype = c_int
# fuse_reply_statfs(req, stbuf)
fuse_reply_statfs.argtypes = [fuse_req_t, POINTER(statvfs)]
fuse_reply_statfs.__doc__ = \
"""int fuse_reply_statfs(fuse_req_t req, unknown * stbuf)
/usr/include/fuse/fuse_lowlevel.h:1184"""
# /usr/include/fuse/fuse_lowlevel.h 1196
fuse_reply_xattr = _libraries['libfuse.so.2'].fuse_reply_xattr
fuse_reply_xattr.restype = c_int
# fuse_reply_xattr(req, count)
fuse_reply_xattr.argtypes = [fuse_req_t, size_t]
fuse_reply_xattr.__doc__ = \
"""int fuse_reply_xattr(fuse_req_t req, size_t count)
/usr/include/fuse/fuse_lowlevel.h:1196"""
# /usr/include/x86_64-linux-gnu/bits/fcntl.h 36
class flock(Structure):
    pass
__pid_t = c_int
flock._fields_ = [
    # /usr/include/x86_64-linux-gnu/bits/fcntl.h 36
    ('l_type', c_short),
    ('l_whence', c_short),
    ('l_start', __off64_t),
    ('l_len', __off64_t),
    ('l_pid', __pid_t),
]
# /usr/include/fuse/fuse_lowlevel.h 1208
fuse_reply_lock = _libraries['libfuse.so.2'].fuse_reply_lock
fuse_reply_lock.restype = c_int
# fuse_reply_lock(req, lock)
fuse_reply_lock.argtypes = [fuse_req_t, POINTER(flock)]
fuse_reply_lock.__doc__ = \
"""int fuse_reply_lock(fuse_req_t req, unknown * lock)
/usr/include/fuse/fuse_lowlevel.h:1208"""
# /usr/include/fuse/fuse_lowlevel.h 1220
fuse_reply_bmap = _libraries['libfuse.so.2'].fuse_reply_bmap
fuse_reply_bmap.restype = c_int
# fuse_reply_bmap(req, idx)
fuse_reply_bmap.argtypes = [fuse_req_t, uint64_t]
fuse_reply_bmap.__doc__ = \
"""int fuse_reply_bmap(fuse_req_t req, uint64_t idx)
/usr/include/fuse/fuse_lowlevel.h:1220"""
# /usr/include/fuse/fuse_lowlevel.h 1271
fuse_reply_ioctl_retry = _libraries['libfuse.so.2'].fuse_reply_ioctl_retry
fuse_reply_ioctl_retry.restype = c_int
# fuse_reply_ioctl_retry(req, in_iov, in_count, out_iov, out_count)
fuse_reply_ioctl_retry.argtypes = [fuse_req_t, POINTER(iovec), size_t, POINTER(iovec), size_t]
fuse_reply_ioctl_retry.__doc__ = \
"""int fuse_reply_ioctl_retry(fuse_req_t req, unknown * in_iov, size_t in_count, unknown * out_iov, size_t out_count)
/usr/include/fuse/fuse_lowlevel.h:1271"""
# /usr/include/fuse/fuse_lowlevel.h 1284
fuse_reply_ioctl = _libraries['libfuse.so.2'].fuse_reply_ioctl
fuse_reply_ioctl.restype = c_int
# fuse_reply_ioctl(req, result, buf, size)
fuse_reply_ioctl.argtypes = [fuse_req_t, c_int, c_void_p, size_t]
fuse_reply_ioctl.__doc__ = \
"""int fuse_reply_ioctl(fuse_req_t req, int result, unknown * buf, size_t size)
/usr/include/fuse/fuse_lowlevel.h:1284"""
# /usr/include/fuse/fuse_lowlevel.h 1298
fuse_reply_ioctl_iov = _libraries['libfuse.so.2'].fuse_reply_ioctl_iov
fuse_reply_ioctl_iov.restype = c_int
# fuse_reply_ioctl_iov(req, result, iov, count)
fuse_reply_ioctl_iov.argtypes = [fuse_req_t, c_int, POINTER(iovec), c_int]
fuse_reply_ioctl_iov.__doc__ = \
"""int fuse_reply_ioctl_iov(fuse_req_t req, int result, unknown * iov, int count)
/usr/include/fuse/fuse_lowlevel.h:1298"""
# /usr/include/fuse/fuse_lowlevel.h 1306
fuse_reply_poll = _libraries['libfuse.so.2'].fuse_reply_poll
fuse_reply_poll.restype = c_int
# fuse_reply_poll(req, revents)
fuse_reply_poll.argtypes = [fuse_req_t, c_uint]
fuse_reply_poll.__doc__ = \
"""int fuse_reply_poll(fuse_req_t req, unsigned int revents)
/usr/include/fuse/fuse_lowlevel.h:1306"""
# /usr/include/fuse/fuse_lowlevel.h 1319
fuse_lowlevel_notify_poll = _libraries['libfuse.so.2'].fuse_lowlevel_notify_poll
fuse_lowlevel_notify_poll.restype = c_int
# fuse_lowlevel_notify_poll(ph)
fuse_lowlevel_notify_poll.argtypes = [POINTER(fuse_pollhandle)]
fuse_lowlevel_notify_poll.__doc__ = \
"""int fuse_lowlevel_notify_poll(fuse_pollhandle * ph)
/usr/include/fuse/fuse_lowlevel.h:1319"""
# /usr/include/fuse/fuse_lowlevel.h 110
class fuse_ctx(Structure):
    pass
uid_t = __uid_t
gid_t = __gid_t
pid_t = __pid_t
mode_t = __mode_t
fuse_ctx._fields_ = [
    # /usr/include/fuse/fuse_lowlevel.h 110
    ('uid', uid_t),
    ('gid', gid_t),
    ('pid', pid_t),
    ('umask', mode_t),
]
# /usr/include/fuse/fuse_lowlevel.h 1445
fuse_req_ctx = _libraries['libfuse.so.2'].fuse_req_ctx
fuse_req_ctx.restype = POINTER(fuse_ctx)
# fuse_req_ctx(req)
fuse_req_ctx.argtypes = [fuse_req_t]
fuse_req_ctx.__doc__ = \
"""unknown * fuse_req_ctx(fuse_req_t req)
/usr/include/fuse/fuse_lowlevel.h:1445"""
# /usr/include/fuse/fuse_lowlevel.h 1583
fuse_session_add_chan = _libraries['libfuse.so.2'].fuse_session_add_chan
fuse_session_add_chan.restype = None
# fuse_session_add_chan(se, ch)
fuse_session_add_chan.argtypes = [POINTER(fuse_session), POINTER(fuse_chan)]
fuse_session_add_chan.__doc__ = \
"""void fuse_session_add_chan(fuse_session * se, fuse_chan * ch)
/usr/include/fuse/fuse_lowlevel.h:1583"""
# /usr/include/fuse/fuse_lowlevel.h 1592
fuse_session_remove_chan = _libraries['libfuse.so.2'].fuse_session_remove_chan
fuse_session_remove_chan.restype = None
# fuse_session_remove_chan(ch)
fuse_session_remove_chan.argtypes = [POINTER(fuse_chan)]
fuse_session_remove_chan.__doc__ = \
"""void fuse_session_remove_chan(fuse_chan * ch)
/usr/include/fuse/fuse_lowlevel.h:1592"""
# /usr/include/fuse/fuse_lowlevel.h 1652
fuse_session_destroy = _libraries['libfuse.so.2'].fuse_session_destroy
fuse_session_destroy.restype = None
# fuse_session_destroy(se)
fuse_session_destroy.argtypes = [POINTER(fuse_session)]
fuse_session_destroy.__doc__ = \
"""void fuse_session_destroy(fuse_session * se)
/usr/include/fuse/fuse_lowlevel.h:1652"""
# /usr/include/fuse/fuse_lowlevel.h 1652
fuse_session_exit = _libraries['libfuse.so.2'].fuse_session_exit
fuse_session_exit.restype = None
# fuse_session_exit(se)
fuse_session_exit.argtypes = [POINTER(fuse_session)]
fuse_session_exit.__doc__ = \
"""void fuse_session_exit(fuse_session * se)
/usr/include/fuse/fuse_lowlevel.h:1652"""
fuse_session_exited = _libraries['libfuse.so.2'].fuse_session_exited
fuse_session_exited.restype = c_int
# fuse_session_exited(se)
fuse_session_exited.argtypes = [POINTER(fuse_session)]
fuse_session_exited.__doc__ = \
"""int fuse_session_exited(fuse_session * se)
/usr/include/fuse/fuse_lowlevel.h:1652"""
# /usr/include/fuse/fuse_lowlevel.h 1690
fuse_session_loop = _libraries['libfuse.so.2'].fuse_session_loop
fuse_session_loop.restype = c_int
# fuse_session_loop(se)
fuse_session_loop.argtypes = [POINTER(fuse_session)]
fuse_session_loop.__doc__ = \
"""int fuse_session_loop(fuse_session * se)
/usr/include/fuse/fuse_lowlevel.h:1690"""
# /usr/include/fuse/fuse_lowlevel.h 1698
fuse_session_loop_mt = _libraries['libfuse.so.2'].fuse_session_loop_mt
fuse_session_loop_mt.restype = c_int
# fuse_session_loop_mt(se)
fuse_session_loop_mt.argtypes = [POINTER(fuse_session)]
fuse_session_loop_mt.__doc__ = \
"""int fuse_session_loop_mt(fuse_session * se)
/usr/include/fuse/fuse_lowlevel.h:1698"""
# /usr/include/fuse/fuse_lowlevel.h 1709
class fuse_chan_ops(Structure):
    pass
fuse_chan_ops._fields_ = [
    # /usr/include/fuse/fuse_lowlevel.h 1709
    ('receive', CFUNCTYPE(c_int, POINTER(POINTER(fuse_chan)), POINTER(c_char), size_t)),
    ('send', CFUNCTYPE(c_int, POINTER(fuse_chan), POINTER(iovec), size_t)),
    ('destroy', CFUNCTYPE(None, POINTER(fuse_chan))),
]
# /usr/include/fuse/fuse_lowlevel.h 1752
fuse_chan_new = _libraries['libfuse.so.2'].fuse_chan_new
fuse_chan_new.restype = POINTER(fuse_chan)
# fuse_chan_new(op, fd, bufsize, data)
fuse_chan_new.argtypes = [POINTER(fuse_chan_ops), c_int, size_t, c_void_p]
fuse_chan_new.__doc__ = \
"""fuse_chan * fuse_chan_new(fuse_chan_ops * op, int fd, size_t bufsize, void * data)
/usr/include/fuse/fuse_lowlevel.h:1752"""
# /usr/include/fuse/fuse_lowlevel.h 1760
fuse_chan_fd = _libraries['libfuse.so.2'].fuse_chan_fd
fuse_chan_fd.restype = c_int
# fuse_chan_fd(ch)
fuse_chan_fd.argtypes = [POINTER(fuse_chan)]
fuse_chan_fd.__doc__ = \
"""int fuse_chan_fd(fuse_chan * ch)
/usr/include/fuse/fuse_lowlevel.h:1760"""
# /usr/include/fuse/fuse_lowlevel.h 1768
fuse_chan_bufsize = _libraries['libfuse.so.2'].fuse_chan_bufsize
fuse_chan_bufsize.restype = size_t
# fuse_chan_bufsize(ch)
fuse_chan_bufsize.argtypes = [POINTER(fuse_chan)]
fuse_chan_bufsize.__doc__ = \
"""size_t fuse_chan_bufsize(fuse_chan * ch)
/usr/include/fuse/fuse_lowlevel.h:1768"""
# /usr/include/fuse/fuse_lowlevel.h 1776
fuse_chan_data = _libraries['libfuse.so.2'].fuse_chan_data
fuse_chan_data.restype = c_void_p
# fuse_chan_data(ch)
fuse_chan_data.argtypes = [POINTER(fuse_chan)]
fuse_chan_data.__doc__ = \
"""void * fuse_chan_data(fuse_chan * ch)
/usr/include/fuse/fuse_lowlevel.h:1776"""
# /usr/include/fuse/fuse_lowlevel.h 1784
fuse_chan_session = _libraries['libfuse.so.2'].fuse_chan_session
fuse_chan_session.restype = POINTER(fuse_session)
# fuse_chan_session(ch)
fuse_chan_session.argtypes = [POINTER(fuse_chan)]
fuse_chan_session.__doc__ = \
"""fuse_session * fuse_chan_session(fuse_chan * ch)
/usr/include/fuse/fuse_lowlevel.h:1784"""
# /usr/include/fuse/fuse_lowlevel.h 1796
fuse_chan_recv = _libraries['libfuse.so.2'].fuse_chan_recv
fuse_chan_recv.restype = c_int
# fuse_chan_recv(ch, buf, size)
fuse_chan_recv.argtypes = [POINTER(POINTER(fuse_chan)), POINTER(c_char), size_t]
fuse_chan_recv.__doc__ = \
"""int fuse_chan_recv(fuse_chan * * ch, char * buf, size_t size)
/usr/include/fuse/fuse_lowlevel.h:1796"""
# /usr/include/fuse/fuse_lowlevel.h 1810
fuse_chan_send = _libraries['libfuse.so.2'].fuse_chan_send
fuse_chan_send.restype = c_int
# fuse_chan_send(ch, iov, count)
fuse_chan_send.argtypes = [POINTER(fuse_chan), POINTER(iovec), size_t]
fuse_chan_send.__doc__ = \
"""int fuse_chan_send(fuse_chan * ch, unknown * iov, size_t count)
/usr/include/fuse/fuse_lowlevel.h:1810"""
# /usr/include/fuse/fuse_lowlevel.h 1817
fuse_chan_destroy = _libraries['libfuse.so.2'].fuse_chan_destroy
fuse_chan_destroy.restype = None
# fuse_chan_destroy(ch)
fuse_chan_destroy.argtypes = [POINTER(fuse_chan)]
fuse_chan_destroy.__doc__ = \
"""void fuse_chan_destroy(fuse_chan * ch)
/usr/include/fuse/fuse_lowlevel.h:1817"""
# /usr/include/x86_64-linux-gnu/bits/statfs.h 25
class statfs(Structure):
    pass
__fsword_t = c_long
# /usr/include/x86_64-linux-gnu/bits/types.h 134
class __fsid_t(Structure):
    pass
__fsid_t._fields_ = [
    # /usr/include/x86_64-linux-gnu/bits/types.h 134
    ('__val', c_int * 2),
]
statfs._fields_ = [
    # /usr/include/x86_64-linux-gnu/bits/statfs.h 25
    ('f_type', __fsword_t),
    ('f_bsize', __fsword_t),
    ('f_blocks', __fsblkcnt64_t),
    ('f_bfree', __fsblkcnt64_t),
    ('f_bavail', __fsblkcnt64_t),
    ('f_files', __fsfilcnt64_t),
    ('f_ffree', __fsfilcnt64_t),
    ('f_fsid', __fsid_t),
    ('f_namelen', __fsword_t),
    ('f_frsize', __fsword_t),
    ('f_flags', __fsword_t),
    ('f_spare', __fsword_t * 4),
]
# /usr/include/fuse/fuse_lowlevel_compat.h 133
fuse_reply_statfs_compat = _libraries['libfuse.so.2'].fuse_reply_statfs_compat
fuse_reply_statfs_compat.restype = c_int
# fuse_reply_statfs_compat(req, stbuf)
fuse_reply_statfs_compat.argtypes = [fuse_req_t, POINTER(statfs)]
fuse_reply_statfs_compat.__doc__ = \
"""int fuse_reply_statfs_compat(fuse_req_t req, unknown * stbuf)
/usr/include/fuse/fuse_lowlevel_compat.h:133"""
# /usr/include/fuse/fuse_lowlevel_compat.h 85
class fuse_file_info_compat(Structure):
    pass
fuse_file_info_compat._fields_ = [
    # /usr/include/fuse/fuse_lowlevel_compat.h 85
]
# /usr/include/fuse/fuse_lowlevel_compat.h 136
fuse_reply_open_compat = _libraries['libfuse.so.2'].fuse_reply_open_compat
fuse_reply_open_compat.restype = c_int
# fuse_reply_open_compat(req, fi)
fuse_reply_open_compat.argtypes = [fuse_req_t, POINTER(fuse_file_info_compat)]
fuse_reply_open_compat.__doc__ = \
"""int fuse_reply_open_compat(fuse_req_t req, unknown * fi)
/usr/include/fuse/fuse_lowlevel_compat.h:136"""
# /usr/include/fuse/fuse_lowlevel_compat.h 144
class fuse_chan_ops_compat24(Structure):
    pass
fuse_chan_ops_compat24._fields_ = [
    # /usr/include/fuse/fuse_lowlevel_compat.h 144
    ('receive', CFUNCTYPE(c_int, POINTER(fuse_chan), POINTER(c_char), size_t)),
    ('send', CFUNCTYPE(c_int, POINTER(fuse_chan), POINTER(iovec), size_t)),
    ('destroy', CFUNCTYPE(None, POINTER(fuse_chan))),
]
# /usr/include/fuse/fuse_lowlevel_compat.h 152
fuse_chan_new_compat24 = _libraries['libfuse.so.2'].fuse_chan_new_compat24
fuse_chan_new_compat24.restype = POINTER(fuse_chan)
# fuse_chan_new_compat24(op, fd, bufsize, data)
fuse_chan_new_compat24.argtypes = [POINTER(fuse_chan_ops_compat24), c_int, size_t, c_void_p]
fuse_chan_new_compat24.__doc__ = \
"""fuse_chan * fuse_chan_new_compat24(fuse_chan_ops_compat24 * op, int fd, size_t bufsize, void * data)
/usr/include/fuse/fuse_lowlevel_compat.h:152"""
# /usr/include/fuse/fuse_lowlevel_compat.h 154
fuse_chan_receive = _libraries['libfuse.so.2'].fuse_chan_receive
fuse_chan_receive.restype = c_int
# fuse_chan_receive(ch, buf, size)
fuse_chan_receive.argtypes = [POINTER(fuse_chan), POINTER(c_char), size_t]
fuse_chan_receive.__doc__ = \
"""int fuse_chan_receive(fuse_chan * ch, char * buf, size_t size)
/usr/include/fuse/fuse_lowlevel_compat.h:154"""
# /usr/include/fuse/fuse_lowlevel_compat.h 155
fuse_kern_chan_new = _libraries['libfuse.so.2'].fuse_kern_chan_new
fuse_kern_chan_new.restype = POINTER(fuse_chan)
# fuse_kern_chan_new(fd)
fuse_kern_chan_new.argtypes = [c_int]
fuse_kern_chan_new.__doc__ = \
"""fuse_chan * fuse_kern_chan_new(int fd)
/usr/include/fuse/fuse_lowlevel_compat.h:155"""
fuse_conn_info._fields_ = [
    # /usr/include/fuse/fuse_common.h 140
    ('proto_major', c_uint),
    ('proto_minor', c_uint),
    ('async_read', c_uint),
    ('max_write', c_uint),
    ('max_readahead', c_uint),
    ('capable', c_uint),
    ('want', c_uint),
    ('max_background', c_uint),
    ('congestion_threshold', c_uint),
    ('reserved', c_uint * 23),
]
fuse_session._fields_ = [
    # /usr/include/fuse/fuse_common.h 192
]
fuse_pollhandle._fields_ = [
    # /usr/include/fuse/fuse_common.h 194
]
# /usr/include/fuse/fuse_common.h 345
class fuse_buf(Structure):
    pass

# values for enumeration 'fuse_buf_flags'
FUSE_BUF_IS_FD = 2
FUSE_BUF_FD_SEEK = 4
FUSE_BUF_FD_RETRY = 8
fuse_buf_flags = c_int # enum
fuse_buf._fields_ = [
    # /usr/include/fuse/fuse_common.h 345
    ('size', size_t),
    ('flags', fuse_buf_flags),
    ('mem', c_void_p),
    ('fd', c_int),
    ('pos', off_t),
]
fuse_bufvec._fields_ = [
    # /usr/include/fuse/fuse_common.h 386
    ('count', size_t),
    ('idx', size_t),
    ('off', size_t),
    ('buf', fuse_buf * 1),
]
fuse_req._fields_ = [
    # /usr/include/fuse/fuse_lowlevel.h 50
]
fuse_args._fields_ = [
    # /usr/include/fuse/fuse_opt.h 108
    ('argc', c_int),
    ('argv', POINTER(POINTER(c_char))),
    ('allocated', c_int),
]
__all__ = ['fuse_session_loop_mt', 'fuse_reply_iov', 'fuse_session',
           '__fsid_t', 'mode_t', '__off64_t', 'size_t',
           'fuse_session_remove_chan', 'FUSE_BUF_FD_SEEK',
           'fuse_chan_recv', 'fuse_chan_fd', 'cuse_lowlevel_new',
           'fuse_session_loop', '__syscall_slong_t',
           'FUSE_BUF_NO_SPLICE', 'FUSE_BUF_SPLICE_NONBLOCK',
           'fuse_entry_param', 'fuse_buf_flags', 'ENOTSUP',
           'cuse_info', 'fuse_reply_xattr', 'uid_t', 'fuse_chan_data',
           'cuse_lowlevel_teardown', 'fuse_chan_send',
           'fuse_pollhandle_destroy', '__time_t', 'ENOATTR',
           'FUSE_SET_ATTR_ATIME_NOW', 'fuse_reply_create',
           'EOPNOTSUPP', 'FUSE_SET_ATTR_MODE', 'statvfs',
           'fuse_chan_destroy', 'cuse_lowlevel_main', '__nlink_t',
           'FUSE_SET_ATTR_MTIME_NOW', 'cuse_lowlevel_setup',
           'timespec', '__fsword_t', 'fuse_reply_write',
           'cuse_lowlevel_ops', 'XATTR_REPLACE', 'flock',
           'fuse_chan_receive', 'fuse_chan_bufsize',
           'FUSE_SET_ATTR_ATIME', 'fuse_reply_data',
           'fuse_remove_signal_handlers', 'fuse_chan_session',
           'FUSE_SET_ATTR_MTIME', 'fuse_file_info_compat',
           'fuse_reply_buf', 'fuse_session_destroy', '__blkcnt_t',
           'XATTR_CREATE', 'fuse_req_t', 'fuse_lowlevel_notify_poll',
           'fuse_chan_new', 'fuse_conn_info', 'FUSE_BUF_SPLICE_MOVE',
           'fuse_reply_poll', '__mode_t', 'fuse_reply_none',
           'fuse_reply_err', 'fuse_ino_t', '__blksize_t', '__off_t',
           'FUSE_BUF_FORCE_SPLICE', 'fuse_reply_ioctl', '__gid_t',
           'fuse_reply_open', 'fuse_ctx', 'FUSE_SET_ATTR_GID',
           'fuse_args', 'fuse_file_info', 'fuse_req',
           'fuse_reply_statfs_compat', '__fsblkcnt64_t',
           'fuse_kern_chan_new', 'ENODATA', '__dev_t',
           'fuse_buf_copy_flags', 'FUSE_SET_ATTR_UID',
           'fuse_reply_entry', 'gid_t', 'pid_t', 'statfs',
           'CUSE_UNRESTRICTED_IOCTL', '__fsfilcnt64_t',
           'FUSE_SET_ATTR_SIZE', 'uint64_t', 'fuse_chan_ops',
           'fuse_reply_statfs', 'iovec', 'FUSE_BUF_FD_RETRY', 'off_t',
           'fuse_reply_readlink', 'fuse_reply_ioctl_iov',
           'fuse_reply_bmap', 'fuse_chan_new_compat24', 'fuse_bufvec',
           'fuse_pollhandle', 'fuse_reply_open_compat',
           'fuse_chan_ops_compat24', 'stat', '__pid_t',
           'fuse_reply_ioctl_retry', 'fuse_reply_lock',
           'FUSE_BUF_IS_FD', '__ino_t', 'fuse_session_add_chan',
           'fuse_version', 'fuse_reply_attr', 'fuse_chan',
           'fuse_set_signal_handlers', '__uid_t', 'fuse_buf',
           'fuse_req_ctx']
