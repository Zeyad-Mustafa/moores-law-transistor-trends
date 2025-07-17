def calculate_halving_period(df):
    import numpy as np
    from scipy.stats import linregress

    log_size = np.log2(df["Transistor Size (nm)"])
    slope, intercept, r_value, _, _ = linregress(df["Year"], log_size)
    halving_time = -1 / slope
    return halving_time, r_value**2
