from numpy import nan
from pandas import read_csv


# Generate a csv for pandas to use from any given load profile
def generate_household_csv(file_in_name: str, file_out_name: str):
    dataset = read_csv('household_power_consumption.txt', sep=';', header=0, low_memory=False,
                       infer_datetime_format=True,
                       parse_dates={'datetime': [0, 1]}, index_col=['datetime'])

    dataset.replace('?', nan, inplace=True)

    values = dataset.values.astype('float32')
    dataset['sub_metering_4'] = (values[:, 0] * 1000 / 60 - (values[:, 4] + values[:, 5] + values[:, 6]))

    dataset.to_csv('household_power_consumption.csv')
