import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import column

def clean_data(series):
    for val in series:
        val = int(val)
    return series

def split_apply_combine(df, user_column):
    grouped_by_day = df.groupby("Day of Week")
    mean_steps = pd.Series(dtype=float)
    for day, day_df in grouped_by_day :
        day_mean_col = day_df[user_column].mean()
        mean_steps[day] = day_mean_col
        mean_steps.name = "Mean per Day"
        mean_steps.to_csv("Mean_per_Day.csv", na_rep="NA")
    return grouped_by_day, mean_steps


def group_days(series):
    days = ["Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"]
    by_day = []
    by_day.append(series["Monday"])
    by_day.append(series["Tuesday"])
    by_day.append(series["Wednesday"])
    by_day.append(series["Thursday"])
    by_day.append(series["Friday"])
    by_day.append(series["Saturday"])
    by_day.append(series["Sunday"])
    return by_day

def plot_by_day(date, series, title):
    plt.plot()
    plt.bar(date, series)
    plt.xlabel("Date")
    plt.ylabel(title)
    x_labels = ["01-25", "02-03", "02-17", "03-03", "03-17", "03-31", "04-14"]
    x_ticks = [9, 22, 35, 48, 62, 75, 88]
    plt.xticks(ticks=x_ticks,labels=x_labels, rotation=0)
    plt.title(title + " per Day")
    plt.show()

def plot_by_day_of_week(series, title):
    days = ["Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"]
    plt.plot()
    plt.bar(days, series)
    plt.xlabel("Day of Week")
    plt.ylabel(title)
    plt.title(title + " by Day of Week Beggining 2022")
    plt.show()

def categorize_high_low(series):
    mean = sum(series) / len(series)
    return_list = []
    for i in range(len(series)):
        if(series[i] > mean):
            return_list.append(1)
        else:
            return_list.append(0)
    return return_list




