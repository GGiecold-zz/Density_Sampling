# Density_Sampling

Overview
--------

For a data-set comprising a mixture of rare and common populations, density sampling gives equal weights 
to selected representatives of those distinct populations.

Density sampling is a balancing act between signal and noise, for while it increases the prevalence of rare populations, 
it also increases the prevalence of noisy sample points which happen to have their local densities larger than 
an outlier density computed by density sampling.

Density sampling proceeds as follows:
* For each sample point of the data-set 'data', estimate a local density in feature space by counting the number of neighboring data-points within a particular region centered around this sample point.
* The ``i``-th sample point of the data-set 'data' is selected by density sampling with a probability given by:
        
                                      | ``0`` if ``outlier_density > LD[i]``;
        P(keep the i-th data-point) = | ``1`` if ``outlier_density <= LD[i] <= target_density``;
                                      | ``target_density / LD[i]`` if ``LD[i] > target_density``.
    
Here ``LD[i]`` denotes the local density of the ``i``-th sample point of the data-set, whereas ``outlier_density`` and ``target_density`` are computed as particular percentiles of the distribution of local densities.

Installation and Requirements
-----------------------------

Density_Sampling is written in Python 2.7 and requires the following packages, along with a few modules 
from the Standard Library:
* NumPy >= 1.9.0
* scikit-learn
* setuptools

Once you are sure that those requirements are met and have checked that those packages are up and running, you can 
install Density_Sampling from the Python Package Index (PyPI) in two simple steps:
* open a terminal window;
* type in the command: ``pip install Density_Sampling``

Usage
-----



Reference
---------

Giecold, G., Marco, E., Trippa, L. and Yuan, G.-C., "Robust Inference of Cell Lineages", submitted for publication.


