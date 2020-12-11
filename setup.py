import os
import sys
from distutils.sysconfig import get_python_lib

from setuptools import setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 6)

# This check and everything above must remain compatible with Python 2.7.
if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("""
==========================
Unsupported Python version
==========================
This version of NLP requires Python {}.{}, but you're trying to
install it on Python {}.{}.
This may be because you are using a version of pip that doesn't
understand the python_requires classifier. Make sure you
have pip >= 9.0 and setuptools >= 24.2, then try again:
    $ python -m pip install --upgrade pip setuptools
    $ python -m pip install nlp
This will install the latest version of NLP which works on your
version of Python. If you can't upgrade your pip (or Python), request
an older version of NLP:
    $ python -m pip install "NLP<2"
""".format(*(REQUIRED_PYTHON + CURRENT_PYTHON)))
    sys.exit(1)

overlay_warning = False
if "install" in sys.argv:
    lib_paths = [get_python_lib()]
    if lib_paths[0].startswith("/usr/lib/"):

        lib_paths.append(get_python_lib(prefix="/usr/local"))

    for lib_path in lib_paths:
        existing_path = os.path.abspath(os.path.join(lib_path, "nlp"))

        if os.path.exists(existing_path):

            overlay_warning = True
            break


setup(
    name='NLP',
    version='1.0',
    description='Python natural language processing algorithm in brazilian portuguese',
    author='Elias Olie',
    author_email='contato.eliasolie@gmail.com',
    url='https://github.com/EliasOlie/NLP',
    packages=['nlp'],
)


if overlay_warning:
    sys.stderr.write("""
========
WARNING!
========
You have just installed NLP over top of an existing
installation, without removing it first. Because of this,
your install may now include extraneous files from a
previous version that have since been removed from
NLP. This is known to cause a variety of problems. You
should manually remove the
%(existing_path)s
directory and re-install NLP.
""" % {"existing_path": existing_path})