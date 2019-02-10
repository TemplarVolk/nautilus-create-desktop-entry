#!/usr/bin/env python3

from compileall import compile_dir
from os import environ, path
from subprocess import call

prefix = environ.get('MESON_INSTALL_PREFIX', '/usr/local')
print(environ.get('MESON_INSTALL_PREFIX'))
datadir = path.join(prefix, 'share')
destdir = environ.get('DESTDIR', '')

if not destdir:
    print('Updating icon cache...')
    call(['gtk-update-icon-cache', '-qtf', path.join(datadir, 'icons', 'hicolor')])

print('Compiling python bytecode...')
moduledir = path.join(datadir, 'nautilus-create-desktop-entry')
compile_dir(destdir + moduledir, optimize=2)
