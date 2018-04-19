from distutils.core import setup, Extension

setup(name='Palindrome',
      version='1.0.0',
      description='Simple SWIG example for palindrome test',
      ext_modules=[Extension('_palindrome', sources=['palindrome.c', 'palindrome.i'])]
      )