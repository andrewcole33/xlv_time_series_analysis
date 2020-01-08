import yfinance as yf
import pandas as pd

def yahoo_finance_clean(ticker):
    '''
    Function to gather financial data from Yahoo Finance using yfinance Python library. Converts imported data into operable Pandas DataFrame.
    
    Input: Asset's ticker symbol (type = 'String')
    
    Output: DataFrame with historic financial information for the given asset ticker.
    '''
    
    ticker = yf.Ticker(ticker)
    ticker_hist = ticker.history(period = 'max', actions = False)
    ticker_hist_monthly = ticker_hist['Close'].resample('MS')
    ticker_monthly_mean = pd.DataFrame(ticker_hist_monthly.mean())
    
    return ticker_monthly_mean.reindex(index = ticker_monthly_mean.index[::-1])
    
