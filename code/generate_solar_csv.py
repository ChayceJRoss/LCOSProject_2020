from pandas import read_csv
from numpy import nan


# Generate a csv from solar irradiance data for pandas to use
def generate_csv(file_in_name: str, file_out_name: str):
    dataset = read_csv(file_in_name, sep=';', header=0, low_memory=False, infer_datetime_format=True,
                       parse_dates={'datetime': [0, 1]}, index_col=['datetime'])

    dataset.replace(-999, nan, inplace=True)

    solar_input_data = dataset[['Global Horiz', 'Temperature']]
    solar_input_data.to_csv(file_out_name)


generate_csv('SoDa_HC3-METEO_lat-20.559_lon29.541_2004-02-01_2006-12-31_1112090259.csv', 'solar_data_2004_2006.csv')
