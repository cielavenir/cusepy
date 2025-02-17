#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Copyright (c) 2010, Naranjo Manuel Francisco <manuel@aircable.net>
Copyright (c) 2010, Nikolaus Rath <Nikolaus@rath.org>
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
    * Neither the name of the main author nor the names of other contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

from __future__ import division, print_function

from distutils.core import setup, Command
import distutils.command.build
import sys
import os
import tempfile
import subprocess
import re
import logging
import ctypes.util

# These are the definitions that we need
cuse_export_regex = ['^FUSE_SET_.*',
                     '^XATTR_.*',
                     'fuse_reply_.*',
                     'cuse_.*',
                     'CUSE_.*',
                     'fuse_chan.*']
cuse_export_symbols = ['fuse_set_signal_handlers',
                       'fuse_session_add_chan',
                       'fuse_session_loop_mt',
                       'fuse_session_remove_chan',
                       'fuse_remove_signal_handlers',
                       'fuse_session_destroy',
                       'fuse_req_ctx',
                       'fuse_session_loop',
                       'ENOATTR',
                       'ENOTSUP',
                       'fuse_version',
                       'fuse_kern_chan_new',
                       'fuse_session_exit',
                       'fuse_session_exited',
                       'fuse_lowlevel_notify_poll',
                       'fuse_pollhandle_destroy']


class build_ctypes(Command):

    description = "Build ctypes interfaces"
    user_options = []
    boolean_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def do_ctypes(self, header="fuse_ctypes.h", output="ctypes_api.py",
                  regex=cuse_export_regex, symbols=cuse_export_symbols, libs=['fuse']):
        '''Create ctypes API to given headers'''

        basedir = os.path.abspath(os.path.dirname(sys.argv[0]))
        api_file = os.path.join(basedir, 'cuse', output)
        if os.path.isfile(api_file):
            return

        from ctypeslib import h2xml, xml2py
        from ctypeslib.codegen import codegenerator as ctypeslib

        print('Creating ctypes API from local headers...')

        cflags = self.get_cflags()
        print('Using cflags: %s' % ' '.join(cflags))

        for l in libs:
            if not ctypes.util.find_library(l):
                print('Could not find %s library' % l, file=sys.stderr)
                sys.exit(1)

        # Create temporary XML file
        tmp_fh = tempfile.NamedTemporaryFile()
        tmp_name = tmp_fh.name

        print('Calling h2xml...')
        argv = ['h2xml.py', '-o', tmp_name, '-c', '-q', '-I', basedir, header]
        argv += cflags
        ctypeslib.ASSUME_STRINGS = False
        ctypeslib.CDLL_SET_ERRNO = False
        ctypeslib.PREFIX = ('# Code autogenerated by ctypeslib. Any changes will be lost!\n\n'
                            '#pylint: disable-all\n'
                            '#@PydevCodeAnalysisIgnore\n\n')
        h2xml.main(argv)

        print('Calling xml2py...')
        argv = ['xml2py.py', '-c', '-d', '-v', tmp_name, '-o', api_file]
        for l in libs:
            argv.append('-l')
            argv.append(l)
        for el in regex:
            argv.append('-r')
            argv.append(el)
        for el in symbols:
            argv.append('-s')
            argv.append(el)
        xml2py.main(argv)

        # Delete temporary XML file
        tmp_fh.close()

        print('Code generation complete.')

    def run(self):
        '''Create ctypes API to local CUSE headers'''

        print("Creating ctypes for CUSE")
        self.do_ctypes('cuse_ctypes.h', 'cuse_api.py')
        self.do_ctypes('ioctl_ctypes.h', 'ioctl_api.py', regex=[], symbols=[], libs=[])
        print('Code generation complete.')

    def get_cflags(self):
        '''Get cflags required to compile with fuse library'''

        proc = subprocess.Popen(['pkg-config', 'fuse', '--cflags'], stdout=subprocess.PIPE)
        cflags = proc.stdout.readline().rstrip()
        proc.stdout.close()
        if proc.wait() != 0:
            sys.stderr.write('Failed to execute pkg-config. Exit code: %d.\n'
                             % proc.returncode)
            sys.stderr.write('Check that the FUSE development package been installed properly.\n')
            sys.exit(1)
        return cflags.split()


# Add as subcommand of build
distutils.command.build.build.sub_commands.insert(0, ('build_ctypes', None))


setup(name='cusepy',
      version='0.1',
      author='Naranjo Manuel Francisco',
      author_email='manuel@aircable.net',
      url='http://code.google.com/p/cusepy/',
      packages=['cuse'],
      provides=['cuse'],
      cmdclass={'build_ctypes': build_ctypes}
      )
