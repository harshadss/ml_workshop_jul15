# Entropy through example
from scipy import stats

help(stats.entropy)

# Check for balanced coin toss
stats.entropy([0.5, 0.5])

# Check for unbalanced coin toss
stats.entropy([0.2, 0.8])

# Check for our earlier example
(pois_dist, bins) = np.histogram(pois_rand, bins = [0, 0.25, 0.5, 1])

stats.entropy(pois_dist)


