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
redactions = "redactions|Select\s*Committee|US\s*House\s*Permanent"
redaction1 = "Select\s*Committee"

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

def main():
  
  connection = sqlite3.connect("CommitteeInfo.db")
  cursor = connection.cursor()
  cursor.execute(sql_command_table_create)

  for root, dirs, files in os.walk(os.path.abspath("/home/m195334/Desktop/ads/")):
    for file in files:
          data = []
          parsed = getFileData(os.path.join(root, file))
          parsed, data = tryFind(parsed, adID, data)
          parsed, data = tryFind(parsed, targetedLocation, data)
          parsed, data  = tryFind(parsed, interest, data)
          parsed, data  = tryFind(parsed, people, data)
          parsed, data  = tryFind(parsed, excluded, data)
          parsed, data  = tryFind(parsed, age, data)
          parsed, data  = tryFind(parsed, language, data)
          parsed, data  = tryFind(parsed, placement, data)
          parsed, data  = tryFind(parsed, URL,  data)
          parsed, data  = tryFind(parsed, time, data)
          parsed, data  = tryFind(parsed, timeEnd,  data)
          parsed, data  = tryFind(parsed, impressions, data)
          parsed, data  = tryFind(parsed, clicks, data)
          parsed, data = tryFind(parsed, spend, data)
          parsed = findRemove(parsed, redactions)
          parsed = findRemove(parsed, redaction1)
          
          data.append("".join(parsed))
         
          cursor.execute("INSERT INTO CommitteeInfo (entryNumber, adID, targetLocation, interests, peopleMatch, excluded, age, language, placement, URL, adCreateDate, adEndDate, adImpression, adClicks, adSpend, imageLocation, adText) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?)", (None, data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], os.path.join(root, file), data[14]))
          
          connection.commit()
  connection.close()

if __name__=="__main__":
  main()
