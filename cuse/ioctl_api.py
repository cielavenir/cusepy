# generated by 'xml2py'
# flags '-c -d -v /tmp/tmplv2WR6 -o /home/vagrant/cusepy/cuse/ioctl_api.py'
from ctypes import *



FIONREAD = 21531 # Variable c_int '21531'
TIOCINQ = FIONREAD # alias
def __va_arg_pack(): return __builtin_va_arg_pack () # macro
def __bos(ptr): return __builtin_object_size (ptr, __USE_FORTIFY_LEVEL > 1) # macro
def __warnattr(msg): return __attribute__((__warning__ (msg))) # macro
# __wur = __attribute_warn_unused_result__ # alias
TIOCM_CAR = 64 # Variable c_int '64'
TIOCM_CD = TIOCM_CAR # alias
# __builtin_va_arg_pack = int # alias
def __attribute_format_strfmon__(a,b): return __attribute__ ((__format__ (__strfmon__, a, b))) # macro
CEOL = '\x00' # Variable c_char "'\\000'"
CBRK = CEOL # alias
# def __LDBL_REDIR_NTH(name,proto): return name proto __THROW # macro
# def __warndecl(name,msg): return extern void name (void) __attribute__((__warning__ (msg))) # macro
def __bos0(ptr): return __builtin_object_size (ptr, 0) # macro
def __glibc_unlikely(cond): return __builtin_expect ((cond), 0) # macro
TIOCM_RNG = 128 # Variable c_int '128'
TIOCM_RI = TIOCM_RNG # alias
CDISCARD = 15 # Variable c_int '15'
CFLUSH = CDISCARD # alias
# def __errordecl(name,msg): return extern void name (void) __attribute__((__error__ (msg))) # macro
def __glibc_likely(cond): return __builtin_expect ((cond), 1) # macro
# def __REDIRECT_NTH(name,proto,alias): return name proto __THROW __asm__ (__ASMNAME (#alias)) # macro
# def __REDIRECT_NTHNL(name,proto,alias): return name proto __THROWNL __asm__ (__ASMNAME (#alias)) # macro
# def __REDIRECT(name,proto,alias): return name proto __asm__ (__ASMNAME (#alias)) # macro
def __PMT(args): return args # macro
def __STRING(x): return #x # macro
def __REDIRECT_NTH_LDBL(name,proto,alias): return __REDIRECT_NTH (name, proto, alias) # macro
# __builtin_va_arg_pack_len = int # alias
# def __attribute_alloc_size__(params): return __attribute__ ((__alloc_size__ params)) # macro
def __REDIRECT_LDBL(name,proto,alias): return __REDIRECT (name, proto, alias) # macro
# def __LDBL_REDIR1_NTH(name,proto,alias): return name proto __THROW # macro
SIOCGIFINDEX = 35123 # Variable c_int '35123'
SIOGIFINDEX = SIOCGIFINDEX # alias
# def __NTH(fct): return __LEAF_ATTR fct throw () # macro
def __attribute_format_arg__(x): return __attribute__ ((__format_arg__ (x))) # macro
CEOF = 4 # Variable c_int '4'
CEOT = CEOF # alias
def _IOWR_BAD(type,nr,size): return _IOC(_IOC_READ|_IOC_WRITE,(type),(nr),sizeof(size)) # macro
def _IOR_BAD(type,nr,size): return _IOC(_IOC_READ,(type),(nr),sizeof(size)) # macro
def _IOWR(type,nr,size): return _IOC(_IOC_READ|_IOC_WRITE,(type),(nr),(_IOC_TYPECHECK(size))) # macro
def __ASMNAME(cname): return __ASMNAME2 (__USER_LABEL_PREFIX__, cname) # macro
def _IOR(type,nr,size): return _IOC(_IOC_READ,(type),(nr),(_IOC_TYPECHECK(size))) # macro
def _IOW(type,nr,size): return _IOC(_IOC_WRITE,(type),(nr),(_IOC_TYPECHECK(size))) # macro
def _IOC_TYPECHECK(t): return (sizeof(t)) # macro
def _IOC_TYPE(nr): return (((nr) >> _IOC_TYPESHIFT) & _IOC_TYPEMASK) # macro
# def __LDBL_REDIR(name,proto): return name proto # macro
def __GNUC_PREREQ(maj,min): return ((__GNUC__ << 16) + __GNUC_MINOR__ >= ((maj) << 16) + (min)) # macro
def _IOC_NR(nr): return (((nr) >> _IOC_NRSHIFT) & _IOC_NRMASK) # macro
def __CONCAT(x,y): return x ## y # macro
def _IOC_SIZE(nr): return (((nr) >> _IOC_SIZESHIFT) & _IOC_SIZEMASK) # macro
def __GLIBC_PREREQ(maj,min): return ((__GLIBC__ << 16) + __GLIBC_MINOR__ >= ((maj) << 16) + (min)) # macro
def _IOW_BAD(type,nr,size): return _IOC(_IOC_WRITE,(type),(nr),sizeof(size)) # macro
# def __ASMNAME2(prefix,cname): return __STRING (prefix) cname # macro
def __va_arg_pack_len(): return __builtin_va_arg_pack_len () # macro
def _IO(type,nr): return _IOC(_IOC_NONE,(type),(nr),0) # macro
def CTRL(x): return (x&0o37) # macro
def _IOC(dir,type,nr,size): return (((dir) << _IOC_DIRSHIFT) | ((type) << _IOC_TYPESHIFT) | ((nr) << _IOC_NRSHIFT) | ((size) << _IOC_SIZESHIFT)) # macro
def _IOC_DIR(nr): return (((nr) >> _IOC_DIRSHIFT) & _IOC_DIRMASK) # macro
# def __LDBL_REDIR1(name,proto,alias): return name proto # macro
CREPRINT = 18 # Variable c_int '18'
CRPRNT = CREPRINT # alias
# def __nonnull(params): return __attribute__ ((__nonnull__ params)) # macro
def __P(args): return args # macro
SIOCDELMULTI = 35122 # Variable c_int '35122'
_POSIX_C_SOURCE = 200809 # Variable c_long '200809l'
_ATFILE_SOURCE = 1 # Variable c_int '1'
__USE_XOPEN2KXSI = 1 # Variable c_int '1'
TIOCPKT_FLUSHWRITE = 2 # Variable c_int '2'
CINTR = 3 # Variable c_int '3'
FIOQSIZE = 21600 # Variable c_int '21600'
FIONCLEX = 21584 # Variable c_int '21584'
__GNU_LIBRARY__ = 6 # Variable c_int '6'
TIOCGDEV = 2147767346 # Variable c_ulong '2147767346ul'
TIOCGETD = 21540 # Variable c_int '21540'
__USE_XOPEN = 1 # Variable c_int '1'
SIOCSIFNAME = 35107 # Variable c_int '35107'
N_HCI = 15 # Variable c_int '15'
TCFLSH = 21515 # Variable c_int '21515'
__USE_XOPEN2K8 = 1 # Variable c_int '1'
__USE_POSIX2 = 1 # Variable c_int '1'
SIOCPROTOPRIVATE = 35296 # Variable c_int '35296'
TIOCOUTQ = 21521 # Variable c_int '21521'
FIOASYNC = 21586 # Variable c_int '21586'
SIOCGIFNAME = 35088 # Variable c_int '35088'
TIOCPKT_STOP = 4 # Variable c_int '4'
SIOCSIFMETRIC = 35102 # Variable c_int '35102'
TIOCM_ST = 8 # Variable c_int '8'
TIOCM_SR = 16 # Variable c_int '16'
SIOCRTMSG = 35085 # Variable c_int '35085'
TIOCSERSETMULTI = 21595 # Variable c_int '21595'
SIOCGIFHWADDR = 35111 # Variable c_int '35111'
IOCSIZE_MASK = 1073676288 # Variable c_int '1073676288'
TIOCMGET = 21525 # Variable c_int '21525'
TIOCSETD = 21539 # Variable c_int '21539'
IOCSIZE_SHIFT = 16 # Variable c_int '16'
N_6PACK = 7 # Variable c_int '7'
TIOCVHANGUP = 21559 # Variable c_int '21559'
IOC_INOUT = 3221225472 # Variable c_uint '3221225472u'
TIOCPKT_IOCTL = 64 # Variable c_int '64'
CQUIT = 28 # Variable c_int '28'
SIOCSIFFLAGS = 35092 # Variable c_int '35092'
TIOCPKT_DATA = 0 # Variable c_int '0'
TIOCSER_TEMT = 1 # Variable c_int '1'
_FILE_OFFSET_BITS = 64 # Variable c_int '64'
CSTOP = 19 # Variable c_int '19'
__USE_ATFILE = 1 # Variable c_int '1'
TIOCGPTN = 2147767344 # Variable c_ulong '2147767344ul'
SIOCSIFMEM = 35104 # Variable c_int '35104'
SIOCGIFMETRIC = 35101 # Variable c_int '35101'
TIOCCBRK = 21544 # Variable c_int '21544'
TIOCLINUX = 21532 # Variable c_int '21532'
TIOCSPGRP = 21520 # Variable c_int '21520'
SIOCGARP = 35156 # Variable c_int '35156'
TIOCGRS485 = 21550 # Variable c_int '21550'
SIOCGIFBRDADDR = 35097 # Variable c_int '35097'
_POSIX_SOURCE = 1 # Variable c_int '1'
_ISOC95_SOURCE = 1 # Variable c_int '1'
_ISOC99_SOURCE = 1 # Variable c_int '1'
SIOCADDRT = 35083 # Variable c_int '35083'
__USE_POSIX = 1 # Variable c_int '1'
_IOC_READ = 2 # Variable c_uint '2u'
SIOCSIFSLAVE = 35120 # Variable c_int '35120'
_IOC_DIRMASK = 3 # Variable c_int '3'
_IOC_SIZEBITS = 14 # Variable c_int '14'
CMIN = 1 # Variable c_int '1'
SIOCGIFADDR = 35093 # Variable c_int '35093'
SIOCSIFBRDADDR = 35098 # Variable c_int '35098'
TIOCGWINSZ = 21523 # Variable c_int '21523'
TIOCGPTLCK = 2147767353 # Variable c_ulong '2147767353ul'
TCXONC = 21514 # Variable c_int '21514'
TCSETAW = 21511 # Variable c_int '21511'
SIOCSIFMTU = 35106 # Variable c_int '35106'
IOC_OUT = 2147483648 # Variable c_uint '2147483648u'
TIOCSERGETMULTI = 21594 # Variable c_int '21594'
__USE_POSIX199309 = 1 # Variable c_int '1'
TIOCSRS485 = 21551 # Variable c_int '21551'
N_X25 = 6 # Variable c_int '6'
TIOCM_LE = 1 # Variable c_int '1'
TIOCGPKT = 2147767352 # Variable c_ulong '2147767352ul'
__SYSCALL_WORDSIZE = 64 # Variable c_int '64'
__GLIBC_MINOR__ = 23 # Variable c_int '23'
TIOCM_DSR = 256 # Variable c_int '256'
TIOCPKT_NOSTOP = 16 # Variable c_int '16'
SIOCDRARP = 35168 # Variable c_int '35168'
N_TTY = 0 # Variable c_int '0'
SIOCGIFMEM = 35103 # Variable c_int '35103'
CSTATUS = '\x00' # Variable c_char "'\\000'"
TIOCMIWAIT = 21596 # Variable c_int '21596'
TCSETSW = 21507 # Variable c_int '21507'
TIOCGSID = 21545 # Variable c_int '21545'
TIOCSERGSTRUCT = 21592 # Variable c_int '21592'
_IOC_NONE = 0 # Variable c_uint '0u'
SIOCGIFFLAGS = 35091 # Variable c_int '35091'
__WORDSIZE_TIME64_COMPAT32 = 1 # Variable c_int '1'
__USE_XOPEN2K = 1 # Variable c_int '1'
SIOCSIFLINK = 35089 # Variable c_int '35089'
CLNEXT = 22 # Variable c_int '22'
SIOCGIFPFLAGS = 35125 # Variable c_int '35125'
_IOC_TYPEMASK = 255 # Variable c_int '255'
TCGETX = 21554 # Variable c_int '21554'
TIOCM_DTR = 2 # Variable c_int '2'
TIOCSBRK = 21543 # Variable c_int '21543'
TCSBRKP = 21541 # Variable c_int '21541'
TCGETS = 21505 # Variable c_int '21505'
TCSETA = 21510 # Variable c_int '21510'
__USE_ISOC95 = 1 # Variable c_int '1'
__USE_GNU = 1 # Variable c_int '1'
SIOCGIFCONF = 35090 # Variable c_int '35090'
TIOCEXCL = 21516 # Variable c_int '21516'
__USE_LARGEFILE64 = 1 # Variable c_int '1'
_IOC_SIZEMASK = 16383 # Variable c_int '16383'
TIOCPKT_START = 8 # Variable c_int '8'
TCSETX = 21555 # Variable c_int '21555'
TCGETA = 21509 # Variable c_int '21509'
N_STRIP = 4 # Variable c_int '4'
TIOCCONS = 21533 # Variable c_int '21533'
TCSETS = 21506 # Variable c_int '21506'
_LARGEFILE_SOURCE = 1 # Variable c_int '1'
TIOCSSERIAL = 21535 # Variable c_int '21535'
SIOCGIFMTU = 35105 # Variable c_int '35105'
_ISOC11_SOURCE = 1 # Variable c_int '1'
TIOCSERCONFIG = 21587 # Variable c_int '21587'
TIOCSCTTY = 21518 # Variable c_int '21518'
SIOCGIFENCAP = 35109 # Variable c_int '35109'
TIOCSSOFTCAR = 21530 # Variable c_int '21530'
SIOCDARP = 35155 # Variable c_int '35155'
TIOCGPGRP = 21519 # Variable c_int '21519'
_IOC_DIRSHIFT = 30 # Variable c_int '30'
__USE_UNIX98 = 1 # Variable c_int '1'
IOC_IN = 1073741824 # Variable c_uint '1073741824u'
SIOCGIFMAP = 35184 # Variable c_int '35184'
N_IRDA = 11 # Variable c_int '11'
__USE_MISC = 1 # Variable c_int '1'
_DEFAULT_SOURCE = 1 # Variable c_int '1'
TIOCSPTLCK = 1074025521 # Variable c_ulong '1074025521ul'
_IOC_WRITE = 1 # Variable c_uint '1u'
SIOCDELDLCI = 35201 # Variable c_int '35201'
CWERASE = 23 # Variable c_int '23'
SIOCSIFBR = 35137 # Variable c_int '35137'
SIOCGRARP = 35169 # Variable c_int '35169'
TIOCPKT_DOSTOP = 32 # Variable c_int '32'
SIOCSIFADDR = 35094 # Variable c_int '35094'
TIOCNXCL = 21517 # Variable c_int '21517'
SIOCGIFDSTADDR = 35095 # Variable c_int '35095'
_IOC_SIZESHIFT = 16 # Variable c_int '16'
SIOCSIFDSTADDR = 35096 # Variable c_int '35096'
_IOC_NRSHIFT = 0 # Variable c_int '0'
TIOCSIG = 1074025526 # Variable c_ulong '1074025526ul'
__USE_FORTIFY_LEVEL = 2 # Variable c_int '2'
SIOCSARP = 35157 # Variable c_int '35157'
SIOCSRARP = 35170 # Variable c_int '35170'
SIOCADDMULTI = 35121 # Variable c_int '35121'
TIOCSERGETLSR = 21593 # Variable c_int '21593'
SIOCGIFSLAVE = 35113 # Variable c_int '35113'
_IOC_TYPEBITS = 8 # Variable c_int '8'
TIOCGICOUNT = 21597 # Variable c_int '21597'
TIOCSLCKTRMIOS = 21591 # Variable c_int '21591'
__USE_XOPEN_EXTENDED = 1 # Variable c_int '1'
N_HDLC = 13 # Variable c_int '13'
N_AX25 = 5 # Variable c_int '5'
CKILL = 21 # Variable c_int '21'
N_SYNC_PPP = 14 # Variable c_int '14'
SIOCADDDLCI = 35200 # Variable c_int '35200'
CERASE = 127 # Variable c_int '127'
__USE_LARGEFILE = 1 # Variable c_int '1'
FIOCLEX = 21585 # Variable c_int '21585'
_IOC_NRMASK = 255 # Variable c_int '255'
_FEATURES_H = 1 # Variable c_int '1'
_IOC_NRBITS = 8 # Variable c_int '8'
SIOCDELRT = 35084 # Variable c_int '35084'
TCSETAF = 21512 # Variable c_int '21512'
SIOCSIFHWADDR = 35108 # Variable c_int '35108'
__USE_POSIX199506 = 1 # Variable c_int '1'
SIOCDEVPRIVATE = 35312 # Variable c_int '35312'
SIOCSIFHWBROADCAST = 35127 # Variable c_int '35127'
__USE_FILE_OFFSET64 = 1 # Variable c_int '1'
SIOCSIFNETMASK = 35100 # Variable c_int '35100'
SIOCSIFENCAP = 35110 # Variable c_int '35110'
SIOCGIFCOUNT = 35128 # Variable c_int '35128'
TIOCSERSWILD = 21589 # Variable c_int '21589'
SIOCGIFBR = 35136 # Variable c_int '35136'
SIOCSIFMAP = 35185 # Variable c_int '35185'
FUSE_USE_VERSION = 29 # Variable c_int '29'
CSTART = 17 # Variable c_int '17'
SIOCSIFPFLAGS = 35124 # Variable c_int '35124'
N_SLIP = 1 # Variable c_int '1'
TIOCSWINSZ = 21524 # Variable c_int '21524'
TIOCPKT = 21536 # Variable c_int '21536'
SIOCDIFADDR = 35126 # Variable c_int '35126'
N_MASC = 8 # Variable c_int '8'
TIOCSERGWILD = 21588 # Variable c_int '21588'
_XOPEN_SOURCE_EXTENDED = 1 # Variable c_int '1'
_IOC_TYPESHIFT = 8 # Variable c_int '8'
__USE_XOPEN2K8XSI = 1 # Variable c_int '1'
__WORDSIZE = 64 # Variable c_int '64'
TIOCM_RTS = 4 # Variable c_int '4'
_SYS_CDEFS_H = 1 # Variable c_int '1'
TIOCMBIS = 21526 # Variable c_int '21526'
_LARGEFILE64_SOURCE = 1 # Variable c_int '1'
TIOCMSET = 21528 # Variable c_int '21528'
CTIME = 0 # Variable c_int '0'
_XOPEN_SOURCE = 700 # Variable c_int '700'
TCSETXW = 21557 # Variable c_int '21557'
TIOCPKT_FLUSHREAD = 1 # Variable c_int '1'
TIOCGSOFTCAR = 21529 # Variable c_int '21529'
N_PPP = 3 # Variable c_int '3'
TIOCNOTTY = 21538 # Variable c_int '21538'
TIOCSTI = 21522 # Variable c_int '21522'
TIOCGSERIAL = 21534 # Variable c_int '21534'
TIOCMBIC = 21527 # Variable c_int '21527'
CSUSP = 26 # Variable c_int '26'
TIOCGLCKTRMIOS = 21590 # Variable c_int '21590'
CDSUSP = 25 # Variable c_int '25'
TIOCGEXCL = 2147767360 # Variable c_ulong '2147767360ul'
N_R3964 = 9 # Variable c_int '9'
_SYS_IOCTL_H = 1 # Variable c_int '1'
__GLIBC__ = 2 # Variable c_int '2'
__USE_ISOC99 = 1 # Variable c_int '1'
__USE_EXTERN_INLINES = 1 # Variable c_int '1'
TIOCM_CTS = 32 # Variable c_int '32'
FIONBIO = 21537 # Variable c_int '21537'
N_SMSBLOCK = 12 # Variable c_int '12'
SIOCGIFNETMASK = 35099 # Variable c_int '35099'
__USE_ISOC11 = 1 # Variable c_int '1'
SIOCSIFTXQLEN = 35139 # Variable c_int '35139'
_IOC_DIRBITS = 2 # Variable c_int '2'
SIOCGIFTXQLEN = 35138 # Variable c_int '35138'
TCSETXF = 21556 # Variable c_int '21556'
TCSETSF = 21508 # Variable c_int '21508'
N_MOUSE = 2 # Variable c_int '2'
TCSBRK = 21513 # Variable c_int '21513'
NCC = 8 # Variable c_int '8'
N_PROFIBUS_FDL = 10 # Variable c_int '10'
# /usr/include/x86_64-linux-gnu/bits/ioctl-types.h 28
class winsize(Structure):
    pass
