#!/usr/bin/env python
import tika
import sys
import re
from tika import parser


try:
  parsed = parser.from_file('2015-q2/2015-06/P(1)0000182.pdf')
except:
  print("fail")
  sys.exit(0)


adIDFind = re.compile("\s*a\s*d\s*i\s*d\s*([0-9]*)", flags = re.VERBOSE|re.IGNORECASE)

locationFind = re.compile("\s*location.\s*((\w|.)*)", flags = re.VERBOSE|re.IGNORECASE)

interestFind = re.compile("\s*interests.\s*((\w|,|.)*)", flags = re.VERBOSE|re.IGNORECASE)

excludedFind = re.compile("\s*excluded\s*connections\s*[:|-]?\s*([A-Za-z\t .]+)", flags = re.VERBOSE|re.IGNORECASE)

ageFind = re.compile("\s*age\s*[:|-]\s*([0-9]*\s*[+|-]?\s*[0-9]*[+|-]?)", flags = re.VERBOSE|re.IGNORECASE)

languageFind = re.compile("\s*language\s*[:|-]?\s*([A-Za-z()\t .]+)", flags = re.VERBOSE|re.IGNORECASE)

placementFind = re.compile("\s*placements\s*[:|-]?\s*([A-Za-z\t .]+)", flags = re.VERBOSE|re.IGNORECASE)

URLFind = re.compile("\s*(http[\S]*)", flags = re.VERBOSE|re.IGNORECASE)

timeFind = re.compile("[0-9]+/[0-9]+/[0-9]+\s*[\S]*\s*[\S]*\s*[\S]*", flags = re.VERBOSE|re.IGNORECASE)


adID = adIDFind.findall(parsed["content"])
location = locationFind.findall(parsed["content"])
interest = interestFind.findall(parsed["content"])
excluded = excludedFind.findall(parsed["content"])
age = ageFind.findall(parsed["content"])
language = languageFind.findall(parsed["content"])
placement = placementFind.findall(parsed["content"])
URL = URLFind.findall(parsed["content"])
time = timeFind.findall(parsed["content"])

f = open("inClassExample.txt", "w")
f.write("adID: " + adID[0] + "\n")
f.write("Location: " + location[0][0] + "\n")
f.write("Interest Areas: " + interest[0] + "\n")
f.write("Excluded Targets: " + excluded[0] + "\n")
f.write("Age Targeted: " + age[0] + "\n")
f.write("Language of Ad: " + language[0] + "\n")
f.write("Placement of Ad: " + placement[0] + "\n")
f.write("URL: " + URL[0] + "\n")
f.write("Time Post: " + time[0] + "\n")
f.close()

f = open(adID[0] + "metaData.txt", "w")
for x in parsed["metadata"]:
  f.write(x)
f.write("\n")
f.close()




