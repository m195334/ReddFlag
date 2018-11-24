#!/usr/bin/env python
import tika
import sys
import re
from tika import parser


try:
  parsed = parser.from_file('../2015-06/P(1)0002117.pdf')
except:
  print("fail")
  sys.exit(0)


adID = re.compile("\s*a\s*d\s*i\s*d\s*([0-9]*)", flags = re.VERBOSE|re.IGNORECASE)

targetedLocation = re.compile("\s*[A|a][D|d]\s*[T|t]argeting\s*[L|l]ocation[^:]*:\s*([A-Za-z\t .]+)", flags = re.VERBOSE|re.IGNORECASE)

interest = re.compile("\s*interests.\s*((\w|,|.)*)", flags = re.VERBOSE|re.IGNORECASE)

people = re.compile("\s*People\s*who\s*match:\s([A-Za-z\t .]+)*", flags = re.VERBOSE|re.IGNORECASE)

excluded = re.compile("\s*excluded\s*connections\s*[:|-]?\s*([A-Za-z\t .]+)", flags = re.VERBOSE|re.IGNORECASE)

age = re.compile("\s*age\s*[:|-]\s*([0-9]*\s*[+|-]?\s*[0-9]*[+|-]?)", flags = re.VERBOSE|re.IGNORECASE)

language = re.compile("\s*language\s*[:|-]?\s*([A-Za-z()\t .]+)", flags = re.VERBOSE|re.IGNORECASE)

placement = re.compile("\s*placements\s*[:|-]?\s*([A-Za-z\t .]+)", flags = re.VERBOSE|re.IGNORECASE)

URL = re.compile("\s*(http[\S]*)", flags = re.VERBOSE|re.IGNORECASE)

time = re.compile("[0-9]+/[0-9]+/[0-9]+\s*[\S]*\s*[\S]*\s*[\S]*", flags = re.VERBOSE|re.IGNORECASE)

impressions = re.compile("ad\s*impressions\s*:?\s*([0-9]*)", flags = re.VERBOSE|re.IGNORECASE)

clicks = re.compile("ad\s*clicks\s*:?\s*([0-9]*)", flags = re.VERBOSE|re.IGNORECASE)

spend = re.compile("ad\s*spend\s*:?\s*([A-Za-z0-9()\t .]+)", flags = re.VERBOSE|re.IGNORECASE)

def tryFind(finder, searchName, f):
  x = " ".join(finder.findall(parsed["content"]))
  if(x != ""):
    f.write(searchName + x + "\n")
  else:
    f.write(searchName + " No Value\n")

f = open("inClassExample.txt", "w")
tryFind(adID, "ad ID: ", f)
tryFind(targetedLocation, "Targeted Locations: ", f)
tryFind(interest, "interest: ", f)
tryFind(people, "People Who Match: ", f)
tryFind(excluded, "Excluded: ", f)
tryFind(age, "Age: ", f)
tryFind(language, "Language: ", f)
tryFind(placement, "Placement: ", f)
tryFind(URL, "URL: ", f)
tryFind(time, "Time: ", f)
tryFind(impressions, "Ad Impressions: ", f)
tryFind(clicks, "Ad Clicks: ", f)
tryFind(spend, "Ad Spend: ", f)
f.close()
