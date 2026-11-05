# Theoretical results
Baseline: p* = 1%, gamma = 1.1, p0 = 10%, n = 2000, spread = 2.7 x p
Largest understatement in percentage points at p = 3.86%

## Long-run estimate, spread and detection (Sections 3 and 6)
m/n = 0.5: estimate 0.903%, spread 244 bp, relative bias 9.7%, tail events to detect 785 (8/delta^2 = 858)
m/n = 1: estimate 0.819%, spread 221 bp, relative bias 18.1%, tail events to detect 208 (8/delta^2 = 243)
m/n = 2: estimate 0.680%, spread 183 bp, relative bias 32.0%, tail events to detect 59 (8/delta^2 = 78)
p* = 0.5%: spread at m/n = 0, 1, 5: 135, 106, 51 bp
p* = 1.0%: spread at m/n = 0, 1, 5: 270, 221, 115 bp
p* = 2.0%: spread at m/n = 0, 1, 5: 540, 465, 265 bp

## Table 2: long-run estimate (percent) at m/n = 0.5, 1, 2
Baseline                           0.90  0.82  0.68
Simulated, n = 2,000               0.91  0.82  0.68
Simulated, n = 200                 0.91  0.84  0.71
gamma = 1.05                       0.95  0.90  0.81
gamma = 1.20                       0.84  0.71  0.53
gamma = 0.95                       1.06  1.13  1.28
p0 = 5%                            0.93  0.86  0.74
p0 = 20%                           0.88  0.78  0.63
Correlated real draws              0.91  0.82  0.69
Ratio varying by year              0.91  0.83  0.69
Synthetic draws weighted one half  0.95  0.90  0.82
Standard deviation of the estimate, m/n = 1, n = 2000: 0.21%
Standard deviation of the estimate, m/n = 1, n = 200: 0.69%
Figure 2, version 15, m/n = 1: mean 222 bp, 5th-95th percentiles 135-324 bp, expected path 221 bp
Spread under Lane (2000) pricing, p* = 0.5%, m/n = 1: 12.5% below the true spread
Spread under Lane (2000) pricing, p* = 1.0%, m/n = 1: 10.7% below the true spread
Spread under Lane (2000) pricing, p* = 2.0%, m/n = 1: 8.5% below the true spread

## Accuracy and the synthetic share (Section 7)
RMSE by m/n: 0: 0.223%, 0.1: 0.226%, 0.2: 0.231%, 0.3: 0.235%, 0.4: 0.240%, 0.5: 0.245%, 0.75: 0.261%, 1: 0.280%
m/n = 0: standard deviation of the estimate 0.223%, standard error the firm perceives 0.224%, standard deviation of the change between versions 0.070%
m/n = 1: standard deviation of the estimate 0.214%, standard error the firm perceives 0.143%, standard deviation of the change between versions 0.113%

## Costly real data (Sections 4 and 6)
Two states for cutoffs between 66 and 221 bp; cutoff 162 bp
20-year calm from year 10: maintenance stops in year 21; spread after the calm 66 bp; restored after the cluster in year 45
1000 observations a year, rho = 0.0: share data-poor at the end of the calm / 40 years later: no calm 0.00/0.01, 10 years 0.27/0.84, 20 years 1.00/1.00
1000 observations a year, rho = 0.005: share data-poor at the end of the calm / 40 years later: no calm 0.18/0.42, 10 years 0.52/0.82, 20 years 0.96/0.93
1000 observations a year, rho = 0.02: share data-poor at the end of the calm / 40 years later: no calm 0.39/0.48, 10 years 0.59/0.54, 20 years 0.88/0.54
100 observations a year, rho = 0.0: share data-poor at the end of the calm / 40 years later: no calm 0.36/0.52, 10 years 0.63/0.64, 20 years 0.96/0.66
100 observations a year, rho = 0.005: share data-poor at the end of the calm / 40 years later: no calm 0.40/0.51, 10 years 0.64/0.56, 20 years 0.93/0.58
100 observations a year, rho = 0.02: share data-poor at the end of the calm / 40 years later: no calm 0.44/0.47, 10 years 0.63/0.48, 20 years 0.86/0.49
