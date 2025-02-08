import requests
import csv
import pandas as pd

API = 'YMH1T8UGO6WSLYFZ'

def fetch_save_reverse_stock_data(symbol, api_key, output_file):
    """
    Fetches daily stock data for the given symbol from Alpha Vantage from 2012-05-18 to 2022-12-30, saves it to a CSV file,
    and then reverses the date order in the saved file.

    Parameters:
    symbol (str): The stock symbol to fetch data for.
    api_key (str): Your Alpha Vantage API key.
    output_file (str): The name of the CSV file to save the processed data.
    """
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": "full",
        "apikey": api_key
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if "Time Series (Daily)" not in data:
        print("Error fetching data:", data.get("Note", data.get("Error Message", "Unknown error")))
        return
    
    time_series = data["Time Series (Daily)"]
    temp_file = "temp_" + output_file  # Temporary file for initial save
    
    with open(temp_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Open", "High", "Low", "Close", "Volume"])
        
        for date, values in sorted(time_series.items(), reverse=True):
            if "2012-05-18" <= date <= "2022-12-30":
                writer.writerow([
                    date,
                    values["1. open"],
                    values["2. high"],
                    values["3. low"],
                    values["4. close"],
                    values["5. volume"]
                ])
    
    df = pd.read_csv(temp_file)
    df.iloc[::-1].to_csv(output_file, index=False)
    
    print(f"Data fetched, filtered, saved, and reversed in {output_file}")

# Example usage
fetch_save_reverse_stock_data("AAPL", API, "AAPL.csv")

# def fetch_save_reverse_stock_data(symbol, api_key, output_file):
#     """
#     Fetches daily stock data for the given symbol from Alpha Vantage, saves it to a CSV file,
#     and then reverses the date order in the saved file.

#     Parameters:
#     symbol (str): The stock symbol to fetch data for.
#     api_key (str): Your Alpha Vantage API key.
#     output_file (str): The name of the CSV file to save the processed data.
#     """
#     url = "https://www.alphavantage.co/query"
#     params = {
#         "function": "TIME_SERIES_DAILY",
#         "symbol": symbol,
#         "outputsize": "full",
#         "apikey": api_key
#     }
    
#     response = requests.get(url, params=params)
#     data = response.json()
    
#     if "Time Series (Daily)" not in data:
#         print("Error fetching data:", data.get("Note", data.get("Error Message", "Unknown error")))
#         return
    
#     time_series = data["Time Series (Daily)"]
#     temp_file = "temp_" + output_file  # Temporary file for initial save
    
#     with open(temp_file, mode="w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Date", "Open", "High", "Low", "Close", "Volume"])
        
#         for date, values in sorted(time_series.items(), reverse=True):
#             writer.writerow([
#                 date,
#                 values["1. open"],
#                 values["2. high"],
#                 values["3. low"],
#                 values["4. close"],
#                 values["5. volume"]
#             ])
    
#     df = pd.read_csv(temp_file)
#     df.iloc[::-1].to_csv(output_file, index=False)
    
#     print(f"Data fetched, saved, and reversed in {output_file}")

# # Example usage
# # fetch_save_reverse_stock_data("AAPL", API, "AAPL.csv")
# fetch_save_reverse_stock_data("AAPL", API, "AAPL.csv")

# def fetch_and_save_stock_data(symbol, api_key, output_file):
#     """
#     Fetches daily stock data for the given symbol from Alpha Vantage and saves it to a CSV file.

#     Parameters:
#     symbol (str): The stock symbol to fetch data for.
#     api_key (str): Your Alpha Vantage API key.
#     output_file (str): The name of the CSV file to save the data to.
#     """
#     # API details
#     url = "https://www.alphavantage.co/query"
#     params = {
#         "function": "TIME_SERIES_DAILY",
#         "symbol": symbol,
#         "outputsize": "full",
#         "apikey": api_key
#     }

#     # Fetch data from Alpha Vantage
#     response = requests.get(url, params=params)

#     # Parse JSON data
#     data = response.json()

#     # Check for errors in the response
#     if "Time Series (Daily)" not in data:
#         print("Error fetching data:", data.get("Note", data.get("Error Message", "Unknown error")))
#     else:
#         # Extract time series data
#         time_series = data["Time Series (Daily)"]

#         # Save to CSV
#         with open(output_file, mode="w", newline="") as file:
#             writer = csv.writer(file)

#             # Write the header
#             writer.writerow(["Date", "Open", "High", "Low", "Close", "Volume"])

#             # Write the data
#             for date, values in sorted(time_series.items(), reverse=True):
#                 writer.writerow([
#                     date,
#                     values["1. open"],
#                     values["2. high"],
#                     values["3. low"],
#                     values["4. close"],
#                     values["5. volume"]
#                 ])

#         print(f"Data saved to {output_file}")

# # Example usage
# # fetch_and_save_stock_data("META", "YMH1T8UGO6WSLYFZ", "Meta_uncleaned.csv")
# fetch_and_save_stock_data("AAPL", "YMH1T8UGO6WSLYFZ", "AAPL_uncleaned.csv")

# def reverse_csv_date_order(input_file, output_file):
#     """
#     Reverses the order of the rows in a CSV file based on the date.

#     Parameters:
#     input_file (str): The name of the input CSV file.
#     output_file (str): The name of the output CSV file to save the reversed data.
#     """
#     # Read the CSV file into a DataFrame
#     df = pd.read_csv(input_file)

#     # Reverse the order of the rows
#     df_reversed = df.iloc[::-1]

#     # Save the reversed DataFrame to a new CSV file
#     df_reversed.to_csv(output_file, index=False)

#     print(f"Data reversed and saved to {output_file}")

# # Example usage
# # reverse_csv_date_order('MDB_uncleaned.csv', 'MDB.csv')
# reverse_csv_date_order('AAPL_uncleaned.csv', 'AAPL.csv')


import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date, output_file):
    """
    Fetch stock data from Yahoo Finance and save to a CSV file.

    Parameters:
    ticker : str
        Stock ticker symbol (e.g., 'AAPL' for Apple).
    start_date : str
        Start date in the format 'YYYY-MM-DD'.
    end_date : str
        End date in the format 'YYYY-MM-DD'.
    output_file : str
        Path to the CSV file where the data will be saved.
    """
    # Download stock data
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    
    # Select desired columns
    stock_data = stock_data[['Open', 'High', 'Low', 'Close', 'Volume']]
    
    # Save to CSV
    stock_data.to_csv(output_file)
    print(f"Stock data for {ticker} saved to {output_file}")

# Example usage
# fetch_stock_data('000001.SS', '2013-01-01', '2023-12-31', 'SSE_stock_data.csv')

import pandas as pd

def reformat_csv(input_file, output_file):
    """
    Reformats the CSV file to match the desired structure.

    Parameters:
    input_file : str
        Path to the input CSV file.
    output_file : str
        Path to save the reformatted CSV file.
    """
    # Read the CSV file
    df = pd.read_csv(input_file, skiprows=3)  # Skip the header rows
    df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']  # Rename columns
    
    # Save the reformatted data to a new CSV file
    df.to_csv(output_file, index=False)
    print(f"Reformatted CSV saved to {output_file}")

# Example usage
# reformat_csv('SSE_stock_data.csv', 'SSE.csv')