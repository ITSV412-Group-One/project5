from setuptools import setup

setup(
  name = 'test',
  version = '1.0',
  
  #insert whatever py file this will use
  py_modules = ['test'],
  
  install_requires = ['Click', ],
  
  #not sure what this is but hello stuff needs to be changed for our specifics
  entry_points = '''
       [console_scripts]
       hello=hello:cli
  '''
)