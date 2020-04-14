import setuptools

from setuptools import setup, Extension
from Cython.Build import cythonize


setup(
    name='example8',
    version='0.1',
    packages=[
        'example8'
    ],
    package_dir={
        'example8': 'project'
    },
    ext_modules=cythonize([
        Extension(
            "example8.pyx", [
                "project/fast_primes.pyx",
            ], extra_compile_args=[
                "-O3", "-Ofast"
            ],
        ),

        Extension(
            "example8.cpp", [
                "src/primes.c",
                "src/python/module.c",
            ], include_dirs=[
                "include"
            ], extra_compile_args=[
                "-O3", "-Ofast"
            ], language="c++",
        ),
    ]),
)
