import csv, sys
import numpy as np
import pandas as pd
import researchpy as rp

#EntryNumber', 'AdID', 'FileName', 'StartDate', 'EndDate', 'Impressions', 'Clicks', 'Spent', 'AdText', 'ImageText', 'HashTags', 'AdLandingPage', 'CustomIncludes', 'Junk', 'AT_Placements', 'AT_Age', 'AT_Location_Country', 'AT_Location_State', 'AT_Location_City', 'AT_Language',
'''
with open("mainViewWithBinary.csv", "r") as f:
  #EntryNumber
  #AdId
  entries = list(csv.reader(f))
  FileNames = [w[2] for w in entries]
  StartDate = [w[3] for w in entries]
  Time
  Zone
  EndDate = [w[4] for w in entries]
  Impressions = [int(w[5]) for w in entries]
  Clicks = [int(w[6]) for w in entries]
  Spent = [float(w[7]) for w in entries]
  #AdText
  #Imagetext
  HashTags = [w[10] for w in entries]
  #Ad Landing Page
  #Custom Includes
  #Junk
  #At placement
  Ages = [w[15] for w in entries]
  Countries = [w[16] for w in entries]
  State = [w[17] for w in entries]
  City = [w[18] for w in entries]

#State Date Analysis
  StartDate = [w.split("_") for w in StartDate]
  rp.summary_cat(StartDate)
'''

table = pd.read_csv("mainViewWithBinary.csv")
print(table[['StartDate', 'Time', 'Zone', 'EndDate', 'Impressions', 'Clicks',
  'Spent']].describe())

print(rp.summary_cat(table['StartDate']))
print(table['StartDate'].mode())
