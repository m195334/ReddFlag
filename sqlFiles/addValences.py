#!/usr/bin/env python
import sys
import re
import sqlite3
import os
import csv

BinaryFlagTableNames = ["BlackCulture", "BlueLives", "Christian", "Clinton", "LatinX", "Immigration", "Constitution", "WhiteSupremacy", "LGBTQ", "LiberalFeminism", "Media", "Muslim", "NativeAmerican", "Patriot", "RedPill","Refugees", "Sanders", "SecondAmendment", "Seperatist", "SouthernCulture", "Syria", "Texas", "Trump", "Veterans", "otherCandidates", "voterFraud", "voterMisdirection", "voterTurnoutSuppression"]

fileName = "../AdMatrix.csv"


def main():

    connection = sqlite3.connect("ReddFlag.db")
    cursor = connection.cursor()

    with open(fileName) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter = ",")
      next(csv_reader)
      for row in csv_reader:
        selected = [0] * 28
        for col in range(1, 28):
          if(row[col] != ''):
            selected[col-1] = row[col]
            statement = "INSERT INTO " + BinaryFlagTableNames[col - 1] + " (EntryNumber, Valence) VALUES (" + str(row[0]) + ", " + str(row[col]) + ");"
            cursor.execute(statement)
        
        statement = "INSERT INTO BinaryAll (EntryNumber, BlackCulture, BlueLives, Christian, Clinton, LatinX, Immigration, Constitution, WhiteSupremacy, LGBTQ, LiberalFeminism, Media, Muslim, NativeAmerican, Patriot, RedPill, Refugees, Sanders, SecondAmendment, Seperatist, SouthernCulture, Syria, Texas, Trump, Veterans, otherCandidates, voterFraud, voterMisdirection, voterTurnoutSuppression) VALUES (" + str(row[0]) +  ", " + str(selected[0]) +   ", " + str(selected[1]) +  ", " + str(selected[2]) +  ", " + str(selected[3]) +  ", " + str(selected[4]) +  ", " + str(selected[5]) +  ", " + str(selected[6]) +  ", " + str(selected[7]) +  ", " + str(selected[8]) +  ", " + str(selected[9]) +  ", " + str(selected[10]) +  ", " + str(selected[11]) +  ", " + str(selected[12]) +  ", " + str(selected[13]) + ", " + str(selected[14]) + ", " + str(selected[15]) + ", " + str(selected[16]) + ", " + str(selected[17]) + ", " + str(selected[18]) + ", " + str(selected[19]) + ", " + str(selected[20]) + ", " + str(selected[21]) + ", " + str(selected[22]) + ", " + str(selected[23]) + ", " + str(selected[24]) + ", " + str(selected[25]) + ", " + str(selected[26]) + "," + str(selected[27]) + ");"
        
        cursor.execute(statement)
    connection.commit()
    connection.close()

if __name__ == '__main__':
    main()
