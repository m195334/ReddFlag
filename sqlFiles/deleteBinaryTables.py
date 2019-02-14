#!/usr/bin/env/python
import sys
import sqlite3
import os


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

def main():
      connection = sqlite3.connect("ReddFlag.db")
      cursor = connection.cursor()
      for x in BinaryFlagTableNames:
        statement = "DROP TABLE IF EXISTS " + x + ";"
        cursor.execute(statement)

if __name__ == '__main__':
    main()
