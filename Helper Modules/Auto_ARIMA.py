import itertools

def auto_arima():
    '''
    Function: Calculates every possible combination of autoregressive and moving average parameters for the ARIMA model, and returns those with the lowest resulting AIC value.
    
    Input: None
    
    Output: The AR/MA parameter combination with the lowest resulting AIC value
    
    '''
    p = d = q = range(0,3)
    pdq = list(itertools.product(p,d,q))
    pdqs = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p,d,q))]
    
    
    warnings.filterwarnings(action='once')
    ans = []
    for comb in pdq:
        for combs in pdqs:
            try:
                mod = sm.tsa.statespace.SARIMAX(xlv_monthly_mean.Close, 
                                                order = comb, 
                                                seasonal_order = combs, 
                                                enforce_stationarity = False, 
                                                enforce_invertability = False)
                output = mod.fit()
                ans.append([comb, combs, output.aic])
                
            except:
                continue
                
    
    ans_df = pd.DataFrame(ans, columns = ['pdq', 'pdqs', 'aic'])
    return ans_df.loc[ans_df['aic'].idxmin()]

