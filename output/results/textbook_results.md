# Textbook generative models and the tail of Danish fire losses
Real: n = 2167, x0 = 5.54, u(1.0%) = 26.04, u(0.5%) = 34.82, u(0.2%) = 57.02, Hill top 10% = 1.40, max = 263
Bootstrap 90% interval for the real Hill index: 1.26-1.56

## One round, log losses (median over 5 seeds)
model | P(>x0) | h(1%) | h(0.5%) | h(0.2%) | implied gamma (1%) | Hill top 10% | max
GAN | 0.099 | 0.0110 | 0.0069 | 0.0030 | 0.96 | 1.45 | 1933
VAE | 0.093 | 0.0088 | 0.0051 | 0.0019 | 1.05 | 1.51 | 773
Gaussian mixture | 0.097 | 0.0115 | 0.0061 | 0.0016 | 0.94 | 1.32 | 361

## One round, raw losses (median over 5 seeds)
model | P(>x0) | h(1%) | h(0.5%) | h(0.2%) | implied gamma (1%) | Hill top 10% | max
GAN | 0.085 | 0.0085 | 0.0033 | 0.0002 | 1.07 | 1.40 | 92
VAE | 0.098 | 0.0026 | 0.0010 | 0.0001 | 1.59 | 2.24 | 91
Gaussian mixture | 0.076 | 0.0273 | 0.0196 | 0.0060 | 0.56 | 1.13 | 137

## Robustness, log losses (median over 3 seeds)
model | P(>x0) | h(1%) | h(0.5%) | h(0.2%) | implied gamma (1%) | Hill top 10% | max
GAN, width 32 | 0.089 | 0.0117 | 0.0074 | 0.0031 | 0.93 | 1.40 | 944
GAN, width 128 | 0.090 | 0.0105 | 0.0066 | 0.0029 | 0.98 | 1.42 | 1389
GAN, noise dimension 2 | 0.098 | 0.0107 | 0.0065 | 0.0026 | 0.97 | 1.44 | 1301
GAN, noise dimension 8 | 0.104 | 0.0114 | 0.0072 | 0.0031 | 0.94 | 1.46 | 902
mixture, 2 components | 0.132 | 0.0037 | 0.0013 | 0.0001 | 1.43 | 2.07 | 147
mixture, 5 components | 0.097 | 0.0119 | 0.0064 | 0.0018 | 0.92 | 1.34 | 331

## Recursive training, log losses (m/n = 1: 8 generations, 3 seeds; m/n = 0.5 and 2: 6 generations, 2 seeds)
GAN, m/n = 1.0: one-round ratio 1.40, Proposition 1 fixed point 1.686%, simulated long run 1.192%
GAN, m/n = 0.5: one-round ratio 1.16, Proposition 1 fixed point 1.103%, simulated long run 1.005%
GAN, m/n = 2.0: one-round ratio 1.16, Proposition 1 fixed point 1.490%, simulated long run 1.218%
VAE, m/n = 1.0: one-round ratio 0.85, Proposition 1 fixed point 0.883%, simulated long run 0.838%
VAE, m/n = 0.5: one-round ratio 0.89, Proposition 1 fixed point 0.961%, simulated long run 0.862%
VAE, m/n = 2.0: one-round ratio 0.89, Proposition 1 fixed point 0.828%, simulated long run 0.723%
Gaussian mixture, m/n = 1.0: one-round ratio 1.11, Proposition 1 fixed point 1.138%, simulated long run 1.090%
Gaussian mixture, m/n = 0.5: one-round ratio 1.15, Proposition 1 fixed point 1.100%, simulated long run 0.974%
Gaussian mixture, m/n = 2.0: one-round ratio 1.15, Proposition 1 fixed point 1.466%, simulated long run 1.256%

Total time 543s
