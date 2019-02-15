#!/usr/bin/env python
import sys
import re
import sqlite3
import os
import json
from pprint import pprint
import string


def main():

  connection = sqlite3.connect("ReddFlag.db")


  with open("../JSONS/JSON_Version_of_ads_28Jan2019.txt") as jsonFile:

    data = json.load(jsonFile)
    cursor = connection.cursor()


    for x in range(0, len(data)):
      data[x] = (dict(map(lambda (key, value):(key,value),data[x].items())))
      flagsFound = []
      dataStore = []
      def addingFunction1(stringNew):
        try:
          dictionaryString = data[x][stringNew]
          if(stringNew == "HashTags"):
            dictionaryString = ''.join(dictionaryString)
        except KeyError:
          dictionaryString = None
        dataStore.append(dictionaryString)

      def addingFunction2(stringNew, stringNew2):
        try:
          dictionaryString = data[x][stringNew][stringNew2]
        except KeyError:
          dictionaryString = None
        dataStore.append(dictionaryString)

      def addingFunction3(stringNew, stringNew2, stringNew3):
        try:
          dictionaryString = data[x][stringNew][stringNew2][stringNew3]
        except KeyError:
          dictionaryString = None
        dataStore.append(dictionaryString)

      addingFunction1("AdID")
      addingFunction1("JSON_name")
      addingFunction1("FileName")
      addingFunction1("StartDate")
      addingFunction1("EndDate")
      addingFunction1("Impressions")
      addingFunction1("Clicks")
      addingFunction1("Spent")
      addingFunction1("AdText")
      addingFunction1("ImageText")
      addingFunction1("HashTags")
      addingFunction1("AdLandingPage")
      addingFunction1("CustomIncludes")
      addingFunction1("Junk")
      addingFunction2("AdTarget", "Placements")
      addingFunction2("AdTarget", "Age")
      addingFunction2("AdTarget", "Location")
      addingFunction2("AdTarget", "Language")
      addingFunction2("AdTarget", "Loose")
      addingFunction2("AdTarget", "Gender")
      addingFunction3("AdTarget","PeopleWhoMatch", "All")
      addingFunction3("AdTarget","PeopleWhoMatch", "Behaviors")
      addingFunction3("AdTarget","PeopleWhoMatch", "FieldOfStudy")
      addingFunction3("AdTarget","PeopleWhoMatch", "Politics")
      addingFunction3("AdTarget","PeopleWhoMatch", "Interests")
      addingFunction3("AdTarget","PeopleWhoMatch", "FriendsOfConnections")
      addingFunction3("AdTarget","PeopleWhoMatch", "MulticulturalAffinity")
      addingFunction3("AdTarget","PeopleWhoMatch", "PeopleWhoLike")
      addingFunction3("AdTarget","PeopleWhoMatch", "Industry")
      addingFunction3("AdTarget","PeopleWhoMatch", "Employers")
      addingFunction3("AdTarget","AndMustAlsoMatch", "All")
      addingFunction3("AdTarget","AndMustAlsoMatch", "Interests")
      addingFunction3("AdTarget","AndMustAlsoMatch", "Politics")
      addingFunction3("AdTarget","AndMustAlsoMatch", "Behaviors")
      addingFunction3("AdTarget","AndMustAlsoMatch", "MulticulturalAffinity")
      addingFunction3("AdTarget","AndMustAlsoMatch", "Industry")
      addingFunction3("AdTarget","AndMustAlsoMatch", "Employers")
      addingFunction3("AdTarget","ExcludedConnections", "All")
      addingFunction3("AdTarget","ExcludedConnections", "ExcludePeopleWhoLike")
      addingFunction3("AdTarget","ExcludedConnections", "ExcludePeopleWhoAreGoingTo")
      addingFunction3("AdTarget","Exclude", "All")
      addingFunction3("AdTarget","Exclude", "MulticulturalAffinity")
      addingFunction3("AdTarget","Exclude", "Behaviors")
      try:
        words = str(dataStore[8]).split()
        average =  sum(len(word) for word in words) / len(words)
      except:
        average = None

      try:
        cursor.execute("INSERT INTO MainTable (EntryNumber, AdID, JSON_name, FileName, StartDate, EndDate, Impressions, Clicks, Spent, AdText, ImageText, HashTags, AdLandingPage, CustomIncludes, Junk, AT_Placements, AT_Age, AT_Location, AT_Language, AT_Loose, AT_Gender, AT_PM_All, AT_PM_Behaviors, AT_PM_FieldOfStudy, AT_PM_Politics, AT_PM_Interests, AT_PM_FriendsOfConnections, AT_PM_MulticulturalAffinity, AT_PM_PeopleWhoLike, AT_PM_Industry, AT_PM_Employers, AT_AM_All, AT_AM_Interests, AT_AM_Politics, AT_AM_Behaviors, AT_AM_MulticulturalAffinity, AT_AM_Industry, AT_AM_Employers, AT_EC_All, AT_EC_ExcludePeopleWhoLike, AT_EC_ExcludePeopleWhoAreGoingTo, AT_EX_All, AT_EX_MulticulturalAffinity, AT_EX_Behaviors, avgWordLength) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (None, int(dataStore[0]), dataStore[1], dataStore[2], dataStore[3], dataStore[4], int(dataStore[5]), int(dataStore[6]), dataStore[7], dataStore[8], dataStore[9], dataStore[10], dataStore[11], dataStore[12], dataStore[13], dataStore[14], dataStore[15], dataStore[16], dataStore[17], dataStore[18], dataStore[19], dataStore[20], dataStore[21], dataStore[22], dataStore[23], dataStore[24], dataStore[25], dataStore[26], dataStore[27], dataStore[28], dataStore[29], dataStore[30], dataStore[31], dataStore[32], dataStore[33], dataStore[34], dataStore[35], dataStore[36], dataStore[37], dataStore[38], dataStore[39], dataStore[40], dataStore[41], dataStore[42],  average))
      except:
        continue
  connection.commit()
  connection.close()
if __name__=="__main__":
  main()
