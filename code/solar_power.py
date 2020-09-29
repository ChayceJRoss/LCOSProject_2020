from pandas import read_csv
from panels import SolarPanel, SolarProfile


# Generates a csv with all the power, open volt, and short circuit info for the solar panel input
def generate_power_output(file_in_name: str, file_out_name: str, year: str, solar_panel: SolarPanel):
    solar_data_2004_2006 = read_csv(file_in_name, header=0, low_memory=False, infer_datetime_format=True,
                                    parse_dates=['datetime'], index_col=['datetime'])

    solar_data_2005 = solar_data_2004_2006.loc[year]

    solar_data_2005 = solar_data_2005.sort_index()
    power = []
    voltage = []
    current = []

    profile = SolarProfile(solar_panel)

    for index, row in solar_data_2005.iterrows():
        power.append(profile.get_power(row['Temperature'] - 273.15, row['Global Horiz']))
        voltage.append(profile.get_voltage(row['Temperature'] - 273.15, row['Global Horiz']))
        current.append(profile.get_current(row['Temperature'] - 273.15, row['Global Horiz']))

    solar_data_2005['Power'] = power
    solar_data_2005['Voltage'] = voltage
    solar_data_2005['Current'] = current

    solar_data_2005.to_csv(file_out_name)


panel_one = SolarPanel("CS3U", pmax=355, vmp=39.4, imp=9.02, voc=46.8, isc=9.59, efficiency=0.1789, op_temp=40,
                       p_coeff=-0.37, v_coeff=-0.0029, i_coeff=0.0005, notc=42, n_s=1, n_p=1)

generate_power_output('datasets/solar_data_2004_2006.csv', 'datasets/solar_power_2005.csv', '2005', panel_one)




