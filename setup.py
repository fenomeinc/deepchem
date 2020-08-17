import sys
import time
from setuptools import setup, find_packages

if '--nightly' in sys.argv:
  release = False
  sys.argv.remove('--nightly')
else:
  # Build a non-nightly package by default.
  release = True

if release:
  project_name = 'deepchem'
else:
  project_name = 'deepchem-nightly'


# get the version from deepchem/__init__.py
def _get_version():
  with open('deepchem/__init__.py') as fp:
    for line in fp:
      if line.startswith('__version__'):
        g = {}
        exec(line, g)
        if project_name == "deepchem":
          return g['__version__']
        else:
          # nightly version string .devYearMonthDayHourMinute
          base = g['__version__']
          dev_version = ".dev" + time.strftime("%Y%m%d%H%M%S")
          return base + dev_version

    raise ValueError('`__version__` not defined in `deepchem/__init__.py`')


setup(
    name=project_name,
    version=_get_version(),
    url='https://github.com/deepchem/deepchem',
    maintainer='DeepChem contributors',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    license='MIT',
    description='Deep learning models for drug discovery, \
        quantum chemistry, and the life sciences.',
    keywords=[
        'deepchem',
        'chemistry',
        'biology',
        'materials-science',
        'life-science',
        'drug-discovery',
    ],
    packages=find_packages(exclude=["*.tests"]),
    project_urls={
        'Documentation': 'https://deepchem.readthedocs.io/en/latest/',
        'Source': 'https://github.com/deepchem/deepchem',
    },
    install_requires=[
        'joblib',
        'numpy',
        'pandas',
        'scikit-learn',
        'scipy',
    ],
    python_requires='>=3.5')
