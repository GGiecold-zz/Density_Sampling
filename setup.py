#!/usr/bin/env python


# Density_Sampling/setup.py;

# Author: Gregory Giecold for the GC Yuan Lab
# Affiliation: Harvard University
# Contact: g.giecold@gmail.com, ggiecold@jimmy.harvard.edu


"""Setup script for Density_Sampling. For a dataset comprising a mixture 
of rare and common populations, density sampling gives equal weights 
to selected representatives of those distinct populations.

Density sampling is a balancing act between signal and noise, for while 
it increases the prevalence of rare populations, it also increases the prevalence 
of noisy sample points which happen to have their local densities larger than
an outlier density computed by Density_Sampling.

Reference
---------
Giecold, G., Marco, E., Trippa, L. and Yuan, G.-C., 
"Robust Inference of Cell Lineages", submitted for publication.
"""


from codecs import open
from os import path
from sys import version
from setuptools import setup, find_packages
    
    
here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README'), encoding = 'utf-8') as f:
    long_description = f.read()
    

setup(name = 'Density_Sampling',
      version = '1.1',
      
      description = 'For a dataset comprising a mixture of rare and common populations, density sampling gives equal weights to the representatives of those distinct populations.',
      long_description = long_description,
                    
      url = 'https://github.com/GGiecold/Density_Sampling',
      download_url = 'https://github.com/GGiecold/Density_Sampling',
      
      author = 'Gregory Giecold',
      author_email = 'g.giecold@gmail.com',
      maintainer = 'Gregory Giecold',
      maintainer_email = 'ggiecold@jimmy.harvard.edu',
      
      license = 'MIT License',
      
      packages = find_packages(),
      
      py_modules = ['Density_Sampling'],
      platforms = ('Any',),
      install_requires = ['numpy>=1.9.0', 'setuptools', 'sklearn'],
                          
      classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'Intended Audience :: End Users/Desktop',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Science/Research',          
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Operating System :: MacOS :: MacOS X',
                   'Operating System :: POSIX',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Scientific/Engineering :: Visualization',
                   'Topic :: Scientific/Engineering :: Mathematics', ],
                   
      keywords = 'data-analysis data-mining downsampling sampling statistics subsampling',    
)
