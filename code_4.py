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

    
    # while True:
    #     year = int(input("Enter a year (2000 - 2022): "))

    #     if 2000 <= year <= 2022:
    #         break
    #     else:
    #         print("Invalid input. Please enter a valid year.")

            
    valid_country_codes = [
    'arg', 'aus', 'bra', 'can', 'che', 'chl', 'chn', 'cze', 'dnk', 'euz',
    'gbr', 'hkg', 'hun', 'idn', 'isr', 'jpn', 'kor', 'mex', 'mys', 'nzl',
    'pol', 'rus', 'sgp', 'swe', 'tha', 'twn', 'usa', 'zaf', 'phl', 'nor',
    'per', 'tur', 'ven', 'egy', 'col', 'cri', 'lka', 'pak', 'sau', 'ukr',
    'ury', 'are', 'ind', 'vnm', 'aze', 'bhr', 'gtm', 'hnd', 'hrv', 'jor',
    'kwt', 'lbn', 'mda', 'nic', 'omn', 'qat', 'rou'
]

    # while True:
    #     country_code = input("Enter a country code: ")
    #     if country_code in valid_country_codes:
    #         break
    #     else:
    #         print("Invalid input. Please enter a valid country code.")
        
   

    # result_a = get_big_mac_price_by_year(year, country_code)
    while True:
        year = int(input("Enter a year (2000 - 2022): "))

        if 2000 <= year <= 2022:
            break
        else:
            print("Invalid input. Please enter a valid year.")

    while True:
        country_code = input("Enter a country code: ")
        if country_code in valid_country_codes:
            break
        else:
            print("Invalid input. Please enter a valid country code.")
    result_a = get_big_mac_price_by_year(year, country_code)
    print(result_a)
    # result_b = get_big_mac_price_by_country(country_code)
    while True:
        country_code = input("Enter a country code: ")
        if country_code in valid_country_codes:
            break
        else:
            print("Invalid input. Please enter a valid country code.")
    result_b = get_big_mac_price_by_country(country_code)
    print(result_b)
    # result_c = get_the_cheapest_big_mac_price_by_year(year)
    while True:
        year = int(input("Enter a year (2000 - 2022): "))

        if 2000 <= year <= 2022:
            break
        else:
            print("Invalid input. Please enter a valid year.")
    result_c = get_the_cheapest_big_mac_price_by_year(year)
    print(result_c)
    # result_d = get_the_most_expensive_big_mac_price_by_year(year)
    while True:
        year = int(input("Enter a year (2000 - 2022): "))

        if 2000 <= year <= 2022:
            break
        else:
            print("Invalid input. Please enter a valid year.")
    result_d = get_the_most_expensive_big_mac_price_by_year(year)
    print(result_d)
    

    # print(get_big_mac_price_by_year(year, country_code))
    # print(get_big_mac_price_by_country(country_code))
    # print(get_the_cheapest_big_mac_price_by_year(year))
    # print(get_the_most_expensive_big_mac_price_by_year(year))



