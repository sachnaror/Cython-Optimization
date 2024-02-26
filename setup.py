
from cython.Build import cythonize
from setuptools import setup

setup(
    ext_modules=cythonize("cyApp/fib.pyx")
)
