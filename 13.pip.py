# What is PIP?
# PIP is a package manager for Python packages, or modules if you like.

"""
# What is a Package?
# A package contains all the files you need for a module.
#
# Modules are Python code libraries you can include in your project.

# Check if PIP is Installed
# pip --version

# Download a Package
# Downloading a package is very easy.
#
# Open the command line interface and tell PIP to download the package you want.
#
# Navigate your command line to the location of Python's script directory, and type the following:

pip install Camelcase - This will install the camelcase package
"""

import camelcase

c = camelcase.CamelCase()
d = "hello world"

print(c.hump(d))

from humps.camel import case
print(case('madhu 2mallidi hyderabad'))

from excel import OpenExcel
f = OpenExcel('TEST.xlsx')
print(f.read('A')) # read 'A' row

