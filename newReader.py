#!/usr/bin/env python
import tika
import sys
import re
from tika import parser


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

def getFileData(fileName):
  try:
    parsed = parser.from_file('../2015-06/P(1)0002262.pdf')
    parsed = parsed['content']
    parsed = parsed.splitlines()
    parsed = map(str, parsed)
    parsed = filter(None, parsed)
    return parsed
  except:
    print("fail")
    sys.exit(0)

def tryFind(parsed, finder, searchName, f):
  for item in enumerate(parsed):
    m = re.search(finder, item[1], flags = re.VERBOSE|re.IGNORECASE)
    if m:
      match = m.groups(0)[0]
      f.write(searchName + match + "\n")
      parsed.pop(item[0])
      return parsed
    else:
      continue
  f.write(searchName + " No Value\n")
  return parsed

def findRemove(parsed, finder):
  x = [i for i, item in enumerate(parsed) if re.findall(finder, item)]
  for y in x:
    parsed.pop(y)
  return parsed


filename = "none"
parsed = getFileData(filename)
f = open("readAds/" + filename, "w")
parsed = tryFind(parsed, adID, "Ad ID: ", f)
parsed = tryFind(parsed, targetedLocation, "Targeted Locations: ", f)
parsed = tryFind(parsed, interest, "Interest: ", f)
parsed = tryFind(parsed, people, "People Who Match: ", f)
parsed = tryFind(parsed, excluded, "Excluded: ", f)
parsed = tryFind(parsed, age, "Age: ", f)
parsed = tryFind(parsed, language, "Language: ", f)
parsed = tryFind(parsed, placement, "Placement: ", f)
parsed = tryFind(parsed, URL, "URL: ", f)
parsed = tryFind(parsed, time, "Ad Creation Date: ", f)
parsed = tryFind(parsed, timeEnd, "Ad End Date: ", f)
parsed = tryFind(parsed, impressions, "Ad Impressions: ", f)
parsed = tryFind(parsed, clicks, "Ad Clicks: ", f)
parsed = tryFind(parsed, spend, "Ad Spend: ", f)
parsed = findRemove(parsed, redactions)
parsed = findRemove(parsed, houseComm)
f.write(" ".join(parsed) + "\n")
f.close()
