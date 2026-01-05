import numpy as np
import scipy.stats as stats

def grubbs_test(data, alpha=0.05):
    n = len(data)
    mean = np.mean(data)
    std = np.std(data, ddof=1)
    numerator = np.max(np.abs(data - mean))
    G = numerator / std
    t_dist = stats.t.ppf(1 - alpha / (2 * n), n - 2)
    numerator_crit = (n - 1) * np.sqrt(np.square(t_dist))
    denominator_crit = np.sqrt(n) * np.sqrt(n - 2 + np.square(t_dist))
    G_crit = numerator_crit / denominator_crit
    return G, G_crit, G > G_crit

# Mock data for validation
data = np.random.normal(12, 2, 20)
data[3] = 25.0 