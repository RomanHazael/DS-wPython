#Subplots December132023

import pandas as pd 
import matplotlib.pyplot as plt


df = pd.read_csv('./avocado.csv')


atlanta = df[df["region"] == "Atlanta"]

price = atlanta["AveragePrice"]
aveprice = price.rolling(30,min_periods=1).mean()
volume = atlanta["Total Volume"]

avocadobags = atlanta["Total Bags"]
sbags = atlanta["Small Bags"]
lbags = atlanta["Large Bags"]
xlbags = atlanta["XLarge Bags"]

plt.subplot(221)
plt.title("Avocado Price")
plt.plot(price, label = 'Price', color = 'green')
plt.plot(aveprice, label = 'Average Price', color = 'purple')

plt.subplot(222)
plt.title("Avocado Volume")
plt.plot(volume, label = 'Volume', color = 'red')


plt.subplot(223)
plt.title("Total Avocado Bags ")
plt.plot(avocadobags, label = 'Total Bags', color = 'blue')


plt.subplot(224)
plt.title('Bags')
plt.plot(sbags, label = 'Small Bags', color = 'black')
plt.plot(lbags, label = 'Large Bags', color = 'orange')
plt.plot(xlbags, label = 'XLarge Bags', color = 'yellow')
plt.legend()
 
plt.tight_layout()
plt.show()