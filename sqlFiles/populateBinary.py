#!/usr/bin/env python
import sys
import re
import sqlite3
import os
BlackCulture ="black|african|pan-african|Black\s*Lives\s*Matter|melanin|diversity|blackout|malcolm|minority|minorities|race|color|africa|civil\s*rights|panthers|fist|resistance"
BlueLives  = "police|law\s*enforcement|cop|pigs|pig|50|five-o|12|twelve|officers|blue|blue\s*lives\s*matter"
Refugees = "immigrant|invader|refugee|immigration|wall|caravan|border|chicana|latino|latina|aliens|illegal"
Texas = "Texas|community|texans|dallas|splendora|lone\s*star|texans|rebels"
SouthernCulture = "Southern|south|confederate|history"
Seperatist = "supremacist|seperatist|calexit|texit|secede|secession|movement"
Muslim = "burga|terrorism|muslim|mosque|arab|islam|allah|malcolm|muhammad|terrorist|islamophobia|koran|mecca|quran"
Christian = "church|christian|jesus|baptist|god|bible"
LGBTQ = "lgbt|gay|lesbian|queer|pride|dream|bi|transgender|straight|community|lgbtq|ellen|degeneres|equalrights|homosexual|homo|homophobia"
NativeAmerican = "native\s*american|indian"
RedPill = "meme|red\s*pill|memopolis"
Patriot = "patriot|patriotic|nationalism|tea\s*party|patriotism|country|anthem"
LiberalFeminism = "liberal|left|feminism|feminist|women"
Veterans = "veteran|va|vet|marine|vets|combat|veterans|VA|soldiers"
SecondAmendment = "gun\s*control|gun|2nd|amendment|second\s*amendment|shot|shoot|gunfire|shooting|bullets|open\s*carry|gunsense|zealots"
Syria = "syria|isis|pro-assad|assad"
ISIS = "isis|isil|terrorist|terrorism"
Media = "media|news|newspaper|trustworth"
NewsAndEvents = "media"
Trump = "trump|donald|president|apprentice|not\s*my\s*president"
Clinton = "clinton|hillary|killary|secretary|democratic|democrat"
Sanders = "sanders|bernie|bern|independent|buff\s*bernie|berniacs"
otherCandidates = "stein|mike\s*huckabee|huckabee|hackabee"
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
