import numpy as np

input = [.7, .9, .5, .4]
weights = [[.2, .3, .4, .2],
           [.6, .2, .9, .4],
           [.6, .3, .7, .5]]
bias = [.6, .8, .4]

print(np.dot(weights, input) + bias)