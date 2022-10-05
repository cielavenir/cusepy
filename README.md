I (@cielavenir) built cuse_api.py using Ubuntu xenial 16.04 virtual machine. This api.py should work on Linux (libfuse2 flavor), but other platforms are untested at all.

```sh
sudo apt update
sudo apt upgrade
sudo apt install -y libfuse-dev libattr1-dev gccxml python-dev python-pip python-wheel pkg-config subversion git g++-4.9
if [ ! -f /usr/bin/gccxml.castxml ]; then
    sudo mv /usr/bin/gccxml /usr/bin/gccxml.castxml
    sudo update-alternatives --install /usr/bin/gccxml gccxml.castxml /usr/bin/gccxml.castxml 1
    sudo update-alternatives --install /usr/bin/gccxml gccxml.real /usr/bin/gccxml.real 10
fi
sudo python -m pip install 'svn+http://svn.python.org/projects/ctypes/trunk/ctypeslib/#egg=ctypeslib-dev'
```

----

Note that the low-level API needs to generate the Python interface
to the local CUSE library before it can be used. For that,
you have to have both the CUSE headers and the GCC-XML
(http://www.gccxml.org) compiler installed.

The interface is generated by running 

# python setup.py build_ctypes

this will create the file cuse/cuse_api.py

Please keep in mind that it's probably not wise to ship this file
with your application, because it has been generated for your
system only.


Note that the fuse_daemonize() function is deliberately not exported
by this module. If you want to daemonize a Python process, you have to
do so from within Python or you will get into trouble. See
 - http://bugs.python.org/issue7931 
 - http://www.python.org/dev/peps/pep-3143/
 
