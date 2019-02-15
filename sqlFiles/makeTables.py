#!/usr/bin/env/python
import sys
import sqlite3
import os

MainCreateStatement = """
CREATE TABLE IF NOT EXISTS MainTable (
EntryNumber INTEGER PRIMARY KEY UNIQUE,
AdID INTEGER,
JSON_name VARCHAR(100),
FileName VARCHAR(100),
StartDate VARCHAR(100),
EndDate VARCHAR(100),
Impressions INTEGER,
Clicks INTEGER,
Spent VARCHAR(100),
AdText VARCHAR(100),
ImageText VARCHAR(100),
HashTags VARCHAR(100),
AdLandingPage VARCHAR(100),
CustomIncludes VARCHAR(100),
Junk VARCHAR(100),
AT_Placements VARCHAR(100),
AT_Age VARCHAR(100),
AT_Location VARCHAR(100),
AT_Language VARCHAR(100),
AT_Loose VARCHAR(100),
AT_Gender VARCHAR(100),
AT_PM_All VARCHAR(100),
AT_PM_Behaviors VARCHAR(100),
AT_PM_FieldOfStudy VARCHAR(100),
AT_PM_Politics VARCHAR(100),
AT_PM_Interests VARCHAR(100),
AT_PM_FriendsOfConnections VARCHAR(100),
AT_PM_MulticulturalAffinity VARCHAR(100),
AT_PM_PeopleWhoLike VARCHAR(100),
AT_PM_Industry VARCHAR(100),
AT_PM_Employers VARCHAR(100),
AT_AM_All VARCHAR(100),
AT_AM_Interests VARCHAR(100),
AT_AM_Politics VARCHAR(100),
AT_AM_Behaviors VARCHAR(100),
AT_AM_MulticulturalAffinity VARCHAR(100),
AT_AM_Industry VARCHAR(100),
AT_AM_Employers VARCHAR(100),
AT_EC_All VARCHAR(100),
AT_EC_ExcludePeopleWhoLike VARCHAR(100),
AT_EC_ExcludePeopleWhoAreGoingTo VARCHAR(100),
AT_EX_All VARCHAR(100),
AT_EX_MulticulturalAffinity VARCHAR(100),
AT_EX_Behaviors VARCHAR(100),
avgWordLength INTEGER);"""

PhotoCollectionCreateStatement = '''
CREATE TABLE IF NOT EXISTS PhotoCollection (EntryNumber INTEGER PRIMARY KEY, photo BLOB, FOREIGN KEY(EntryNumber) REFERENCES MainTable(EntryNumber));'''

