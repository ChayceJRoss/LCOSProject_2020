from pandas import read_csv
from matplotlib import pyplot


# Generates a pyplot from a csv entry showing data for a whole year
def plot_over_years(file_in_name: str, years: [str], y_axis: str):

    dataset = read_csv(file_in_name, header=0, low_memory=False, infer_datetime_format=True,
                       parse_dates=['datetime'], index_col=['datetime'])

    pyplot.figure()
    for i in range(len(years)):
        # prepare subplot
        ax = pyplot.subplot(len(years), 1, i+1)
        # determine the year to plot
        year = years[i]
        # get all observations for the year
        result = dataset[str(year)]
        # plot the active power for the year
        pyplot.plot(result[y_axis])
        # add a title to the subplot
        pyplot.title(str(year), y=0, loc='left')
    pyplot.show()


# Generates a pyplot from a csv entry showing data for a set of months
def plot_over_months(file_in_name: str, year: str, months: [int], y_axis: str):
    dataset = read_csv(file_in_name, header=0, infer_datetime_format=True, parse_dates=['datetime'],
                       index_col=['datetime'])
    # plot active power for each year
    pyplot.figure()
    for i in range(len(months)):
        # prepare subplot
        ax = pyplot.subplot(len(months), 1, i+1)
        # determine the month to plot
        month = '{0}-{1}'.format(str(year), str(months[i]))
        # get all observations for the month
        result = dataset[month]
        # plot the active power for the month
        pyplot.plot(result[y_axis])
        # add a title to the subplot
        pyplot.title(month, y=0, loc='left')
    pyplot.show()


# Generates a pyplot from a csv entry showing data for a set of days, broken
def plot_over_days(file_in_name: str, year: str, month: str, days: [int], y_axis: str):
    dataset = read_csv(file_in_name, header=0, infer_datetime_format=True,
                       parse_dates=['datetime'], index_col=['datetime'])
    # plot active power for each year
    pyplot.figure()
    for i in range(len(days)):
        # prepare subplot
        ax = pyplot.subplot(len(days), 1, i + 1)
        # determine the day to plot
        day = '{0}-{1}-{2}'.format(str(year), str(month), str(days[i]))
        # get all observations for the day
        result = dataset[day]
        # plot the active power for the day
        pyplot.plot(result[y_axis])
        # add a title to the subplot
        pyplot.title(day, y=0, loc='left')
    pyplot.show()


plot_over_years('datasets/solar_power_2005.csv', ['2005'], 'Power')
# plot_over_months('solar_power_2005.csv', '2005', [x for x in range(1, 13)], 'Power')
# plot_over_days('solar_power_2005.csv', '2005', '02', [x for x in range(1, 20)], 'Power')
