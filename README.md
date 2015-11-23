# Density_Sampling

Overview
--------

For a data-set comprising a mixture of rare and common populations, density sampling gives equal weights 
to selected representatives of those distinct populations.

Density sampling is a balancing act between signal and noise. Indeed, while it increases the prevalence of rare populations, it also increases the prevalence of noisy sample points that would happen to have their local densities larger than an outlier density computed by density sampling.

More specifically, density sampling proceeds as follows:
* For each sample point of the data-set 'data', estimate a local density in feature space by counting the number of neighboring data-points within a particular region centered around that sample point.
* The ``i``-th sample point of the data-set is selected by density sampling with a probability given by:
```
                                  | 0 if outlier_density > LD[i];
    P(keep the i-th data-point) = | 1 if outlier_density <= LD[i] <= target_density;
                                  | target_density / LD[i] if LD[i] > target_density.
```                                      
Here ``LD[i]`` denotes the local density of the ``i``-th sample point of the data-set, whereas ``outlier_density`` and ``target_density`` are computed as particular percentiles of the distribution of local densities.

Installation and Requirements
-----------------------------

Density_Sampling is written in Python 2.7 and requires the following packages, along with a few modules 
from the Python Standard Library:
* NumPy >= 1.9.0
* scikit-learn
* setuptools

Having ascertained that those requirements are met and having checked that the afore-mentioned libraries are up and running, you can install Density_Sampling from the Python Package Index (PyPI) in two simple steps:
* open a terminal emulator window to interact with the Shell (KDE ``konsole`` or GNOME ``terminal``); 
* enter the command: ``pip install Density_Sampling``

Usage
-----

More information on the inner workings of density sampling can be gained from the docstrings of the functions making up this module.

The following few lines illustrate density sampling on the Iris data-set from the UCI Machine Learning repository. Instead of copying those lines into a Python interpreter console, a similar exemple can be run automatically via Python's doctest's functionality. Simply locate the directory holding the file ``Density_Sampling.py``, change it to your current working directory and then type ``python Density_Sampling.py`` at the command line.

```
>>> from sklearn import datasets

>>> iris = datasets.load_iris()
>>> Y = iris.target

>>> from sklearn.decomposition import PCA

>>> X_reduced = PCA(n_components = 3).fit_transform(iris.data)

>>> import matplotlib.pyplot as plt
>>> from mpl_toolkits.mplot3d import Axes3D
>>> from time import sleep

>>> def plot_PCA(X_reduced, Y, title):
    fig = plt.figure(1, figsize = (10, 8))
    ax = Axes3D(fig, elev = -150, azim = 110)
    
    ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], 
               c = Y, cmap = plt.cm.Paired)
                   
    ax.set_title('First three PCA direction for {title}'.format(**locals()))
    ax.set_xlabel('1st eigenvector')
    ax.w_xaxis.set_ticklabels([])
    ax.set_ylabel('2nd eigenvector')
    ax.w_yaxis.set_ticklabels([])
    ax.set_zlabel('3rd eigenvector')
    ax.w_zaxis.set_ticklabels([])
        
    plt.show(block = False)
    sleep(3)
    plt.close()
    
>>> plot_PCA(X_reduced, Y, 'the whole Iris data-set')

>>> import Density_Sampling
>>> sampled_indices = Density_Sampling.density_sampling(X_reduced, 
                        metric = 'euclidean', desired_samples = 50)
                        
>>> downsampled_X_reduced = X_reduced[sampled_indices, :]
>>> downsampled_Y = Y[sampled_indices]

>>> plot_PCA(downsampled_X_reduced, downsampled_Y, 
             'the Iris data-set\ndown-sampled to about 50 samples')
```

Reference
---------

Giecold, G., Marco, E., Trippa, L. and Yuan, G.-C., "Robust Inference of Cell Lineages", submitted for publication.