BinaryFlagCreateStatements = [
'CREATE TABLE IF NOT EXISTS BlackCulture (EntryNumber INTEGER PRIMARY KEY, Valence INTEGER NULL, FOREIGN KEY(EntryNumber) REFERENCES MainTable(EntryNumber));',
'CREATE TABLE IF NOT EXISTS BlueLives (EntryNumber INTEGER PRIMARY KEY, Valence INTEGER NULL, FOREIGN KEY(EntryNumber) REFERENCES MainTable(EntryNumber));',
'CREATE TABLE IF NOT EXISTS Refugees (EntryNumber INTEGER PRIMARY KEY, Valence INTEGER NULL, FOREIGN KEY(EntryNumber) REFERENCES MainTable(EntryNumber));',
'CREATE TABLE IF NOT EXISTS Texas (EntryNumber INTEGER PRIMARY KEY,Valence INTEGER NULL, FOREIGN KEY(EntryNumber) REFERENCES MainTable(EntryNumber));',
'CREATE TABLE IF NOT EXISTS SouthernCulture (EntryNumber INTEGER PRIMARY KEY, Valence INTEGER NULL, FOREIGN KEY(EntryNumber) REFERENCES MainTable(EntryNumber));',
'CREATE TABLE IF NOT EXISTS Seperatist (EntryNumber INTEGER PRIMARY KEY, Valence INTEGER NULL, FOREIGN KEY(EntryNumber) REFERENCES MainTable(EntryNumber));',
'CREATE TABLE IF NOT EXISTS Muslim (EntryNumber INTEGER PRIMARY KEY,  Valence INTEGER NULL, FOREIGN KEY(EntryNumber) REFERENCES MainTable(EntryNumber));',
'CREATE TABLE IF NOT EXISTS Christian (EntryNumber INTEGER PRIMARY KEY, Valence INTEGER NULL, FOREIGN KEY(EntryNumber) REFERENCES MainTable(EntryNumber));',
'CREATE TABLE IF NOT EXISTS LGBTQ (EntryNumber INTEGER PRIMARY KEY, Valence INTEGER NULL, FOREIGN KEY(EntryNumber) REFERENCES MainTable(EntryNumber));',
'CREATE TABLE IF NOT EXISTS NativeAmerican (EntryNumber INTEGER PRIMARY KEY, Valence INTEGER NULL, FOREIGN KEY(EntryNumber) REFERENCES MainTable(EntryNumber));',
'CREATE TABLE IF NOT EXISTS RedPill (EntryNumber INTEGER PRIMARY KEY, Valence INTEGER NULL, FOREIGN KEY(EntryNumber) REFERENCES MainTable(EntryNumber));',
'CREATE TABLE IF NOT EXISTS Patriot (EntryNumber INTEGER PRIMARY KEY, Valence INTEGER NULL, FOREIGN KEY(EntryNumber) REFERENCES MainTable(EntryNumber));',
'CREATE TABLE IF NOT EXISTS LiberalFeminism (EntryNumber INTEGER PRIMARY KEY, Valence INTEGER NULL, FOREIGN KEY(EntryNumber) REFERENCES MainTable(EntryNumber));',
'CREATE TABLE IF NOT EXISTS Veterans (EntryNumber INTEGER PRIMARY KEY, Valence INTEGER NULL, FOREIGN KEY(EntryNumber) REFERENCES MainTable(EntryNumber));',
'CREATE TABLE IF NOT EXISTS SecondAmendment (EntryNumber INTEGER PRIMARY KEY, Valence INTEGER NULL, FOREIGN KEY(EntryNumber) REFERENCES MainTable(EntryNumber));',
'CREATE TABLE IF NOT EXISTS Syria (EntryNumber INTEGER PRIMARY KEY, Valence INTEGER NULL, FOREIGN KEY(EntryNumber) REFERENCES MainTable(EntryNumber));',
'CREATE TABLE IF NOT EXISTS Media (EntryNumber INTEGER PRIMARY KEY, Valence INTEGER NULL, FOREIGN KEY(EntryNumber) REFERENCES MainTable(EntryNumber));',
'CREATE TABLE IF NOT EXISTS NewsAndEvents (EntryNumber INTEGER PRIMARY KEY, Valence INTEGER NULL, FOREIGN KEY(EntryNumber) REFERENCES MainTable(EntryNumber));',
'CREATE TABLE IF NOT EXISTS Trump (EntryNumber INTEGER PRIMARY KEY, Valence INTEGER NULL, FOREIGN KEY(EntryNumber) REFERENCES MainTable(EntryNumber));',
'CREATE TABLE IF NOT EXISTS Clinton (EntryNumber INTEGER PRIMARY KEY, Valence INTEGER NULL, FOREIGN KEY(EntryNumber) REFERENCES MainTable(EntryNumber));',
'CREATE TABLE IF NOT EXISTS Sanders (EntryNumber INTEGER PRIMARY KEY, Valence INTEGER NULL, FOREIGN KEY(EntryNumber) REFERENCES MainTable(EntryNumber));',
'CREATE TABLE IF NOT EXISTS otherCandidates (EntryNumber INTEGER PRIMARY KEY, Valence INTEGER NULL, FOREIGN KEY(EntryNumber) REFERENCES MainTable(EntryNumber));',
'CREATE TABLE IF NOT EXISTS voterFraud (EntryNumber INTEGER PRIMARY KEY, Valence INTEGER NULL, FOREIGN KEY(EntryNumber) REFERENCES MainTable(EntryNumber));',
'CREATE TABLE IF NOT EXISTS voterMisdirection (EntryNumber INTEGER PRIMARY KEY, Valence INTEGER NULL, FOREIGN KEY(EntryNumber) REFERENCES MainTable(EntryNumber));',
'CREATE TABLE IF NOT EXISTS voterTurnoutSuppression (EntryNumber INTEGER PRIMARY KEY, Valence INTEGER NULL);']


def main():
      connection = sqlite3.connect("ReddFlag.db")
      cursor = connection.cursor()
      cursor.execute(MainCreateStatement)
      cursor.execute(PhotoCollectionCreateStatement)
      for x in BinaryFlagCreateStatements:
          cursor.execute(x)

if __name__ == '__main__':
    main()
