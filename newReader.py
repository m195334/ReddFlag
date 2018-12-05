#!/usr/bin/env python
import tika
import sys
import re
from tika import parser
import sqlite3
import os

# Regular Expression Outlines
adID = "\s*a\s*d\s*i\s*d\s*([0-9]*)"
targetedLocation = "\s*[A|a][D|d]\s*[T|t]argeting\s*[L|l]ocation[^:]*:\s*([A-Za-z\t .]+)"
interest = "\s*interests.\s*((\w|,|.)*)"
people = "\s*People\s*who\s*match:\s([A-Za-z\t .]+)*"
excluded = "\s*excluded\s*connections\s*[:|-]?\s*([A-Za-z\t .]+)"
age = "\s*age\s*[:|-]\s*([0-9]*\s*[+|-]?\s*[0-9]*[+|-]?)"
language = "\s*language\s*[:|-]?\s*([A-Za-z()\t .]+)"
placement = "\s*placements\s*[:|-]?\s*([A-Za-z\t .]+)"
URL = "\s*(http[\S]*)"
time = "\s*Creation\s*Date\s*[0-9]+/[0-9]+/[0-9]+\s*[\S]*\s*[\S]*\s*[\S]*"
timeEnd = "\s*End\s*Date\s*[0-9]+/[0-9]+/[0-9]+\s*[\S]*\s*[\S]*\s*[\S]*"
impressions = "ad\s*impressions\s*:?\s*([0-9]*)"
clicks = "ad\s*clicks\s*:?\s*([0-9]*)"
spend = "ad\s*spend\s*:?\s*([A-Za-z0-9()\t .]+)"
redactions = "redactions"
houseComm = "Select\s*Committee"

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
adImpression INTEGER,
adClicks INTEGER,
adSpend INTEGER,
imageLocation VARCHAR(20),
adText VARCHAR(100)
);"""

sql_command_insert = """INSERT INTO CommitteeInfo (entryNumber, adID, targetLocation, interests, peopleMatch, excluded, age, language, placement, URL, adCreateDate, adEndDate, adImpression, adClicks, adSpend, imageLocation, adText) 
  VALUES (NULL, "{adID}", "{tL}","{i}","{pM}","{ex}", "{a}","{l}","{p}","{URL}","{aCT}", "{aED}", "{aI}", "{aC}", "{aS}", "{iP}", "{aT}");"""

# This calls Tika to remove text from PDF and removes unneeded lines
def getFileData(fileName):
  try:
    parsed = parser.from_file('../ads/2015-06/P(1)0002262.pdf')
    parsed = parsed['content']
    parsed = parsed.splitlines()
    parsed = map(str, parsed)
    parsed = filter(None, parsed)
    return parsed
  except:
    print("fail")
    sys.exit(0)

# This searches through extracted text for datafields
def tryFind(parsed, finder, searchName, data):
  for item in enumerate(parsed):
    m = re.search(finder, item[1], flags = re.VERBOSE|re.IGNORECASE)
    if m:
      match = m.groups(0)[0]
      data.append(match)
      parsed.pop(item[0])
      return parsed, data
    else:
      continue
  data.append(None)
  return parsed, data

# This searches through extracted text to remove unneeded text
def findRemove(parsed, finder):
  for item in enumerate(parsed):
    m = re.search(finder, item[1], flags = re.VERBOSE|re.IGNORECASE)
    if m:
      parsed.pop(item[0])
  return parsed

def main():
  
  connection = sqlite3.connect("committeeInfo.db")
  cursor = connection.cursor()
  cursor.execute(sql_command_table_create)
 
  for root, dirs, filenames in os.walk("/home/m195334/Desktop/ads/"):
    for x in filenames:
      if x.endswith(".pdf"):
        data = []
        parsed = getFileData("/home/m195334/Desktop/ads/" + x)
        parsed, data = tryFind(parsed, adID, "Ad ID: ", data)
        parsed, data = tryFind(parsed, targetedLocation, "Targeted Locations: ", data)
        parsed, data  = tryFind(parsed, interest, "Interest: ", data)
        parsed, data  = tryFind(parsed, people, "People Who Match: ", data)
        parsed, data  = tryFind(parsed, excluded, "Excluded: ", data)
        parsed, data  = tryFind(parsed, age, "Age: ", data)
        parsed, data  = tryFind(parsed, language, "Language: ", data)
        parsed, data  = tryFind(parsed, placement, "Placement: ", data)
        parsed, data  = tryFind(parsed, URL, "URL: ", data)
        parsed, data  = tryFind(parsed, time, "Ad Creation Date: ", data)
        parsed, data  = tryFind(parsed, timeEnd, "Ad End Date: ", data)
        parsed, data  = tryFind(parsed, impressions, "Ad Impressions: ", data)
        parsed, data  = tryFind(parsed, clicks, "Ad Clicks: ", data)
        parsed, data = tryFind(parsed, spend, "Ad Spend: ", data)
        parsed = findRemove(parsed, redactions)
        parsed = findRemove(parsed, houseComm)
        data.append("".join(parsed))
        next_command = sql_command_insert.format(adID =data[0], tL = data[1], i = data[2], pM = data[3], ex = data[4], a = data[5], l = data[6], p = data[7], URL = data[8], aCT = data[9], aED = data[10], aI  = data[11], aC = data[12], aS = data[13], iP = x, aT = data[14])
        cursor.execute(next_command)
        connection.commit()
  connection.close()

if __name__=="__main__":
  main()
