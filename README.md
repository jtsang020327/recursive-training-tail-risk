# Replication package

Xiwen Zhao, "Recursive Training on Synthetic Data and Tail-Risk Pricing"

## Requirements

Python 3.11 with the packages in `requirements.txt`, and R to extract the data.

```
pip install -r requirements.txt
bash run_all.sh
```

`run_all.sh` takes about two hours, almost all of it in `sdv_models.py`.

## Files

| Script | Produces |
|---|---|
| `data/get_danish_data.sh` | `data/danish.csv` |
| `code/empirical/textbook_models.py` | Section 5: GAN, VAE and Gaussian mixture |
| `code/empirical/sdv_models.py` | Section 5: CTGAN, TVAE and Gaussian copula |
| `code/empirical/evidence_figure.py` | Figure 1, Table 1 |
| `code/theory_figures.py` | Figures 2-4 |
| `code/theory_results.py` | Table 2 and the theoretical numbers in the text |

`code/model.py` contains the model and `code/empirical/common.py` the data, thresholds and
textbook models. Figures are written to `output/figures` and numbers to `output/results`.

## Data

Danish fire insurance losses, 1980-1990 (2,167 losses above DKK 1 million), from the CRAN
package evir, version 1.7-4 (GPL-2). The script downloads them; they are not redistributed here.

## Notes

Seeds are fixed. The theory scripts run in under a minute and reproduce the numbers in the
paper exactly. Results from the neural networks may differ slightly across hardware and
library versions.
