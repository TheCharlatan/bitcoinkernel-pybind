from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import sys
import os

class get_pybind_include(object):
    """Helper class to determine the pybind11 include path
    The purpose of this class is to postpone importing pybind11
    until it is actually installed, so that the ``get_include()``
    method can be invoked."""

    def __init__(self, user=False):
        self.user = user

    def __str__(self):
        import pybind11
        return pybind11.get_include(self.user)

ext_modules = [
    Extension(
        'bitcoinkernel',
        ['src/bindings.cpp'],
        include_dirs=[
            # Path to pybind11 headers
            get_pybind_include(),
            get_pybind_include(user=True),
            "bitcoin/src"
        ],
        define_macros=[
            ('HAVE_CONFIG_H', '1'),
            ('DEBUG', '1'),
            ('_DEBUG', '1')
        ],
        undef_macros=[
            'NDEBUG',
            'WAIT_LOCK'
        ],
        library_dirs=[
            "bitcoin/build/lib"
        ],
        libraries=[
            'bitcoinkernel'
        ],
        runtime_library_dirs=[
            "bitcoin/build/lib"
        ],
        language='c++'
    ),
]

class BuildExt(build_ext):
    """A custom build extension for adding compiler-specific options."""
    c_opts = {
        'msvc': ['/EHsc'],
        'unix': ['-std=c++20'],
    }
    l_opts = {
        'msvc': [],
        'unix': [],
    }

    if sys.platform == 'darwin':
        darwin_opts = ['-stdlib=libc++', '-mmacosx-version-min=10.14']
        c_opts['unix'] += darwin_opts
        l_opts['unix'] += darwin_opts

    def build_extensions(self):
        ct = self.compiler.compiler_type
        opts = self.c_opts.get(ct, [])
        link_opts = self.l_opts.get(ct, [])
        if ct == 'unix':
            opts.append('-DVERSION_INFO="%s"' % self.distribution.get_version())
        elif ct == 'msvc':
            opts.append('/DVERSION_INFO=\\"%s\\"' % self.distribution.get_version())
        for ext in self.extensions:
            ext.extra_compile_args = opts
            ext.extra_link_args = link_opts
        build_ext.build_extensions(self)

setup(
    name='bitcoinkernel',
    version='0.1',
    author='Your Name',
    author_email='your.email@example.com',
    description='Python bindings for libbitcoinkernel',
    long_description='',
    ext_modules=ext_modules,
    install_requires=['pybind11>=2.13.0'],
    setup_requires=['pybind11>=2.13.0'],
    cmdclass={'build_ext': BuildExt},
    zip_safe=False,
)

