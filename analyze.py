import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle as pk
from sklearn.cluster import KMeans, MiniBatchKMeans
import math
import re
from collections import Counter
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

statename_to_abbr = {
    # Other
    'District of Columbia': 'DC',
    # States
    'Alabama': 'AL',
    'Montana': 'MT',
    'Alaska': 'AK',
    'Nebraska': 'NE',
    'Arizona': 'AZ',
    'Nevada': 'NV',
    'Arkansas': 'AR',
    'New Hampshire': 'NH',
    'California': 'CA',
    'New Jersey': 'NJ',
    'Colorado': 'CO',
    'New Mexico': 'NM',
    'Connecticut': 'CT',
    'New York': 'NY',
    'Delaware': 'DE',
    'North Carolina': 'NC',
    'Florida': 'FL',
    'North Dakota': 'ND',
    'Georgia': 'GA',
    'Ohio': 'OH',
    'Hawaii': 'HI',
    'Oklahoma': 'OK',
    'Idaho': 'ID',
    'Oregon': 'OR',
    'Illinois': 'IL',
    'Pennsylvania': 'PA',
    'Indiana': 'IN',
    'Rhode Island': 'RI',
    'Iowa': 'IA',
    'South Carolina': 'SC',
    'Kansas': 'KS',
    'South Dakota': 'SD',
    'Kentucky': 'KY',
    'Tennessee': 'TN',
    'Louisiana': 'LA',
    'Texas': 'TX',
    'Maine': 'ME',
    'Utah': 'UT',
    'Maryland': 'MD',
    'Vermont': 'VT',
    'Massachusetts': 'MA',
    'Virginia': 'VA',
    'Michigan': 'MI',
    'Washington': 'WA',
    'Minnesota': 'MN',
    'West Virginia': 'WV',
    'Mississippi': 'MS',
    'Wisconsin': 'WI',
    'Missouri': 'MO',
    'Wyoming': 'WY',
}
   
adTextFile = open('adText.txt','r')
adList = adTextFile.readlines()

def preprocess():
   #data =  pd.read_csv('AdMatrix.csv', sep=',')
   #data = np.array(data)
   #txtFile = open('adText.txt','r')
   #pk.dump(data,open('ads.pkl','wb'))

   mainTable =  pd.read_csv('mainMat.csv', sep=',')
   mainTable = np.array(mainTable,dtype=object)
   pk.dump(mainTable,open('main.pkl','wb'))

def retrieve():
    ratings = pk.load(open('ads.pkl','rb'))
    return ratings

def bestK(data):
   inertiaList = []
   X = list(range(2,30))
   print(X)
   for n in range(2,30):
      res = KMeans(init='k-means++').fit(data)
      inertiaList.append(res.inertia_)

   plt.plot(X,inertiaList)
   plt.show()
   
   

 
def kMeans(data):
   nclust = 8
   res = KMeans(init='k-means++').fit(data)
   clusterlist = []
   for k in range(nclust):
      clst = np.where(res.labels_ == k)
      clst = clst[0]*1
      clusterlist.append(clst)

   i = 0
   for clust in clusterlist:
      f = open('cluster' + str(i) + '.txt','w')
      for c in clust:
         f.write(adList[c])
      i += 1

def spentVClick(main):
  spent= main[main[:,8].argsort()]
  X = main[:,8]
  Y = main[:,7]
  plt.scatter(X,Y,s=5)
  plt.show()


def geodist(m):
   country =[x for x in m if str(x[16]) != 'nan']
   state = [x for x in m if str(x[17]) != 'nan']
   city = [x for x in m if str(x[18]) != 'nan']

   stlist = []
   statedict = dict()
   
   for s in state:
      x = s[17].split(';')
      for item in x:
         item = item.strip(' `')
         if item == '':
            print(s[0])
            exit()
         stlist.append(item)
         if statename_to_abbr[item] in statedict: #https://stackoverflow.com/questions/3199171/append-multiple-values-for-one-key-in-a-dictionary
            # append the new number to the existing array at this slot
            
            statedict[statename_to_abbr[item]].append(s)
         else:
            # create a new array in this slot
            statedict[statename_to_abbr[item]] = [s]
            
   stlist = np.array(stlist)
   c = Counter(stlist)
   c = c.items()
   c = sorted(c,key=lambda x: x[0])
   f = open('stateDistribution.txt','w')
   st = []
   num = []
   for item in c:
      st.append(statename_to_abbr[item[0]])
      num.append(item[1])
      f.write(str(item[0]) + ': ' + str(item[1]) + '\n')
   
   for key in statedict.keys():
      f = open('Ads_state/'+ str(key) + '_ads.txt', 'w')
      for ad in statedict[key]:
         f.write(str(ad[8]) + '\n\n')
   exit()
      
   plotly.tools.set_credentials_file(username='iJam', api_key='tfbPZcGBRdN74q52Czm7')
      
   scl = [
      [0.0, 'rgb(242,240,247)'], #https://plot.ly/python/choropleth-maps/
      [0.2, 'rgb(218,218,235)'],
      [0.4, 'rgb(188,189,220)'],
      [0.6, 'rgb(158,154,200)'],
      [0.8, 'rgb(117,107,177)'],
      [1.0, 'rgb(84,39,143)']
   ]
   
   data = [go.Choropleth(
   colorscale = scl,
   autocolorscale = False,
   locations = st,
   z = num,
   locationmode = 'USA-states',
   marker = go.choropleth.Marker(
      line = go.choropleth.marker.Line(
         color = 'rgb(255,255,255)',
         width = 2
      )),
   colorbar = go.choropleth.ColorBar(
      title = "Number of Ads")
   )]

   layout = go.Layout(
      title = go.layout.Title(
        text = 'Geographic Distribution of Targeted States in the Russian Ad Campaign'
    ),
    geo = go.layout.Geo(
        scope = 'usa',
        projection = go.layout.geo.Projection(type = 'albers usa'),
        showlakes = True,
        lakecolor = 'rgb(255, 255, 255)'),
   )

   fig = go.Figure(data = data, layout = layout)
   py.iplot(fig, filename = 'd3-cloropleth-map')

#ratings = retrieve()
#kMeans(ratings)
#bestK(ratings)


main = pk.load(open('main.pkl','rb'))
geodist(main)








# Code fixed Csv. Now all numbers. 0 where there is no rating
############################################
# print(ratings)
# for r in range(ratings.shape[0]):
#    for c in range(ratings.shape[1]):
#       print(r,c)
#       if math.isnan(ratings[r][c]):
#          ratings[r][c] = 0

# print(ratings)
# pk.dump(ratings,open('ads.pkl','wb'))
#############################################


