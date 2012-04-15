from setuptools import setup
from setuptools.extension import Extension
from Cython.Distutils import build_ext

ext_modules=[Extension("calibkinect.calibkinect_cy",
                       ["calibkinect/calibkinect_cy.pyx"])]

for e in ext_modules:
    e.pyrex_directives = {"embedsignature": True}

setup(name='CalibKinect',
      version='0.1',
      author='Andrew Miller',
      email='amiller@cs.ucf.edu',
      packages=['calibkinect'],
      cmdclass={'build_ext': build_ext},
      ext_modules=ext_modules,
      install_requires=['distribute', 'cython', 'numpy', 'scipy'])
