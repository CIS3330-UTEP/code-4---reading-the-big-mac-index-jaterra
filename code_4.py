import csv
import pandas as pd

big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year, country_code):
    filtered_data = df[(df['date'].str.startswith(f"{year}-")) & (df['iso_a3'] == country_code)]['dollar_price']
    mean_price = filtered_data.mean() if not filtered_data.empty else 0
    return round(mean_price, 2)

def get_big_mac_price_by_country(country_code):
    filtered_data = df[df['iso_a3'] == country_code]['dollar_price']
    mean_price = filtered_data.mean() if not filtered_data.empty else 0
    return round(mean_price, 2)

def get_the_cheapest_big_mac_price_by_year(year):
    filtered_data = df[df['date'].str.startswith(f"{year}-")].nsmallest(1, 'dollar_price')
    
    if filtered_data.empty:
        return f"No data available for {year}"
    
    country_name = filtered_data['name'].iloc[0]
    country_code = filtered_data['iso_a3'].iloc[0]
    price = round(filtered_data['dollar_price'].iloc[0], 2)

    return f"In {year}, the cheapest Big Mac price is {country_name}({country_code.upper()}): ${price}"

def get_the_most_expensive_big_mac_price_by_year(year):
    filtered_data = df[df['date'].str.startswith(f"{year}-")].nlargest(1, 'dollar_price')
    
    if filtered_data.empty:
        return f"No data available for {year}"
    
    country_name = filtered_data['name'].iloc[0]
    country_code = filtered_data['iso_a3'].iloc[0]
    price = round(filtered_data['dollar_price'].iloc[0], 2)

    return f"In {year}, the most expensive Big Mac price is {country_name}({country_code.upper()}): ${price}"

if __name__ == "__main__":
    year = 2014
    country_code = 'mex'

    print(f"Mean Big Mac price in {year} in {country_code.upper()} is: ${get_big_mac_price_by_year(year, country_code)}")
    print(f"Mean Big Mac price in {country_code.upper()} is: ${get_big_mac_price_by_country(country_code)}")
    print(get_the_cheapest_big_mac_price_by_year(year))
    print(get_the_most_expensive_big_mac_price_by_year(year))





    