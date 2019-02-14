#!/usr/bin/env python
import sys
import re
import sqlite3
import os
import json
from pprint import pprint
import string


sql_command_table_delete = """DROP TABLE IF EXISTS CommitteeInfo;"""

sql_command_table_create = """
CREATE TABLE IF NOT EXISTS CommitteeInfo (
entryNumber INTEGER PRIMARY KEY,
AdID VARCHAR(100),
JSON_name VARCHAR(100),
FileName VARCHAR(100),
StartDate VARCHAR(100),
EndDate VARCHAR(100),
Impressions VARCHAR(100),
Clicks VARCHAR(100),
Spent VARCHAR(100),
AdText VARCHAR(100),
ImageText VARCHAR(100),
HashTags VARCHAR(100),
AdLandingPage VARCHAR(100),
CustomIncludes VARCHAR(100),
Junk VARCHAR(100),
AT_Placements VARCHAR(100),
AT_Age VARCHAR(100),
AT_Location VARCHAR(100),
AT_Language VARCHAR(100),
AT_Loose VARCHAR(100),
AT_Gender VARCHAR(100),
AT_PM_All VARCHAR(100),
AT_PM_Behaviors VARCHAR(100),
AT_PM_FieldOfStudy VARCHAR(100),
AT_PM_Politics VARCHAR(100),
AT_PM_Interests VARCHAR(100),
AT_PM_FriendsOfConnections VARCHAR(100),
AT_PM_MulticulturalAffinity VARCHAR(100),
AT_PM_PeopleWhoLike VARCHAR(100),
AT_PM_Industry VARCHAR(100),
AT_PM_Employers VARCHAR(100),
AT_AM_All VARCHAR(100),
AT_AM_Interests VARCHAR(100),
AT_AM_Politics VARCHAR(100),
AT_AM_Behaviors VARCHAR(100),
AT_AM_MulticulturalAffinity VARCHAR(100),
AT_AM_Industry VARCHAR(100),
AT_AM_Employers VARCHAR(100),
AT_EC_All VARCHAR(100),
AT_EC_ExcludePeopleWhoLike VARCHAR(100),
AT_EC_ExcludePeopleWhoAreGoingTo VARCHAR(100),
AT_EX_All VARCHAR(100),
AT_EX_MulticulturalAffinity VARCHAR(100),
AT_EX_Behaviors VARCHAR(100),
blackCultureCommunityBlackLM INTEGER,
blueLMPolice INTEGER,
refugeesimmigration INTEGER,
Texas INTEGER,
SoutherCulture INTEGER,
Separatist INTEGER,
Muslim INTEGER,
Christian INTEGER,
LGBTQ INTEGER,
NativeAmerican INTEGER,
MemeRedPill INTEGER,
Patriotism INTEGER,
LiberalFeminism INTEGER,
Veterans INTEGER,
Gun2ndAmend INTEGER,
Syria INTEGER,
Media INTEGER,
newsAndEvents INTEGER,
Trump INTEGER,
Clinton INTEGER,
Sanders INTEGER,
otherCandidates  INTEGER,
voterFraud INTEGER,
voterMisdirection INTEGER,
voterTurnoutSuppression INTEGER,
avgWordLength INTEGER);"""

