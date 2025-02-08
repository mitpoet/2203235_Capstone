import requests
import csv
import pandas as pd
import os
import shutil
import pathlib

API = 'YMH1T8UGO6WSLYFZ'

def fetch_stock_data(symbol, api_key, output_file, start_date, end_date):
    """...existing docstring..."""
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
    temp_file = "temp_" + output_file
    
    with open(temp_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Open", "High", "Low", "Close", "Volume"])
        
        for date, values in sorted(time_series.items(), reverse=True):
            if start_date <= date <= end_date:
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
    
    # Delete the temporary file
    os.remove(temp_file)
    
    # Create datasets directory if it doesn't exist
    datasets_dir = "./Datasets"
    pathlib.Path(datasets_dir).mkdir(parents=True, exist_ok=True)
    
    # Move the file to datasets directory
    final_path = os.path.join(datasets_dir, os.path.basename(output_file)).replace('\\', '/')
    shutil.move(output_file, final_path)
    
    print(f"Data fetched, filtered, saved, and moved to {final_path}")

# Example usage with custom date range
fetch_stock_data(
    symbol="ORCL",
    api_key=API,
    output_file="ORCL.csv",
    start_date="2014-01-01",
    end_date="2024-01-31"
)

# def fetch_save_reverse_stock_data(symbol, api_key, output_file, start_date, end_date):
#     """
#     Fetches daily stock data for the given symbol from Alpha Vantage between specified dates,
#     saves it to a CSV file, and then reverses the date order in the saved file.

#     Parameters:
#     symbol (str): The stock symbol to fetch data for.
#     api_key (str): Your Alpha Vantage API key.
#     output_file (str): The name of the CSV file to save the processed data.
#     start_date (str): Start date in 'YYYY-MM-DD' format.
#     end_date (str): End date in 'YYYY-MM-DD' format.
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
#     temp_file = "temp_" + output_file
    
#     with open(temp_file, mode="w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Date", "Open", "High", "Low", "Close", "Volume"])
        
#         for date, values in sorted(time_series.items(), reverse=True):
#             if start_date <= date <= end_date:  # Using the custom date range
#                 writer.writerow([
#                     date,
#                     values["1. open"],
#                     values["2. high"],
#                     values["3. low"],
#                     values["4. close"],
#                     values["5. volume"]
#                 ])
    
#     df = pd.read_csv(temp_file)
#     df.iloc[::-1].to_csv(output_file, index=False)

#     # Delete the temporary file
#     os.remove(temp_file)
    
#     print(f"Data fetched, filtered, saved, and reversed in {output_file}")

# # Example usage with custom date range
# fetch_save_reverse_stock_data(
#     symbol="ORCL",
#     api_key=API,
#     output_file="ORCL.csv",
#     start_date="2014-01-01",
#     end_date="2024-01-31"
# )






