""" yf_example3.py

The purpose of this module is to download stock price data for Qantas for a given year and save the information in a CSV file.
"""
import yfinance as yf
import os
import toolkit_config as cfg

def qan_prc_to_csv(year):
    """ Download Qantas stock prices for a given year into a CSV file.

       Parameters
       ----------
       year : int
           The year for which the stock prices are downloaded.

       tic : str
            Ticker

       pth : str
            Location of the output CSV file

       start: str, optional
           Download start date string (YYYY-MM-DD)
            If None (the default), start is set to '1900-01-01'

       end: str, optional
            Download end date string (YYYY-MM-DD)
            If None (the default), end is set to the most current date available

    The name of this file will be qan_prc_YYYY.csv, where the YYYY stands for the year in year.
    """

    tic = 'QAN.AX'
    pth = os.path.join(cfg.DATADIR, f'qan_prc_{year}.csv')
    start = f"{year}-01-01"
    end = f"{year}-12-31"
    df = yf.download(tic, start=start, end=end)
    df.to_csv(pth)

if __name__ == "__main__":
    qan_prc_to_csv(2020)