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
        for x in range(0, len(row)):
          if(row[x] == '' or row[x] == ' '):
            row[x] = 0
        for col in range(2, 74, 3):
          if(row[col] != 0):
            statement = "INSERT INTO " + BinaryFlagTableNames[((col+1)/3) - 1] + "(EntryNumber, Category, Valence) VALUES (" + str(row[0]) + ", " +  str(row[col+ 1 ]) + ", " + str(row[col+2]) + ");"
            try:
              cursor.execute(statement)
            except:
              #print("wrong")
              continue
        try:
          statement = "INSERT INTO BinaryAll (EntryNumber, BlackCulture, BCVal, BlueLives, BLVal, Christian, ChristianVal, Clinton, ClintonVal, LatinX, LatinXVal, Immigration, ImmigrationVal, Constitution, ConstitutionVal, WhiteSupremacy, WSVal, LGBTQ, LGBTQVal, LiberalFeminism, LFVal, Media, MediaVal, Muslim, MuslimVal, NativeAmerican, NAVal, Patriot, PatriotVal, RedPill, RPVal, Refugees, RefugeesVal, Sanders, SandersVal, SecondAmendment, SAVal, Seperatist, SeperatistVal, SouthernCulture,SCVal, Syria, SyriaVal, Texas, TexasVal, Trump, TrumpVal, Veterans, VeteransVal, otherCandidates, OCVal, voterFraud, VFVal, voterMisdirection, VMVal, voterTurnoutSuppression, VTSVal) VALUES (" + str(row[0]) +  ", " + str(row[3]) +   ", " + str(row[4]) +  ", " + str(row[6]) +  ", " + str(row[7]) +  ", " + str(row[9]) +  ", " + str(row[10]) +  ", " + str(row[12]) +  ", " + str(row[13]) +  ", " + str(row[15]) + ", " + str(row[16]) +  ", " + str(row[18]) + ", " + str(row[19]) + ", " + str(row[21]) +  ", " + str(row[22]) + ", " + str(row[24]) + ", " + str(row[25]) + ", " + str(row[27]) + ", " + str(row[28]) + ", " + str(row[30]) + ", " + str(row[31]) + ", " + str(row[33]) + ", " + str(row[34]) + ", " + str(row[36]) + ", " + str(row[37]) + ", " + str(row[39]) + ", " + str(row[40]) + ", " + str(row[42]) + ", " + str(row[43]) + ", " + str(row[45]) + ", " + str(row[46]) + ", " + str(row[48]) + "," + str(row[49]) + ", " +  str(row[51]) + ", " + str(row[52]) + ", " + str(row[54]) + ", " + str(row[55]) + ", " + str(row[57]) + ", " + str(row[58]) + ", " +  str(row[60]) + ", " + str(row[61]) + ", " + str(row[63]) + ", " + str(row[64]) + ", " + str(row[66]) + ", " + str(row[67]) + ", " + str(row[69]) + ", " + str(row[70]) + ", " + str(row[72]) + ", " + str(row[73]) + ", " + str(row[75]) + ", " + str(row[76]) +", " + str(row[78]) + ", " + str(row[79]) + ", " + str(row[81]) + ", " + str(row[82]) + ", " + str(row[84]) + ", " + str(row[85]) + ");"
          cursor.execute(statement)
        except:
          continue
    connection.commit()
    connection.close()
if __name__ == '__main__':
    main()
