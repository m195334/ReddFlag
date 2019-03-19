import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle as pk
from sklearn.cluster import KMeans, MiniBatchKMeans
import math

def preprocess():
   data =  pd.read_csv('AdMatrix.csv', sep=',')
   data = np.array(data)

   #txtFile = open('adText.txt','r')
 
   pk.dump(data,open('ads.pkl','wb'))

def retrieve():
    ratings = pk.load(open('ads.pkl','rb'))
    return ratings

def kMeans(data):
   nclust = 8
   res = KMeans(init='k-means++').fit(data)
   clusterlist = []
   for k in range(nclust):
      clst = np.where(res.labels_ == k)
      clst = clst[0]*1
      print(clst)
      clusterlist.append(clst)

   print(clusterlist)
   
   

ratings = retrieve()
kMeans(ratings)

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


