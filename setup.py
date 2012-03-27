from setuptools import setup, find_packages

requires = []

setup(
    name = "knockout",
    description='Provides hooks to alter import. Allowe import from remote host',
    version = "0.1",
    author = "Jure Vrscaj",
    packages = ["knockout"],
    platforms = 'any',
    install_requires = requires,
  )