winsize._fields_ = [
    # /usr/include/x86_64-linux-gnu/bits/ioctl-types.h 28
    ('ws_row', c_ushort),
    ('ws_col', c_ushort),
    ('ws_xpixel', c_ushort),
    ('ws_ypixel', c_ushort),
]
# /usr/include/x86_64-linux-gnu/bits/ioctl-types.h 37
class termio(Structure):
    pass
termio._fields_ = [
    # /usr/include/x86_64-linux-gnu/bits/ioctl-types.h 37
    ('c_iflag', c_ushort),
    ('c_oflag', c_ushort),
    ('c_cflag', c_ushort),
    ('c_lflag', c_ushort),
    ('c_line', c_ubyte),
    ('c_cc', c_ubyte * 8),
]
__all__ = ['SIOCDELMULTI', 'CSUSP', '_ATFILE_SOURCE',
           '__USE_XOPEN2KXSI', 'CDISCARD', '__glibc_unlikely',
           '__glibc_likely', 'SIOCGIFMEM', '_IOC_TYPEBITS',
           'FIONCLEX', '__GNU_LIBRARY__', '_IOC_READ', 'TIOCGETD',
           '__USE_XOPEN', 'SIOCSIFNAME', 'TCFLSH', '__USE_XOPEN2K8',
           'SIOCSIFENCAP', '__USE_POSIX2', 'SIOCPROTOPRIVATE',
           'TIOCOUTQ', 'CTRL', '__USE_XOPEN2K8XSI', 'SIOCGIFNAME',
           'SIOCGIFHWADDR', '_IOC_TYPE', 'SIOCSIFMETRIC', 'TIOCM_ST',
           '__WORDSIZE', 'TIOCM_SR', 'SIOCRTMSG', 'TIOCSERSETMULTI',
           'TIOCM_RTS', 'TIOCMGET', 'TIOCGSERIAL', 'TIOCSETD',
           'IOCSIZE_SHIFT', 'N_6PACK', 'TIOCVHANGUP', 'IOC_INOUT',
           'TCSETXF', 'TIOCPKT_IOCTL', 'SIOCSIFFLAGS', 'TIOCPKT_DATA',
           'TIOCSER_TEMT', '_FILE_OFFSET_BITS', 'CSTOP',
           '__USE_ATFILE', 'TIOCGPTN', 'SIOCGIFMETRIC', 'TIOCSRS485',
           '__GLIBC_PREREQ', 'TIOCCBRK', '_IOC_NR', '__ASMNAME',
           'TIOCSPGRP', 'SIOCDARP', 'SIOCGARP', 'TIOCPKT_FLUSHWRITE',
           'SIOCGIFBRDADDR', '_POSIX_SOURCE', '_IOC_SIZE', 'TIOCM_CD',
           '_ISOC99_SOURCE', 'SIOCADDRT', 'TIOCLINUX', '__USE_POSIX',
           'winsize', 'TIOCGRS485', '__bos', '_IOC_DIRMASK', 'CEOF',
           'CMIN', 'SIOCGIFADDR', 'SIOCSIFBRDADDR', 'FIONREAD',
           'CEOL', 'TIOCGWINSZ', 'TCXONC', 'CEOT', 'SIOCSIFNETMASK',
           '__USE_LARGEFILE', 'SIOCSIFMTU', 'IOC_OUT',
           '_ISOC95_SOURCE', '__warnattr', 'N_HCI', 'N_X25',
           'TIOCM_LE', 'TIOCGPKT', '__SYSCALL_WORDSIZE',
           '__GLIBC_MINOR__', 'TIOCM_DSR', '__USE_MISC', 'CINTR',
           'CSTATUS', 'N_IRDA', '_IOR_BAD', 'TCSETSW', 'TIOCGSID',
           'TIOCSERGSTRUCT', 'SIOCSIFHWADDR',
           '__attribute_format_strfmon__', 'SIOCGIFFLAGS',
           'SIOCSIFLINK', 'CDSUSP', '__USE_XOPEN2K',
           '__WORDSIZE_TIME64_COMPAT32', 'CLNEXT', '_IOWR_BAD', '__P',
           '_IOC_TYPEMASK', '_SYS_CDEFS_H', 'TCGETX', 'TIOCM_DTR',
           '__USE_GNU', '_IOW_BAD', 'SIOCGIFCONF', 'TCGETS', 'TCSETA',
           'TIOCMBIC', 'SIOCSIFSLAVE', 'TIOCM_RI', 'SIOCSIFMEM',
           '__CONCAT', 'TIOCM_RNG', 'TIOCPKT_START', 'TCSETX',
           'TIOCSERSWILD', '__attribute_format_arg__', 'TCGETA',
           'N_STRIP', '__PMT', 'TCSETS', '_LARGEFILE_SOURCE',
           '_POSIX_C_SOURCE', 'SIOCGIFMTU', '_ISOC11_SOURCE',
           'TIOCSERCONFIG', 'TIOCSCTTY', 'SIOCGIFENCAP',
           'SIOCGIFTXQLEN', 'TIOCSSOFTCAR', 'TIOCMIWAIT', 'SIOCDRARP',
           'TIOCGDEV', '__USE_UNIX98', '__USE_POSIX199506',
           'TIOCPKT_STOP', 'TIOCPKT_NOSTOP', '_DEFAULT_SOURCE',
           'TIOCSPTLCK', 'CRPRNT', 'SIOCGRARP', '_IOC_DIRSHIFT',
           'SIOCDELDLCI', '__USE_FILE_OFFSET64', 'SIOCGIFINDEX',
           'SIOCSIFBR', '_IOC_TYPECHECK', 'TIOCSTI', '__USE_ISOC99',
           'termio', '__USE_LARGEFILE64', 'TIOCNXCL', '_IOWR',
           'SIOCGIFDSTADDR', '_IOC_SIZESHIFT', 'SIOCSIFDSTADDR',
           '_IOC_NRSHIFT', 'TIOCSIG', '__USE_FORTIFY_LEVEL', '_IOW',
           'SIOCSARP', 'SIOCSRARP', 'SIOCADDMULTI', '_IOR',
           'SIOCGIFSLAVE', '_IOC_SIZEBITS', 'FIOQSIZE', 'CTIME',
           'TIOCGICOUNT', 'CFLUSH', '_IOC', 'TIOCSLCKTRMIOS',
           '__USE_XOPEN_EXTENDED', 'TIOCM_CAR', 'N_HDLC', 'N_AX25',
           'CKILL', 'N_SYNC_PPP', 'SIOCADDDLCI', 'CERASE', 'TCSETAW',
           'FIOCLEX', '_IO', 'TCSBRKP', '_IOC_NRMASK', '_FEATURES_H',
           'N_SMSBLOCK', 'SIOCDELRT', 'TCSETAF',
           '__REDIRECT_NTH_LDBL', 'N_TTY', 'SIOCGIFMAP', 'IOC_IN',
           'SIOCSIFHWBROADCAST', 'CWERASE', 'CQUIT', '_SYS_IOCTL_H',
           '_IOC_NONE', 'CREPRINT', '__STRING', 'SIOCDEVPRIVATE',
           'SIOCGIFBR', 'SIOCSIFMAP', 'FUSE_USE_VERSION',
           'SIOCSIFTXQLEN', 'SIOCSIFPFLAGS', '_IOC_DIR', 'N_SLIP',
           '__GNUC_PREREQ', 'TIOCSWINSZ', 'TIOCSERGETMULTI',
           'SIOCDIFADDR', 'TIOCEXCL', 'TIOCSERGWILD',
           '_XOPEN_SOURCE_EXTENDED', '_IOC_TYPESHIFT',
           '__USE_POSIX199309', '_IOC_WRITE', 'FIOASYNC',
           '_IOC_SIZEMASK', 'TIOCGPTLCK', 'N_PPP', 'SIOCSIFADDR',
           'TIOCSSERIAL', 'TIOCMBIS', '_LARGEFILE64_SOURCE',
           'TIOCMSET', '__va_arg_pack', '_XOPEN_SOURCE',
           'SIOCGIFCOUNT', 'TCSETXW', 'TIOCPKT_FLUSHREAD', 'N_R3964',
           'TIOCGSOFTCAR', '_IOC_NRBITS', 'SIOGIFINDEX',
           'TIOCSERGETLSR', 'TIOCSBRK', '__USE_ISOC95', 'TIOCPKT',
           'TIOCGLCKTRMIOS', '__va_arg_pack_len', 'CBRK', 'TIOCGEXCL',
           '__bos0', 'SIOCGIFPFLAGS', '__GLIBC__', '__REDIRECT_LDBL',
           'TIOCPKT_DOSTOP', '__USE_EXTERN_INLINES', 'TIOCM_CTS',
           'SIOCGIFNETMASK', 'FIONBIO', 'TIOCCONS', 'TIOCGPGRP',
           'N_MASC', 'TIOCINQ', '__USE_ISOC11', 'CSTART',
           '_IOC_DIRBITS', 'IOCSIZE_MASK', 'TIOCNOTTY', 'TCSETSF',
           'N_MOUSE', 'TCSBRK', 'NCC', 'N_PROFIBUS_FDL']
