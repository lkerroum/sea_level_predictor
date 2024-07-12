import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Scatter', s=15)

    # Create first line of best fit
    lr = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = pd.concat([df['Year'],pd.DataFrame(range(2014,2051))], ignore_index=True)
    y = lr.intercept + x*lr.slope
    plt.plot(x,y, label='Best fit 1', color='orange')

    


    # Create second line of best fit
    df2 =df[df['Year'] >= 2000]
    lr2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    x2 = pd.concat([df['Year'],pd.DataFrame(range(2014,2051))], ignore_index=True)
    y2 = lr2.intercept + x2*lr2.slope
    plt.plot(x2,y2, label='Best fit 2', color='red')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend() 
    plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

