
# coding: utf-8

# In[8]:

import quandl
import matplotlib.pyplot as plt


# In[12]:

#1) Use Quandl API to get and plot (on the same graph) the Terms of Trade for Armenia and Luxembourg from the World Bank database.
Armenia_TOT=quandl.get('WORLDBANK/ARM_TOT',authtoken='S_VRmaJ57bu7B896mWgY')
Luxembourg_TOT=quandl.get('WORLDBANK/LUX_TOT', authtoken='S_VRmaJ57bu7B896mWgY')
Armenia_TOT['Value'].plot()
plt.show()
Luxembourg_TOT['Value'].plot()
plt.show()


# In[51]:

#2) Calculate the 2nd highest value for the above mentioned database, for Armenia.
Armenia_TOT_sorted=Armenia_TOT.sort('Value', ascending=False)
print(Armenia_TOT_sorted.ix[2:3])


# In[24]:

#3) Draw the Net exports graph for Armenia based on the Merchandise Exports and Import for Armenia from the World Trade Organization database on Quandl.
Armenia_MEXP=quandl.get('WTO/MERCH_EXP_ARM', authtoken='S_VRmaJ57bu7B896mWgY')
Armenia_MEXP['Value'].plot()
plt.show()


# In[41]:

#4)Draw the correlation matrix between arbitrary 3 stocks using the End of day stock prices database on Quandl.
share_prices=quandl.get(['SIX/CH0006089921CHF4', 'SIX/FR0000120164CHF4','SIX/LU0269583422CHF4'], authtoken='S_VRmaJ57bu7B896mWgY')
share_prices.drop(share_prices.columns[[1,3,5]], axis=1, inplace=True)
share_prices.corr()


# In[54]:

#5) Create a list of 10 cities. Use google maps API to calculate (inside a for or while loop)
#the distance of each of those cities from New York (in km-s).
import googlemaps
from datetime import datetime 
gmaps=googlemaps.Client('AIzaSyDMqvPw0qUSzIsu29CBNm18yqdRKnW9QUU')
city_list=[]
C1 = gmaps.directions("Panama, Panama","New York, USA")
C2 = gmaps.directions("California, USA","New York, USA")
C3 = gmaps.directions("Texas, USA","New York, USA")
C4 = gmaps.directions("Denver, USA","New York, USA")
C5 = gmaps.directions("Mexico City, Mexico","New York, USA")
C6 = gmaps.directions("Oklahoma, USA","New York, USA")
C7 = gmaps.directions("Dallas, USA","New York, USA")
C8 = gmaps.directions("Kansas City, USA","New York, USA")
C9 = gmaps.directions("Miamia, USA","New York, USA")
C10 = gmaps.directions("Managua, Nicaragua","New York, USA")
city_list.append([C1,C2,C3,C4,C5,C6,C7,C8,C9,C10])
distances=[]
for C in city_list:
    for item in C:
        dist = item[0]["legs"][0]["distance"]
        distances.append(dist)
distances


# In[154]:




# In[ ]:



