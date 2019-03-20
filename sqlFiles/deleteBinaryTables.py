#!/usr/bin/env/python
import sys
import sqlite3
import os


BinaryFlagTableNames = ["BlackCulture", "BlueLives", "Christian", "Clinton", "LatinX", "Immigration", "Constitution", "WhiteSupremacy", "LGBTQ", "LiberalFeminism", "Media", "Muslim", "NativeAmerican", "Patriot", "RedPill","Refugees", "Sanders", "SecondAmendment", "Seperatist", "SouthernCulture", "Syria", "Texas", "Trump", "Veterans", "otherCandidates", "voterFraud", "voterMisdirection", "voterTurnoutSuppression"]

def main():
      connection = sqlite3.connect("ReddFlag.db")
      cursor = connection.cursor()
      statement = "DROP TABLE IF EXISTS BinaryAll;"
      cursor.execute(statement)
      for x in BinaryFlagTableNames:
        statement = "DROP TABLE IF EXISTS " + x + ";"
        cursor.execute(statement)

if __name__ == '__main__':
    main()
