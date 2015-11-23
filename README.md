# Density_Sampling

Overview
--------

For a data-set comprising a mixture of rare and common populations, density sampling gives equal weights 
to selected representatives of those distinct populations.

Density sampling is a balancing act between signal and noise, for while it increases the prevalence of rare populations, 
it also increases the prevalence of noisy sample points which happen to have their local densities larger than 
an outlier density computed by density sampling.

Installation and Requirements
-----------------------------

Density_Sampling is written in Python 2.7 and requires the following packages, along with a few modules 
from the Standard Library:
* NumPy >= 1.9.0
* scikit-learn
* setuptools

Once you are sure that those requirements are met and have checked that those packages are up and running, you can 
install Density_Sampling from the Python Package Index (PyPI) as follows:
* open a terminal window;
* type in the command: ``pip install Density_Sampling``


