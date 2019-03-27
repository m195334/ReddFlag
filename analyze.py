import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle as pk
from sklearn.cluster import KMeans, MiniBatchKMeans
import math
import re
from collections import Counter

   
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
   country =[x for x in m if str(x[18]) != 'nan']
   state = [x for x in m if str(x[19]) != 'nan']
   city = [x for x in m if str(x[20]) != 'nan']

   stlist = []
   for s in state:
      x = s[19].split(';')
      for item in x:
         item = item.strip(' `')
         stlist.append(item)
   stlist = np.array(stlist)
   c = Counter(stlist)
   c = c.items()
   c = sorted(c,key=lambda x: x[0])
   f = open('stateDistribution.txt','w')
   for item in c:
      f.write(str(item[0]) + ': ' + str(item[1]) + '\n')
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


