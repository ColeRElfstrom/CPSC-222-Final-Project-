import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler

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

def hypothesis_test(series1, series2):
    from scipy import stats
    # use t-test dependent 
    t, pval = stats.ttest_rel(series1, series2)
    pval /= 2 # divide by two because 1 rejection region
    print("t:", t, "pval:", pval)
    alpha = 0.01
    if pval < alpha:
        print("reject H0")
    else:
        print("do not reject H0")


def prep_model(df, column):
    df = df.drop("Date", axis=1)
    df = df.drop("Day of Week", axis=1)
    X = df.drop(column, axis=1)
    y = df[column]
    return X, y

def knn_model(df, column):
    X, y = prep_model(df, column)
    X_train, X_test, y_train, y_test =\
        train_test_split(X, y, test_size=0.25,
        random_state=0)

    scaler = MinMaxScaler()
    scaler.fit(X_train)
    #X_train_normalized = scaler.transform(X_train)
    knn_clf = KNeighborsClassifier(n_neighbors=25)
    knn_clf.fit(X_train, y_train)
    y_predicted = knn_clf.predict(X_test)
    accuracy = knn_clf.score(X_test, y_test)
    accuracy = accuracy_score(y_test, y_predicted)
    print("accuracy:", accuracy)