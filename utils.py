import pandas as pd
import matplotlib.pyplot as plt

health_df = pd.read_csv("health_data.csv")
steps = health_df["Step Count"]
date = health_df["Date"]

for val in steps:
    val = int(val)

plt.bar(date, steps)
plt.xlabel("Date")
plt.ylabel("Steps")
x_labels = ["01-25", "02-03", "02-17", "03-03", "03-17", "03-31", "04-14"]
x_ticks = [9, 22, 35, 48, 62, 75, 88]
plt.xticks(ticks=x_ticks,labels=x_labels, rotation=0)
plt.title("Steps per Day 2022")
plt.show()




