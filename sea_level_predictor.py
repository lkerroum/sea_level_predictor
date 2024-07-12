import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Scatter')

    # Create first line of best fit
    lr = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = df['Year']
    y = lr.intercept + x*lr.slope
    plt.plot(x,y, label='Best fit 1', color=orange)
    plt.legend() 
    plt.show()


    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()