def main():

  blackCulture ="black|african|pan-african|Black\s*Lives\s*Matter"
  police = "police|law\s*enforcement|cop"
  refugee = "immigrant|invader|refugee|immigration(s?)|wall|caravan"
  texas = "Texas|community"
  southernCulture = "Southern|south|confederate|history"
  seperatist = "seperatist|calexit|texit|secede|secession|movement"
  muslim = "muslim|mosque|arab|islam|allah"
  christian = "church|christian|jesus|baptist|god"
  lgbt = "lgbt|gay|lesbian|queer|pride"
  nativeAm = "native\s*american"
  meme = "meme|red\s*pill"
  patriotism = "patriot|patriotic|nationalism|tea\s*party"
  liberal = "liberal|left|feminism|feminist|women"
  veteran = "veteran|va|vet"
  gunRights = "gun|2nd|amendment|second\s*amendment"
  syria = "syria|isis|pro-assad|assad"
  isis = "isis|isil"
  media = "media|news|newspaper|trustworth"
  trump = "trump|donald|president|apprentice"
  clinton = "clinton|hillary|killary"
  sanders = "sanders|bernie|bern"
  otherCandidates = "stein"
  vote_fraud = "voter\s*fraud|fraudulent|voting|vote|polls|election"
  vote_misdirection = "voter|polling|votes|vote|election"
  vote_suppression = "voter|polling|votes|vote|election"


  connection = sqlite3.connect("mlFlagsAddedtoParsedData.db")


  with open("JSONS/JSON_Version_of_ads_28Jan2019.txt") as jsonFile:
    data = json.load(jsonFile)
    cursor = connection.cursor()
    cursor.execute(sql_command_table_delete)    
    cursor.execute(sql_command_table_create)

    for x in range(0, len(data)):
      data[x] = (dict(map(lambda (key, value):(key,value),data[x].items())))
      flagsFound = []

      def findFlag(finder):
        m = re.search(finder, str(data[x]), flags = re.VERBOSE|re.IGNORECASE)
        if m:
          flagsFound.append(True)
          #print('Found')
          #print(finder)
          #print(data[x])
        else:
          flagsFound.append(False)

      findFlag(blackCulture)
      findFlag(police)
      findFlag(refugee)
      findFlag(texas)
      findFlag(southernCulture)
      findFlag(seperatist)
      findFlag(muslim)
      findFlag(christian)
      findFlag(lgbt)
      findFlag(nativeAm)
      findFlag(meme)
      findFlag(patriotism)
      findFlag(liberal)
      findFlag(veteran)
      findFlag(gunRights)
      findFlag(syria)
      findFlag(isis)
      findFlag(media)
      findFlag(trump)
      findFlag(clinton)
      findFlag(sanders)
      findFlag(otherCandidates)
      findFlag(vote_fraud)
      findFlag(vote_misdirection)
      findFlag(vote_suppression)

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
      # HASHTAGS ARE LIST
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
      #Datastore 10 is hashtags  
      cursor.execute("INSERT INTO CommitteeInfo (entryNumber, AdID, JSON_name,FileName, StartDate, EndDate, Impressions, Clicks, Spent, AdText, ImageText, HashTags, AdLandingPage, CustomIncludes, Junk, AT_Placements, AT_Age, AT_Location, AT_Language, AT_Loose, AT_Gender, AT_PM_All, AT_PM_Behaviors, AT_PM_FieldOfStudy, AT_PM_Politics, AT_PM_Interests, AT_PM_FriendsOfConnections, AT_PM_MulticulturalAffinity, AT_PM_PeopleWhoLike, AT_PM_Industry, AT_PM_Employers, AT_AM_All, AT_AM_Interests, AT_AM_Politics, AT_AM_Behaviors, AT_AM_MulticulturalAffinity, AT_AM_Industry, AT_AM_Employers, AT_EC_All, AT_EC_ExcludePeopleWhoLike, AT_EC_ExcludePeopleWhoAreGoingTo, AT_EX_All, AT_EX_MulticulturalAffinity, AT_EX_Behaviors, blackCultureCommunityBlackLM,blueLMPolice, refugeesimmigration, Texas, SoutherCulture, Separatist, Muslim, Christian, LGBTQ, NativeAmerican, MemeRedPill, Patriotism, LiberalFeminism, Veterans, Gun2ndAmend, Syria, Media, newsAndEvents, Trump, Clinton, Sanders,  otherCandidates, voterFraud, voterMisdirection, voterTurnoutSuppression, avgWordLength) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )", (None, dataStore[0], dataStore[1], dataStore[2], dataStore[3], dataStore[4], dataStore[5], dataStore[6], dataStore[7], dataStore[8], dataStore[9], dataStore[10], dataStore[11], dataStore[12], dataStore[13], dataStore[14], dataStore[15], dataStore[16], dataStore[17], dataStore[18], dataStore[19], dataStore[20], dataStore[21], dataStore[22], dataStore[23], dataStore[24], dataStore[25], dataStore[26], dataStore[27], dataStore[28], dataStore[29], dataStore[30], dataStore[31], dataStore[32], dataStore[33], dataStore[34], dataStore[35], dataStore[36], dataStore[37], dataStore[38], dataStore[39], dataStore[40], dataStore[41], dataStore[42], flagsFound[0], flagsFound[1],flagsFound[2],flagsFound[3],flagsFound[4],flagsFound[5],flagsFound[6],flagsFound[7],flagsFound[8],flagsFound[9],flagsFound[10],flagsFound[11],flagsFound[12],flagsFound[13],flagsFound[14],flagsFound[15],flagsFound[16],flagsFound[17],flagsFound[18],flagsFound[19],flagsFound[20],flagsFound[21],flagsFound[22],flagsFound[23], flagsFound[24], average))

  connection.commit()
  connection.close()
if __name__=="__main__":
  main()
