#!/usr/bin/env python
import sys
import csv
import re
import sqlite3
import os
import json
from pprint import pprint
import string


def main():
  fileName = "../updatedMain.csv"
  average = 0
  connection = sqlite3.connect("ReddFlag.db")
  with open(fileName) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    cursor = connection.cursor()
    next(csv_reader)
    for dataStore in csv_reader:
      try:
        cursor.execute("INSERT INTO MainTable (EntryNumber, AdID, FileName, StartDate, EndDate, Impressions, Clicks, Spent, AdText, ImageText, HashTags, AdLandingPage, CustomIncludes, Junk, AT_Placements, AT_Age, AT_Location_Country, AT_Location_State, AT_Language, AT_Loose, AT_Gender, AT_PM_All, AT_PM_Behaviors, AT_PM_FieldOfStudy, AT_PM_Politics, AT_PM_Interests, AT_PM_FriendsOfConnections, AT_PM_MulticulturalAffinity, AT_PM_PeopleWhoLike, AT_PM_Industry, AT_PM_Employers, AT_AM_All, AT_AM_Interests, AT_AM_Politics, AT_AM_Behaviors, AT_AM_MulticulturalAffinity, AT_AM_Industry, AT_AM_Employers, AT_EC_All, AT_EC_ExcludePeopleWhoLike, AT_EC_ExcludePeopleWhoAreGoingTo, AT_EX_All, AT_EX_MulticulturalAffinity, AT_EX_Behaviors, avgWordLength) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (int(dataStore[0]), dataStore[1], dataStore[2], dataStore[3], dataStore[4], int(dataStore[5]), int(dataStore[6]), dataStore[7], dataStore[8], dataStore[9], dataStore[10], dataStore[11], dataStore[12], dataStore[13], dataStore[14], dataStore[15], dataStore[16], dataStore[17], dataStore[18], dataStore[19], dataStore[20], dataStore[21], dataStore[22], dataStore[23], dataStore[24], dataStore[25], dataStore[26], dataStore[27], dataStore[28], dataStore[29], dataStore[30], dataStore[31], dataStore[32], dataStore[33], dataStore[34], dataStore[35], dataStore[36], dataStore[37], dataStore[38], dataStore[39], dataStore[40], dataStore[41], dataStore[42], dataStore[43], average)) 
      except:
        continue
  connection.commit()
  connection.close()
if __name__=="__main__":
  main()
