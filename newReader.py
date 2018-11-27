#!/usr/bin/env python
import tika
import sys
import re
from tika import parser


adID = re.compile("\s*a\s*d\s*i\s*d\s*([0-9]*)", flags = re.VERBOSE|re.IGNORECASE)
targetedLocation = re.compile("\s*[A|a][D|d]\s*[T|t]argeting\s*[L|l]ocation[^:]*:\s*([A-Za-z\t .]+)", flags = re.VERBOSE|re.IGNORECASE)
interest = re.compile("\s*interests.\s*((\w|,|.)*)", flags = re.VERBOSE|re.IGNORECASE)
people = re.compile("\s*People\s*who\s*match:\s([A-Za-z\t .]+)*", flags = re.VERBOSE|re.IGNORECASE)
excluded = re.compile("\s*excluded\s*connections\s*[:|-]?\s*([A-Za-z\t .]+)", flags = re.VERBOSE|re.IGNORECASE)
age = re.compile("\s*age\s*[:|-]\s*([0-9]*\s*[+|-]?\s*[0-9]*[+|-]?)", flags = re.VERBOSE|re.IGNORECASE)
language = re.compile("\s*language\s*[:|-]?\s*([A-Za-z()\t .]+)", flags = re.VERBOSE|re.IGNORECASE)
placement = re.compile("\s*placements\s*[:|-]?\s*([A-Za-z\t .]+)", flags = re.VERBOSE|re.IGNORECASE)
URL = re.compile("\s*(http[\S]*)", flags = re.VERBOSE|re.IGNORECASE)
time = re.compile("\s*Creation\s*Date\s*[0-9]+/[0-9]+/[0-9]+\s*[\S]*\s*[\S]*\s*[\S]*", flags = re.VERBOSE|re.IGNORECASE)
timeEnd = re.compile("\s*End\s*Date\s*[0-9]+/[0-9]+/[0-9]+\s*[\S]*\s*[\S]*\s*[\S]*", flags = re.VERBOSE|re.IGNORECASE)
impressions = re.compile("ad\s*impressions\s*:?\s*([0-9]*)", flags = re.VERBOSE|re.IGNORECASE)
clicks = re.compile("ad\s*clicks\s*:?\s*([0-9]*)", flags = re.VERBOSE|re.IGNORECASE)
spend = re.compile("ad\s*spend\s*:?\s*([A-Za-z0-9()\t .]+)", flags = re.VERBOSE|re.IGNORECASE)
redactions = re.compile("redactions", flags = re.VERBOSE|re.IGNORECASE)
houseComm = re.compile("Select\s*Committee", flags = re.VERBOSE|re.IGNORECASE)

def getFileData(fileName):
  try:
    parsed = parser.from_file('../2015-06/P(1)0002117.pdf')
    parsed = parsed['content']
    parsed = parsed.splitlines()
    parsed = map(str, parsed)
    parsed = filter(None, parsed)
    return parsed
  except:
    print("fail")
    sys.exit(0)

def tryFind(parsed, finder, searchName, f):
  x = [i for i, item in enumerate(parsed) if re.findall(finder, item)]
  if len(x) == 1:
    x = x[0]
    f.write(parsed[x] + "\n")
    parsed.pop(x)
  else:
    f.write(searchName + " No Value\n")
  return parsed

def findRemove(parsed, finder):
  x = [i for i, item in enumerate(parsed) if re.findall(finder, item)]
  for y in x:
    parsed.pop(y)
  return parsed

parsed = getFileData("none")
adID = ''.join(filter(adID.findall, parsed))
f = open(adID + ".txt", "w")
parsed = tryFind(parsed, adID, "Ad ID ", f)
parsed = tryFind(parsed, targetedLocation, "Targeted Locations ", f)
parsed = tryFind(parsed, interest, "Interest ", f)
parsed = tryFind(parsed, people, "People Who Match ", f)
parsed = tryFind(parsed, excluded, "Excluded ", f)
parsed = tryFind(parsed, age, "Age ", f)
parsed = tryFind(parsed, language, "Language ", f)
parsed = tryFind(parsed, placement, "Placement ", f)
parsed = tryFind(parsed, URL, "URL ", f)
parsed = tryFind(parsed, time, "Ad Creation Date ", f)
parsed = tryFind(parsed, timeEnd, "Ad End Date ", f)
parsed = tryFind(parsed, impressions, "Ad Impressions ", f)
parsed = tryFind(parsed, clicks, "Ad Clicks ", f)
parsed = tryFind(parsed, spend, "Ad Spend ", f)
parsed = findRemove(parsed, redactions)
parsed = findRemove(parsed, houseComm)

f.write(" ".join(parsed) + "\n")
f.close()
