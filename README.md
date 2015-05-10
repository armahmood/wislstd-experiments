# WIS-LSTD Experiments

The main purpose of this project is to provide the python implementation of WIS-LSTD introduced by Mahmood, van Hasselt and Sutton (2014). Additionally, it also provides a random walk experiment to illustrate the usage of this algorithm.

It can be imported as an Eclipse Pydev project. 

Its main experiment file is located at pysrc/experiments/stdrwexp.py

An example of running an experiment from the command prompt is as follows:

python ./pysrc/experiments/stdrwexp.py 1 StdRWSparseReward ./results/wislstdexperiments/wislstd/

##References

Mahmood, A.R., van Hasselt, H., Sutton, R.S. (2014). Weighted importance sampling for off-policy learning with linear function approximation. *Advances in Neural Information Processing Systems 27*.
