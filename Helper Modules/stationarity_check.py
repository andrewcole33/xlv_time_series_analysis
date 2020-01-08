import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
import pandas as pd

def stationarity_check(Series):
    '''
    Function: To take in a series that has trend, take a rolling mean/std to try and remove trend, and then perform a Dickey Fuller test for stationarity. Function will also visualize the rolling mean, std, and original movements.
    
    Input: Time Series 
    
    Output: DataFrame with results of DF test. Also a visualization of rolling mean, std, and original movements.
    '''
    
    rolmean = Series.rolling(window = 12, center = False).mean()
    rolstd = Series.rolling(window = 12, center = False).std()
    
    dftest = adfuller(Series)
    
    fig = plt.figure(figsize = (16,9))
    orig = plt.plot(Series, color = 'b', label = 'original')
    mean = plt.plot(rolmean, color = 'r', label = 'Rolling Mean')
    std = plt.plot(rolstd, color = 'black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block = False)
    
    print('Results of Dickey-Fuller Test')
    
    dfoutput = pd.Series(dftest[0:4], index = ['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
        dfoutput['Critical Value (%s)' %key] = value
    print(dfoutput)
    
    return None
