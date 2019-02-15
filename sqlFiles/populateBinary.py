#!/usr/bin/env python
import sys
import re
import sqlite3
import os

BlackCulture ="black|african|pan-african|Black\s*Lives\s*Matter"
BlueLives  = "police|law\s*enforcement|cop"
Refugees = "immigrant|invader|refugee|immigration(s?)|wall|caravan"
Texas = "Texas|community"
SouthernCulture = "Southern|south|confederate|history"
Seperatist = "seperatist|calexit|texit|secede|secession|movement"
Muslim = "muslim|mosque|arab|islam|allah"
Christian = "church|christian|jesus|baptist|god"
LGBTQ = "lgbt|gay|lesbian|queer|pride"
NativeAmerican = "native\s*american"
RedPill = "meme|red\s*pill"
Patriot = "patriot|patriotic|nationalism|tea\s*party"
LiberalFeminism = "liberal|left|feminism|feminist|women"
Veterans = "veteran|va|vet"
SecondAmendment = "gun|2nd|amendment|second\s*amendment"
Syria = "syria|isis|pro-assad|assad"
ISIS = "isis|isil"
Media = "media|news|newspaper|trustworth"
NewsAndEvents = ""
Trump = "trump|donald|president|apprentice"
Clinton = "clinton|hillary|killary"
Sanders = "sanders|bernie|bern"
otherCandidates = "stein"
voterFraud = "voter\s*fraud|fraudulent|voting|vote|polls|election"
voterMisdirection = "voter|polling|votes|vote|election"
voterTurnoutSuppression = "voter|polling|votes|vote|election"

BinaryFlagTableNames = ["BlackCulture", "BlueLives", "Refugees",
 "Texas", "SouthernCulture",
 "Seperatist", "Muslim",
 "Christian", "LGBTQ",
 "NativeAmerican", "RedPill",
 "Patriot", "LiberalFeminism",
 "Veterans", "SecondAmendment",
 "Syria", "Media",
 "NewsAndEvents", "Trump",
 "Clinton", "Sanders",
 "otherCandidates", "voterFraud",
 "voterMisdirection", "voterTurnoutSuppression"]

def findFlags(AdText):
    try:
      AdText = str(AdText)
    except:
      return []
    flagsFound = []
    flagsFound.append(re.search(BlackCulture, AdText, flags = re.VERBOSE|re.IGNORECASE))
    flagsFound.append(re.search(BlueLives, AdText, flags = re.VERBOSE|re.IGNORECASE))
    flagsFound.append(re.search(Refugees, AdText, flags = re.VERBOSE|re.IGNORECASE))
    flagsFound.append(re.search(Texas, AdText, flags = re.VERBOSE|re.IGNORECASE))
    flagsFound.append(re.search(SouthernCulture, AdText, flags = re.VERBOSE|re.IGNORECASE))
    flagsFound.append(re.search(Seperatist, AdText, flags = re.VERBOSE|re.IGNORECASE))
    flagsFound.append(re.search(Muslim, AdText, flags = re.VERBOSE|re.IGNORECASE))
    flagsFound.append(re.search(Christian, AdText, flags = re.VERBOSE|re.IGNORECASE))
    flagsFound.append(re.search(LGBTQ, AdText, flags = re.VERBOSE|re.IGNORECASE))
    flagsFound.append(re.search(NativeAmerican, AdText, flags = re.VERBOSE|re.IGNORECASE))
    flagsFound.append(re.search(RedPill, AdText, flags = re.VERBOSE|re.IGNORECASE))
    flagsFound.append(re.search(Patriot, AdText, flags = re.VERBOSE|re.IGNORECASE))
    flagsFound.append(re.search(LiberalFeminism, AdText, flags = re.VERBOSE|re.IGNORECASE))
    flagsFound.append(re.search(Veterans, AdText, flags = re.VERBOSE|re.IGNORECASE))
    flagsFound.append(re.search(SecondAmendment, AdText, flags = re.VERBOSE|re.IGNORECASE))
    flagsFound.append(re.search(Syria, AdText, flags = re.VERBOSE|re.IGNORECASE))
    flagsFound.append(re.search(Media, AdText, flags = re.VERBOSE|re.IGNORECASE))
    flagsFound.append(re.search(NewsAndEvents, AdText, flags = re.VERBOSE|re.IGNORECASE))
    flagsFound.append(re.search(Trump, AdText, flags = re.VERBOSE|re.IGNORECASE))
    flagsFound.append(re.search(Clinton, AdText, flags = re.VERBOSE|re.IGNORECASE))
    flagsFound.append(re.search(Sanders, AdText, flags = re.VERBOSE|re.IGNORECASE))
    flagsFound.append(re.search(otherCandidates, AdText, flags = re.VERBOSE|re.IGNORECASE))
    flagsFound.append(re.search(voterFraud, AdText, flags = re.VERBOSE|re.IGNORECASE))
    flagsFound.append(re.search(voterMisdirection, AdText, flags = re.VERBOSE|re.IGNORECASE))
    flagsFound.append(re.search(voterTurnoutSuppression, AdText, flags = re.VERBOSE|re.IGNORECASE))

    returnedBinaries = []
    for x in range(0, len(flagsFound)):
        if (flagsFound[x]):
            returnedBinaries.append(1)
        else:
            returnedBinaries.append(0)
    return returnedBinaries

def runFlagChecks(EntryNumber, Filename, AdText, cursor):
    returnedBinaries = findFlags(AdText)
    for x in range(0, len(returnedBinaries)):
        if returnedBinaries[x] == True:
            statement = "INSERT INTO " + BinaryFlagTableNames[x] + " (EntryNumber) VALUES (" + str(EntryNumber)  + ");"
            cursor.execute(statement)

def main():

    connection = sqlite3.connect("ReddFlag.db")
    cursor = connection.cursor()

    statement = "SELECT EntryNumber, FileName, AdText FROM MainTable;"

    cursor.execute(statement)
    rows=cursor.fetchall()

    for row in rows:
        runFlagChecks(row[0], row[1], row[2], cursor)

    connection.commit()
    connection.close()

if __name__=="__main__":
  main()
