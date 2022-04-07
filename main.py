from matplotlib import pylab as plt
import pandas as pd

 #pd.plotting.register_matplotlib_converters()

df1 = pd.read_csv("ADS.DE.csv")
print(df1.head())
df1['Date'] = pd.to_datetime(df1.Date)
 print(df1.head())

df2 = pd.read_csv("NKE.csv")
print(df2)
df2['Date'] = pd.to_datetime(df2.date)
 indexes = []
 for date2 in df2.Date:
     for index, date1 in enumerate(df1.Date):
        if date2 == date1:
             indexes.append(index)
 print(indexes)


mean = df1["Close"].mean()

mean2 = df2["Close"].mean()

plt.figure("AAPL.csv")
plt.plot(df1["Date"], df1["Close"], 'r-', linewidth=0.6, label="APPL Stock price, mean="+str(mean))
 or the same can be:
 plt.plot("Date", "Close", 'r-', linewidth=0.6, label="APPL Stock price, mean="+str(mean), data=df1)

plt.xlabel("Dates")
plt.legend(loc="upper left")

plt.figure("AAPL.csv")
plt.plot(df2["Date"], df2["Close"], 'r-', linewidth=0.6, label="APPL Stock price, mean="+str(mean2))
 or the same can be:
 plt.plot("Date", "Close", 'r-', linewidth=0.6, label="APPL Stock price, mean="+str(mean), data=df1)

plt.xlabel("Dates")
plt.legend(loc="upper left")

plt.show()

print(plt.show())