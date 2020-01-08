# Module 4 Project - XLV Forecasting: Time Series Analysis

## Data Scientist: Andrew Cole

### Goals: 
Answer a small market wealth mgmt. company's inquiry for finding a financial vehicle for it's investor pool which has historically produced strong returns and will continue to do so well into the future. Time Series analysis & forecasting will be used to determine the future performance.
    - What is a financial vehicle which has produced historic increase in value to it's investors?
    - Will the fund (XLV Healthcare Mutual Fund) continue to increase in value?
    - Create a model which accurately tracks the historic movement of the fund as well as confidently forecasts the value increase into the future.

### Responsibilities:
- Create github repository for files and efficient tracking of the project progress
- Research various mutual funds for historic successes
- Import necessary libraries for gathering of historic financial data
- Clean and organize financial data for operation in TS analysis
- Identify components of TS data and perform necessary transformations/computations of the data for model testing
- Train multiple Time Series models for comparison, choose strongest performing model
- Fit financial test data to best performing model for final TS Analysis 
- Formulate recommendations for the business based off of results of the TS model
- Create appropriate visualizations for explaining the process and models
- Create helper modules for efficient running of the script
- Create README file for project overview
- Create slide deck for presentation of findings
- Present concepts to the "business"

### Summary of Included Files:
The following files are included under the Module_4_Project folder within the GitHub repository:
- Mod4_TS_Technical.ipynb
    - Jupyter notebook for techincal audience
    - PEP 8 Standards
    - Imports cleaning, stationarity check, auto_arima, and future_dates modules
    - Library importation, statistical testing, and forecasting with visualizations

- Mod4_Non_Techical.ipynb
    - Jupyter notebook for non-technical audience
    - Description of stakeholder needs and goals of the analysis
    - Visualizations with detailed non-technical explanations of what each step is accomplishing and what outcomes mean
    - Actionable insights for stakeholder

- Mod4_TS_Full.ipynb
    - Technical jupyter notebook which contains scratch work and non-formal coding
    
- ticker_cleaner.py
    - Packaged module for importation and cleaning of financial data for respective financial instruments
    - Imports, cleans, and arranges financial information into operable Pandas DataFrame
    - Resamples daily inputs into monthly averages
    - Returns Time Series dataframe for analysis and modeling

- stationarity_check.py
    - Contains function to check stationarity of the given time series
    - Takes rolling mean & rolling standard deviation
    - Performs Dickey-Fuller stationarity check
    - Plots rolling mean, rolling standard deviation, and original series
    - Outputs visualization as well as results of Dickey-Fuller test 
    
- Auto_ARIMA.py
    - Creates all possible combinations of SARIMA parameter inputs
    - Performs SARIMAX model on every combination and returns combination with lowest output AIC value

- future_dates.py
    - Adds future Datetime entries to Time Series dataframe which will be populated by predicted values for corresponding index points



