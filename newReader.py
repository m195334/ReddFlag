#!/usr/bin/env python
import tika
import sys
import re
from tika import parser
import sqlite3
import os
from pdf2image import *


# Regular Expression Outlines
adID = "\s*a\s*d\s*i\s*d\s*([0-9]*)"
targetedLocation = "\s*[A|a][D|d]\s*[T|t]argeting\s*[L|l]ocation[^:]*:\s*([A-Za-z\t .]+)"
otherLocation = "\s*Location:?\s*([A-Za-z\t .]+)"
interest = "\s*interests.\s*((\w|,|.)*)"
people = "\s*People\s*who\s*match:\s([A-Za-z\t .]+)*"
excluded = "\s*excluded\s*connections\s*[:|-]?\s*([A-Za-z\t .]+)"
age = "\s*age\s*[:|-]\s*([0-9]*\s*[+|-]?\s*[0-9]*[+|-]?)"
language = "\s*language\s*[:|-]?\s*([A-Za-z()\t .]+)"
placement = "\s*placements\s*[:|-]?\s*([A-Za-z\t .]+)"
URL = "\s*(http[\S]*)"
dateString = "[(\s*Ad\s*End\s*Date)|(\s*Ad\s*Start\s*Date)|(\s*Ad\s*Suspend\s*Date)]?\s*[0-9]+/[0-9]+/[0-9]+\s*[\S]*\s*[\S]*\s*[\S]*"
impressions = "ad\s*impressions\s*:?\s*([0-9]*)"
clicks = "ad\s*clicks\s*:?\s*([0-9]*)"
spend = "ad\s*spend\s*:?\s*([A-Za-z0-9()\t .]+)"
spend2 = "([0-9]+\s*rub)"
redactions = "redactions|Select\s*Committee|US\s*House\s*Permanent"
redaction1 = "Select\s*Committee"
redaction2 = "\s*Ad\s*landing\s*"
redaction3 = "\s*ad\s*targeting\s*"
redaction4 = "\s*ad\s*spend\s*"
redaction5 = "\s*Ad\s*creation\s*"
redaction6 = "\s*Ad\s*end\s*"
blackCulture ="\s*"
police = ""
refugee = ""
texas = ""
southernCulture = ""
seperatist = ""
muslim = ""
christian = ""
lgbt = ""
nativeAm = ""
meme = ""
redPill = ""
patriotism = ""
liberal = ""
veteran = ""
gunRights = ""
syria = ""
isis = ""
media = ""
news = ""
trump = ""
clinton = ""
sanders = ""
otherCandidates = ""
vote_fraud = ""
vote_misdirection = ""
vote_suppression = ""



# SQL Commands

sql_command_table_create = """
CREATE TABLE IF NOT EXISTS CommitteeInfo (
entryNumber INTEGER PRIMARY KEY,
adID INTEGER,
targetLocation VARCHAR(30),
interests VARCHAR(30),
peopleMatch VARCHAR(30),
excluded VARCHAR(30),
age VARCHAR(10),
language VARCHAR(30),
placement VARCHAR(30),
URL VARCHAR(10),
adCreateDate VARCHAR(10),
adEndDate VARCHAR(10),
adSuspendDate VARCHAR(10),
adImpression INTEGER,
adClicks INTEGER,
adSpend INTEGER,
imageLocation VARCHAR(20),
adText VARCHAR(100)
);"""



# This calls Tika to remove text from PDF and removes unneeded lines
def getFileData(fileName):
  parsed = parser.from_file(fileName)
  parsed = parsed['content']
  parsed = parsed.splitlines()
  for x in range(0, len(parsed)):
    parsed[x] = parsed[x].encode('ascii', 'ignore')
  parsed = filter(None, parsed)
  return parsed

# This searches through extracted text for datafields
def tryFind(parsed, finder, data):
  try:
    for item in enumerate(parsed):
      m = re.search(finder, item[1], flags = re.VERBOSE|re.IGNORECASE)
      if m:
        match = m.groups(0)[0]
        data.append(match)
        parsed.pop(item[0])
        return parsed, data
      else:
        continue
    data.append("Null")
    return parsed, data
  except:
    data.append("Null")
    return parsed, data

