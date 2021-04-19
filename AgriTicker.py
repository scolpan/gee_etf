import os
import pandas as pd
import alpaca_trade_api as tradeapi
from dotenv import load_dotenv

def get_etf_data():

    load_dotenv()

    alpaca_api_key = os.getenv("ALPACA_API_KEY")
    alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

    #print(alpaca_secret_key)

    alpaca = tradeapi.REST(
        alpaca_api_key,
        alpaca_secret_key,
        base_url = "https://paper-api.alpaca.markets",
        api_version="v2"
    )

    start_date_1 = pd.Timestamp("2010-01-01", tz="America/New_York").isoformat()
    end_date_1 = pd.Timestamp("2012-12-31", tz="America/New_York").isoformat()

    start_date_2 = pd.Timestamp("2013-01-01", tz="America/New_York").isoformat()
    end_date_2 = pd.Timestamp("2015-12-31", tz="America/New_York").isoformat()

    start_date_3 = pd.Timestamp("2016-01-01", tz="America/New_York").isoformat()
    end_date_3 = pd.Timestamp("2018-12-31", tz="America/New_York").isoformat()

    start_date_4 = pd.Timestamp("2019-01-01", tz="America/New_York").isoformat()
    end_date_4 = pd.Timestamp("2020-12-31", tz="America/New_York").isoformat()

    # Set the tickers
    tickers = ["CORN", "SOYB", "WEAT"]

    # Set timeframe to '1D' for Alpaca API
    timeframe = "1D"

    # Get 10 years worth of historical data for WEAT, CORN and SOYB

    # Max limit of 1000 so we get two sets of date range data and concatenate.
    df_etf_data1 = alpaca.get_barset(
        tickers,
        timeframe,
        start = start_date_1,
        end = end_date_1,
        limit=1000
    ).df

    df_etf_data2 = alpaca.get_barset(
        tickers,
        timeframe,
        start = start_date_2,
        end = end_date_2,
        limit=1000
    ).df

    df_etf_data3 = alpaca.get_barset(
        tickers,
        timeframe,
        start = start_date_3,
        end = end_date_3,
        limit=1000
    ).df

    df_etf_data4 = alpaca.get_barset(
        tickers,
        timeframe,
        start = start_date_4,
        end = end_date_4,
        limit=1000
    ).df


    #Concatenate
    df_etf_data = df_etf_data1.append(df_etf_data2).append(df_etf_data3).append(df_etf_data4)

    #Drop nulls
    df_etf_data.dropna(inplace=True)


    # Convert to date value (gets rid of closing time date e.g. 16:00) but this operation tends to convert the date type to object type
    df_etf_data.index = df_etf_data.index.date

    # Convert the Date column back to datetime type
    df_etf_data.index = pd.to_datetime(df_etf_data.index, infer_datetime_format=True)

    # Sort by index (Date)
    df_etf_data = df_etf_data.sort_index()


    # Create DataFrame
    df_etf_closing_prices = pd.DataFrame()

    # Rename the headers to the corresponding ticker
    df_etf_closing_prices["CORN_ETF"] = df_etf_data['CORN']['close']
    df_etf_closing_prices["WEAT_ETF"] = df_etf_data['WEAT']['close']
    df_etf_closing_prices["SOYB_ETF"] = df_etf_data['SOYB']['close']


    return df_etf_closing_prices



