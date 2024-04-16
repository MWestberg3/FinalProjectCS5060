import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from fitter import Fitter
from scipy.stats import burr

def graph_employment(csv_file: str) -> None:

    # Load the CSV file into a DataFrame
    data = pd.read_csv(csv_file)

    # Flatten the data into a single column
    values = data.iloc[:, 1:].values.flatten()

    # Create a corresponding index for the flattened data
    years = data['Year'].values
    months = data.columns[1:]
    index = [f"{year}-{month}" for year in years for month in months]

    # Plot the data
    plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
    plt.plot(index, values)

    # Add labels and title
    plt.xticks([])
    plt.xlabel("Time (Jan 2014 - Present)")
    plt.ylabel("All Employees, Thousands")
    plt.title("Employment in Tech (U.S.)")

    # Show plot
    plt.grid(True)
    plt.tight_layout()
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.show()

def flatten_csv(csv_file: str) -> list:
    data = np.genfromtxt(csv_file, 
                         delimiter=',', 
                         skip_header=1,
                         usecols=range(1,13))
    flattened_data = data[~np.isnan(data)].flatten()

    return flattened_data

def calculate_volatility(data: list) -> float:
    returns = np.diff(data) / data[:-1] # Calculate Returns
    volatility = np.std(returns) * np.sqrt(252)
    return volatility

def calculate_drift(data: list) -> float:
    delta = np.diff(data)
    drift = delta.mean()
    return drift

def graph_best_fit(data: list) -> dict:
    delta = np.diff(data)

    sns.set_style('white')
    sns.set_context('paper', font_scale=2)

    sns.histplot(delta, kde=False)

    f = Fitter(delta, distributions=['gamma',
                                    'lognorm',
                                    'burr',
                                    'norm'])
    
    f.fit()
    f.summary()

    plt.xlabel('All Employees, Thousands')
    plt.ylabel('Frequency')
    plt.title('All Employees (Thousands) Over Time')
    plt.show()

    best_fit = f.get_best(method='sumsquare_error')
    print(f'Employee Outlook Best Fit: {best_fit}')

    return best_fit

class European_Call_Payoff:
    def __init__(self, strike: float):
        self.strike = strike

    def get_payoff(self, employment_rate: float) -> float:
        if employment_rate > self.strike:
            return employment_rate - self.strike
        else:
            return 0
        
class Gamma_motion:
    def simulate_paths(self):
        while (self.T - self.dt > 0):
            dWt = np.random.gamma(shape=self.shape, scale=self.scale,) + self.loc # Gamma motion with shift to left of self.loc
            dYt = self.drift * self.dt + self.volatility * dWt # Change in employment
            self.current_job_outlook += dYt # Add the change to the current employment
            self.employment.append(self.current_job_outlook) # Append new employment count to series
            self.T -= self.dt # Account for the step in time

    def __init__(self,
                 initial_job_outlook,
                 drift,
                 volatility,
                 dt,
                 T,
                 shape,
                 loc,
                 scale):
        self.current_job_outlook = initial_job_outlook
        self.initial_job_outlook = initial_job_outlook
        self.drift = drift
        self.volatility = volatility
        self.dt = dt
        self.T = T
        self.shape = shape
        self.loc = loc
        self.scale = scale
        self.employment = [] # Initializes an empty list ot store number employed
        self.simulate_paths() # Start the simulation upon initialization

class Burr_Motion:
    def simulate_paths(self):
        while (self.T - self.dt > 0):
            dWt = burr.rvs(self.c, self.d, loc=self.loc, scale=self.scale)
            dYt = self.drift * self.dt + self.volatility * dWt # Change in employment
            self.current_employment += dYt # Add the change to the current price
            self.employment.append(self.current_employment) # Append new employment to series
            self.T -= self.dt

    def __init__(self,
                 initial_employment,
                 drift,
                 volatility,
                 dt,
                 T,
                 c,
                 d,
                 loc,
                 scale):
        self.current_employment = initial_employment
        self.initial_employment = initial_employment
        self.drift = drift
        self.volatility = volatility
        self.dt = dt
        self.T = T
        self.c = c
        self.d = d
        self.loc = loc
        self.scale = scale
        self.employment = []
        self.simulate_paths()

if __name__ == "__main__":
    print("==== GRAPHING EMPLOYMENT IN DATA PROCESSING, HOSTING, AND RELATED SERVICES ====")
    graph_employment("EuropeanCallOption/data/Tech_Industry_Employment.csv")
    flat_csv = flatten_csv("EuropeanCallOption/data/Tech_Industry_Employment.csv")
    employment_best_fit = graph_best_fit(flat_csv)

    paths = 1000
    initial_job_outlook = flat_csv[-1]
    drift = calculate_drift(flat_csv)
    volatility = calculate_volatility(flat_csv)
    dt = 1/365
    T = 1
    c = employment_best_fit['burr']['c']
    d = employment_best_fit['burr']['d']
    loc = employment_best_fit['burr']['loc']
    scale = employment_best_fit['burr']['scale']
    employment_paths = []

    # Generate a set of sample paths
    for i in range(0, paths):
        employment_paths.append(Burr_Motion(initial_job_outlook,
                                            drift,
                                            volatility,
                                            dt,
                                            T,
                                            c,
                                            d,
                                            loc,
                                            scale).employment)
    
    call_payoffs = []
    final_employment = []
    ec = European_Call_Payoff(initial_job_outlook)
    risk_free_rate = .01
    for employment_path in employment_paths:
        call_payoffs.append(ec.get_payoff(employment_path[-1])/(1 + risk_free_rate))
        # We get teh last employment rate in the series generated to determine the payoff and discount it by one year
        final_employment.append(employment_path[-1])

    # Plot the set of generated sample paths
    for employment_path in employment_paths:
        plt.plot(employment_path)
    plt.xlabel('Days')
    plt.ylabel('All Employed, Thousands')
    plt.title('Simulation of Employment in Data Processing, Hosting, and Related Services Based on Gamma Distribution')
    plt.show()


    avg_final_employment = np.average(final_employment)
    print(f'Data Processing, Hosting, and Related Services Average Employment today: {initial_job_outlook * 1000} Employed')
    print(f'Data Processing, Hosting, and Related Services Average Employment after {int(1 / dt) * T} days: {avg_final_employment * 1000} Employed')
    print(f'Speculated job growth: {(avg_final_employment - initial_job_outlook) * 1000} new jobs')
