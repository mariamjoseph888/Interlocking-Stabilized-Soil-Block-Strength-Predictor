# Interlocking-Stabilized-Soil-Block-Strength-Predictor

This app predicts the strength of Interlocking Stabilized Soil Blocks (ISSBs) using input cement and lime percentages.

## How to Run

1. Clone this repository.
2. Install Python 3 and dependencies (`pip install -r requirements.txt`).
3. Start the web app: `streamlit run web_app.py`.

## Calculation

- Block strength: `fcb1 = 2.283 * (cement - (3 * lime / 761)) - 9.995`
- Wall strength: `fcw2 = 2.64 * fcb1 + 0.08`

## Reference

- Based on formulas derived in the resarch paper [ Fundi, S.I., Kaluli, J.W., and Kinuthia, J., (2021),
- “Finite Element Modelling of Interlocking Stabilised Laterite Soil Block Walls,”
-  SN Applied Sciences, Springer, Vol. 3, Article  225  (2021)].

## Contact

- Author: Mariam Osbert




