# SDV synthesizers: other settings (median over 3 seeds)
model | P(>x0) | h(1%) | h(0.5%) | h(0.2%) | implied gamma (1%) | Hill top 10% | max
CTGAN, 1,000 epochs | 0.091 | 0.0086 | 0.0042 | 0.0005 | 1.06 | 1.43 | 84
TVAE, 1,000 epochs | 0.075 | 0.0058 | 0.0003 | 0.0000 | 1.24 | 1.62 | 82
copula, normal marginal | 0.401 | 0.0037 | 0.0001 | 0.0000 | 1.43 | 4.33 | 45
copula, gamma marginal | 0.000 | 0.0000 | 0.0000 | 0.0000 | inf | 6.72 | 14
copula, kernel marginal | 0.133 | 0.0092 | 0.0046 | 0.0022 | 1.03 | 1.60 | 263
