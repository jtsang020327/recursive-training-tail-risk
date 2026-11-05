"""Table 2 and the theoretical numbers quoted in Sections 3, 4, 6, 7 and 8."""
from functools import partial
from pathlib import Path

import numpy as np

from model import (PSTAR, BP, N_REAL, GAMMA, P0, WIN_H, P_CUT, M_SYN, OBS_PER_YEAR,
                   h_tail_index, fixed_point, simulate, maintenance_path, maintenance_simulate,
                   detection_events)

OUT = Path(__file__).resolve().parents[1] / "output" / "results"
OUT.mkdir(parents=True, exist_ok=True)
lines = []


def out(s=""):
    print(s)
    lines.append(s)


def pct(p):
    return f"{100 * p:.2f}"


out("# Theoretical results")
out(f"Baseline: p* = {PSTAR:.0%}, gamma = {GAMMA}, p0 = {P0:.0%}, n = {N_REAL}, spread = 2.7 x p")
out(f"Largest understatement in percentage points at p = {P0 * GAMMA ** (-1 / (GAMMA - 1)):.2%}")
out()

out("## Long-run estimate, spread and detection (Sections 3 and 6)")
for r in [0.5, 1, 2]:
    p = fixed_point(r)
    d = 1 - p / PSTAR
    out(f"m/n = {r}: estimate {p:.3%}, spread {p * BP:.0f} bp, relative bias {d:.1%}, "
        f"tail events to detect {detection_events(d):.0f} (8/delta^2 = {8 / d ** 2:.0f})")
for ps in [0.005, 0.01, 0.02]:
    out(f"p* = {ps:.1%}: spread at m/n = 0, 1, 5: "
        + ", ".join(f"{fixed_point(r, ps) * BP:.0f}" for r in [0, 1, 5]) + " bp")
out()

out("## Table 2: long-run estimate (percent) at m/n = 0.5, 1, 2")


def sim_mean(n, r, seed, rho=0.0):
    return simulate(n, int(round(r * n)), 300, 4000, seed=seed, rho=rho)[50:].mean()


def varying_ratio(r, seed=3, T=200_000):
    rng = np.random.default_rng(seed)
    p, acc = PSTAR, []
    for t in range(T):
        w = 1 / (1 + rng.uniform(0.5 * r, 1.5 * r))
        p = w * PSTAR + (1 - w) * float(h_tail_index(p))
        if t > 100:
            acc.append(p)
    return np.mean(acc)


R3 = [0.5, 1.0, 2.0]
rows = [
    ("Baseline", [fixed_point(r) for r in R3]),
    ("Simulated, n = 2,000", [sim_mean(2000, r, 21 + i) for i, r in enumerate(R3)]),
    ("Simulated, n = 200", [sim_mean(200, r, 31 + i) for i, r in enumerate(R3)]),
    ("gamma = 1.05", [fixed_point(r, h=partial(h_tail_index, gamma=1.05)) for r in R3]),
    ("gamma = 1.20", [fixed_point(r, h=partial(h_tail_index, gamma=1.20)) for r in R3]),
    ("gamma = 0.95", [fixed_point(r, h=partial(h_tail_index, gamma=0.95)) for r in R3]),
    ("p0 = 5%", [fixed_point(r, h=partial(h_tail_index, p0=0.05)) for r in R3]),
    ("p0 = 20%", [fixed_point(r, h=partial(h_tail_index, p0=0.20)) for r in R3]),
    ("Correlated real draws", [sim_mean(2000, r, 41 + i, rho=0.02) for i, r in enumerate(R3)]),
    ("Ratio varying by year", [varying_ratio(r) for r in R3]),
    ("Synthetic draws weighted one half", [fixed_point(0.5 * r) for r in R3]),
]
for name, ps in rows:
    out(f"{name:34s} " + "  ".join(pct(p) for p in ps))
for n in [2000, 200]:
    s = simulate(n, n, 300, 4000, seed=99)[50:]
    out(f"Standard deviation of the estimate, m/n = 1, n = {n}: {s.std():.2%}")
f2 = simulate(N_REAL, N_REAL, 15, 20000, seed=11)
lo, hi = np.percentile(f2[15], [5, 95])
out(f"Figure 2, version 15, m/n = 1: mean {f2[15].mean() * BP:.0f} bp, 5th-95th percentiles "
    f"{lo * BP:.0f}-{hi * BP:.0f} bp, expected path {fixed_point(1.0) * BP:.0f} bp")
# Lane (2000): spread = expected loss + 0.5551 PFL^0.4946 CEL^0.5741, with CEL = 1
lane = lambda p: p + 0.5551 * p ** 0.4946
for ps in (0.005, 0.01, 0.02):
    out(f"Spread under Lane (2000) pricing, p* = {ps:.1%}, m/n = 1: "
        f"{1 - lane(fixed_point(1.0, ps=ps)) / lane(ps):.1%} below the true spread")
out()

out("## Accuracy and the synthetic share (Section 7)")
grid = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.75, 1.0]
rmse = [np.sqrt(np.mean((simulate(N_REAL, int(round(r * N_REAL)), 400, 4000,
                                  seed=int(100 * r) + 1)[100:] - PSTAR) ** 2)) for r in grid]
out("RMSE by m/n: " + ", ".join(f"{r:g}: {e:.3%}" for r, e in zip(grid, rmse)))
for r in [0, 1.0]:
    m = int(round(r * N_REAL))
    s = simulate(N_REAL, m, 400, 4000, seed=7)[100:]
    se = np.sqrt(s.mean() / (N_REAL + m))
    out(f"m/n = {r:g}: standard deviation of the estimate {s.std():.3%}, standard error the firm "
        f"perceives {se:.3%}, standard deviation of the change between versions "
        f"{np.diff(s, axis=0).std():.3%}")
out()

out("## Costly real data (Sections 4 and 6)")
n_hi, n_lo = OBS_PER_YEAR * WIN_H, OBS_PER_YEAR * 2
out(f"Two states for cutoffs between {fixed_point(M_SYN / n_lo) * BP:.0f} and "
    f"{fixed_point(M_SYN / n_hi) * BP:.0f} bp; cutoff {P_CUT * BP:.0f} bp")
ps = np.full(WIN_H + 76, PSTAR)
ps[WIN_H + 10:WIN_H + 30] = 0.005
est, kept = maintenance_path(ps, extra_events={WIN_H + 45: 9}, p_init=fixed_point(1.0))
stop = int(np.argmax(~kept))
out(f"20-year calm from year 10: maintenance stops in year {stop}; spread after the calm "
    f"{est[44] * BP:.0f} bp; restored after the cluster in year 45")
for q in [1000, 100]:
    for rho in [0.0, 0.005, 0.02]:
        res = []
        for L in [0, 10, 20]:
            path_ps = np.full(WIN_H + 20 + L + 40, PSTAR)
            path_ps[WIN_H + 20:WIN_H + 20 + L] = 0.005
            _, k = maintenance_simulate(path_ps, 4000, m=20 * q, q=q, rho=rho, seed=11 + L)
            res.append((np.mean(~k[20 + L - 1]), np.mean(~k[-1])))
        out(f"{q} observations a year, rho = {rho}: share data-poor at the end of the calm / 40 years "
            f"later: no calm {res[0][0]:.2f}/{res[0][1]:.2f}, 10 years {res[1][0]:.2f}/"
            f"{res[1][1]:.2f}, 20 years {res[2][0]:.2f}/{res[2][1]:.2f}")

(OUT / "theory_results.md").write_text("\n".join(lines) + "\n")