# This searches through extracted text to remove unneeded text
def findRemove(parsed, finder):
  for item in enumerate(parsed):
    m = re.search(finder, item[1], flags = re.VERBOSE|re.IGNORECASE)
    if m:
      parsed.pop(item[0])
  return parsed

def findDates(parsed, finder, data):
  matches = []
  index = []
  for item in enumerate(parsed):
    m = re.search(finder, item[1], flags = re.VERBOSE|re.IGNORECASE)
    if m:
      matches.append(m)
      index.append(item[0])
  if(len(matches) == 1):
    data.append(matches[0].group(0))
    data.append("Null")
    data.append("Null")    
    parsed.pop(index[0])
    return parsed, data
  elif(len(matches) == 2):
    data.append(matches[0].group(0))
    data.append(matches[1].group(0))
    parsed.pop(index[0])
    parsed.pop(index[1])
    data.append("Null")
    return parsed, data
  elif(len(matches) == 3):
    data.append(matches[0].group(0))
    data.append(matches[1].group(0))
    data.append(matches[2].group(0))
    parsed.pop(index[0])
    parsed.pop(index[1])
    parsed.pop(index[2])
    return parsed, data
  else:
    data.append("Null")
    data.append("Null")
    data.append("Null")
    return parsed, data


def main():
  
  connection = sqlite3.connect("CommitteeInfo.db")
  cursor = connection.cursor()
  cursor.execute(sql_command_table_create)

  for root, dirs, files in os.walk(os.path.abspath("ads/")):
    for file in files:
          data = []
          print root, dirs, file
          #fname =  open("ads/2015-06/" + file,"r")
          # pages = convert_from_path("ads/2015-06/" + file, 500,output_folder='ads/img',last_page=True)
          # for page in pages:
          #   page.save(file + '.png')
          parsed = getFileData(os.path.join(root, file))
          parsed, data = tryFind(parsed, adID, data)
          parsed, data = tryFind(parsed, targetedLocation, data)
          parsed, data = tryFind(parsed, otherLocation, data)
          if (data[1] == "Null"):
            data[1] = data[2]
          elif (data[2] != "Null"):
            data[1] = data[1] + " " + data[2]
          data.pop()
          parsed, data  = tryFind(parsed, interest, data)
          parsed, data  = tryFind(parsed, people, data)
          parsed, data  = tryFind(parsed, excluded, data)
          parsed, data  = tryFind(parsed, age, data)
          parsed, data  = tryFind(parsed, language, data)
          parsed, data  = tryFind(parsed, placement, data)
          parsed, data  = tryFind(parsed, URL,  data)
          parsed, data = findDates(parsed, dateString, data)
          parsed, data  = tryFind(parsed, impressions, data)
          parsed, data  = tryFind(parsed, clicks, data)
          parsed, data = tryFind(parsed, spend, data)
          if(data[14] == "Null"):
            data.pop()
            parsed, data = tryFind(parsed, spend2, data)
          
          parsed = findRemove(parsed, redactions)
          parsed = findRemove(parsed, redaction1)
          parsed = findRemove(parsed,redaction2)
          parsed = findRemove(parsed,redaction3)
          parsed = findRemove(parsed,redaction4)
          parsed = findRemove(parsed,redaction5)
          parsed = findRemove(parsed,redaction6)
          
          data.append(" ".join(parsed))
         
          cursor.execute("INSERT INTO CommitteeInfo (entryNumber, adID, targetLocation, interests, peopleMatch, excluded, age, language, placement, URL, adCreateDate, adEndDate, adSuspendDate, adImpression, adClicks, adSpend, imageLocation, adText) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?)", (None, data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], os.path.join(root, file), data[15]))
          
          connection.commit()
  connection.close()

if __name__=="__main__":
  main()
