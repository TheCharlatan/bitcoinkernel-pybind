from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import sys
import os

ext_modules = [
    Extension(
        'bitcoinkernel',
        ['src/bindings.cpp'],
        include_dirs=[
            "bitcoin/src"
        ],
        define_macros=[
            ('HAVE_CONFIG_H', '1'),
            ('DEBUG', '1'),
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
        'unix': ['-std=c++20'],
    }
    l_opts = {
        'unix': [],
    }

    if sys.platform == 'darwin':
        darwin_opts = ['-stdlib=libc++']
        c_opts['unix'] += darwin_opts
        l_opts['unix'] += darwin_opts

    def build_extensions(self):
        ct = self.compiler.compiler_type
        opts = self.c_opts.get(ct, [])
        link_opts = self.l_opts.get(ct, [])
        if ct == 'unix':
            opts.append('-DVERSION_INFO="%s"' % self.distribution.get_version())
        for ext in self.extensions:
            ext.extra_compile_args = opts
            ext.extra_link_args = link_opts
        build_ext.build_extensions(self)

setup(
    name='bitcoinkernel',
    version='0.1',
    description='Python bindings for libbitcoinkernel',
    ext_modules=ext_modules,
    install_requires=['pybind11>=2.13.0'],
    setup_requires=['pybind11>=2.13.0'],
    cmdclass={'build_ext': BuildExt},
    zip_safe=False,
)

