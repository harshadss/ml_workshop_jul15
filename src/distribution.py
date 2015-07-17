# Let's see some code now!

import numpy as np

# Generate random numbers from uniform
unif_rand = np.random.uniform(size = 1000)

# Random numbers from poisson
pois_rand = np.random.poisson(5, size = 1000)

# Check histogram: spread of probability (which is just proportion!)
print np.histogram(unif_rand, bins = [0, 0.25, 0.5, 1])

print np.histogram(pois_rand, bins = [0, 5, 10, 50, 100])

# Check which other distributions are available?
print dir(np.random)

