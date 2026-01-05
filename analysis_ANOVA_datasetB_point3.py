import numpy as np
import scipy.stats as stats

# Mock data reconstruction based on paper context
# Group B, point 3 was the outlier
np.random.seed(42)
group_A = np.random.normal(10, 2, 20)
group_B = np.random.normal(12, 2, 20)
group_B[3] = 25.0 
group_C = np.random.normal(10.5, 2, 20)

# Exclude outlier (index 3)
group_B_clean = np.delete(group_B, 3)

# One-way ANOVA
f_stat, p_value = stats.f_oneway(group_A, group_B_clean, group_C)
df_between = 2
df_within = len(group_A) + len(group_B_clean) + len(group_C) - 3
