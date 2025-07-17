import pandas as pd
from src.visualize import plot_interactive
from src.analyze import calculate_halving_period

def main():
    df = pd.read_csv("data/transistor_sizes.csv")
    plot_interactive(df)
    halving_time, r2 = calculate_halving_period(df)
    print(f"Estimated halving period: {halving_time:.2f} years")
    print(f"Regression R²: {r2:.2f}")

if __name__ == "__main__":
    main()
