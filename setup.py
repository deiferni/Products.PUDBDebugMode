from setuptools import setup, find_packages
import os

version = '2.0.0'

setup(name='Products.PUDBDebugMode',
      version=version,
      description="Post-mortem debugging on Zope 2 excpetions",
      long_description=open(
          os.path.join("README.rst")
          ).read() + "\n" + open(
          os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      url='http://pypi.python.org/pypi/Products.PUDBDebugMode',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.monkeypatcher',
          'pudb',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
