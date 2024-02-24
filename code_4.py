import csv
import pandas as pd

big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year, country_code):
   
    query = f"(iso_a3 == '{country_code.upper()}')"
    country_df = df.query(query)
    country_df = country_df[country_df['date'].apply(lambda row: row[:4] == str(year))]

    average_price = round(country_df['dollar_price'].mean(), 2)

    return average_price

def get_big_mac_price_by_country(country_code):

    query = f"(iso_a3 == '{country_code.upper()}')"
    country_df = df.query(query)

    average_price = round(country_df['dollar_price'].mean(), 2)

    return average_price

def get_the_cheapest_big_mac_price_by_year(year):
    

    query = df['date'].apply(lambda row: row[:4] == str(year))
    year_df = df[query]

    min_idx = year_df['dollar_price'].idxmin()
    country_name = year_df.loc[min_idx]['name']
    country_code = year_df.loc[min_idx]['iso_a3']
    dollar_price = round(year_df.loc[min_idx]['dollar_price'], 2)

    output = f"{country_name} ({country_code}): ${dollar_price}"

    return output

def get_the_most_expensive_big_mac_price_by_year(year):
    
    query = df['date'].apply(lambda row: row[:4] == str(year))
    year_df = df[query]

    max_idx = year_df['dollar_price'].idxmax()
    country_name = year_df.loc[max_idx]['name']
    country_code = year_df.loc[max_idx]['iso_a3']
    dollar_price = round(year_df.loc[max_idx]['dollar_price'],2)

    output = f"{country_name}({country_code}): ${dollar_price}"
    
    return output

if __name__ == "__main__":
   

    result_a = get_big_mac_price_by_year(2010, "arg")
    print(result_a)
    result_b = get_big_mac_price_by_country("mex")
    print(result_b)
    result_c = get_the_cheapest_big_mac_price_by_year(2008)
    print(result_c)
    result_d = get_the_most_expensive_big_mac_price_by_year(2014)
    print(result_d)



