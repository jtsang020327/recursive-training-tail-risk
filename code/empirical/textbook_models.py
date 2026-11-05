"""Section 5: a standard GAN, a VAE and a Gaussian mixture, trained on the Danish losses."""
import json
import time

import numpy as np

import common as C

HEAD = "model | P(>x0) | h(1%) | h(0.5%) | h(0.2%) | implied gamma (1%) | Hill top 10% | max"


def row(name, d):
    return (f"{name} | {d['ref']:.3f} | {d['h0.01']:.4f} | {d['h0.005']:.4f} | "
            f"{d['h0.002']:.4f} | {d['gamma0.01']:.2f} | {d['hill10']:.2f} | {d['max']:.0f}")


def main():
    t0 = time.time()
    out = C.Log("textbook_results")
    out("# Textbook generative models and the tail of Danish fire losses")
    out(f"Real: n = {C.N_REAL}, x0 = {C.X0:.2f}, "
        + ", ".join(f"u({p:.1%}) = {C.U[p]:.2f}" for p in C.PS)
        + f", Hill top 10% = {C.real['hill10']:.2f}, max = {C.real['max']:.0f}")
    rng = np.random.default_rng(0)
    hb = [C.hill(rng.choice(C.x_real, C.N_REAL), 0.10) for _ in range(1000)]
    out(f"Bootstrap 90% interval for the real Hill index: "
        f"{np.percentile(hb, 5):.2f}-{np.percentile(hb, 95):.2f}")
    out()

    one = {}
    for log in [True, False]:
        spec = "log losses" if log else "raw losses"
        out(f"## One round, {spec} (median over 5 seeds)")
        out(HEAD)
        for name in C.TEXTBOOK:
            st = [C.tail_stats(C.textbook_sample(name, C.x_real, s, log=log)) for s in range(1, 6)]
            one[f"{name} | {spec}"] = {"runs": st, "median": C.median_stats(st)}
            out(row(name, C.median_stats(st)))
        out()
    json.dump(one, open(C.RES / "textbook_one_round.json", "w"), indent=1)

    out("## Robustness, log losses (median over 3 seeds)")
    out(HEAD)
    for name, kw, lab in [("GAN", {"hidden": 32}, "GAN, width 32"),
                          ("GAN", {"hidden": 128}, "GAN, width 128"),
                          ("GAN", {"zdim": 2}, "GAN, noise dimension 2"),
                          ("GAN", {"zdim": 8}, "GAN, noise dimension 8"),
                          ("Gaussian mixture", {"K": 2}, "mixture, 2 components"),
                          ("Gaussian mixture", {"K": 5}, "mixture, 5 components")]:
        st = [C.tail_stats(C.textbook_sample(name, C.x_real, s, **kw)) for s in range(1, 4)]
        out(row(lab, C.median_stats(st)))
    out()

    out("## Recursive training, log losses (m/n = 1: 8 generations, 3 seeds; "
        "m/n = 0.5 and 2: 6 generations, 2 seeds)")
    rec = {}
    for name in C.TEXTBOOK:
        def fn(x, s, name=name):
            return C.textbook_sample(name, x, s)
        for ratio, gens, seeds in [(1.0, 8, [11, 12, 13]), (0.5, 6, [21, 22]), (2.0, 6, [21, 22])]:
            paths = [C.recursion(fn, s, gens, ratio) for s in seeds]
            rec[f"{name} | m/n={ratio}"] = paths
            p = paths[0]["estimate"][0]
            theta = np.mean([q["h"][0] for q in paths]) / p
            longrun = np.mean([q["estimate"][-3:] for q in paths])
            out(f"{name}, m/n = {ratio}: one-round ratio {theta:.2f}, Proposition 1 fixed point "
                f"{100 * p / (1 + ratio * (1 - theta)):.3f}%, simulated long run {100 * longrun:.3f}%")
    json.dump(rec, open(C.RES / "textbook_recursion.json", "w"), indent=1)
    out()
    out(f"Total time {time.time() - t0:.0f}s")
    out.save()


if __name__ == "__main__":
    main()
