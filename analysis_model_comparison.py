import pandas as pd

# Metric computation based on likelihoods (mocked here for reproduction)
data = {
    'Model': ['Gauss-Bonnet Leakage', 'Massive Neutrinos', 'Early Dark Energy', 'Modified Recombination'],
    'Delta_Chi2': [-10.2, -2.1, -5.4, -4.8],
    'k_params': [2, 1, 3, 2]
}
df = pd.DataFrame(data)
df['AIC'] = df['Delta_Chi2'] + 2 * df['k_params']
# Assuming N_eff = 1500 for high-l tail
df['BIC'] = df['Delta_Chi2'] + df['k_params'] * 7.31 

print(df)