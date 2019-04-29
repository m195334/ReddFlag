#!/usr/bin/env python
import sys
import re
import sqlite3
import os
import csv

#BinaryFlagTableNames = ["BlackCulture", "BlueLives", "Christian", "Clinton", "LatinX", "Immigration", "Constitution", "WhiteSupremacy", "LGBTQ", "LiberalFeminism", "Media", "Muslim", "NativeAmerican", "Patriot", "RedPill","Refugees", "Sanders", "SecondAmendment", "Seperatist", "SouthernCulture", "Syria", "Texas", "Trump", "Veterans", "otherCandidates", "voterFraud", "voterMisdirection", "voterTurnoutSuppression"]

fileName = "../BinaryAllNew.csv"


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
        #for col in range(1, 57, 3):
          #if(row[col] != '0'):
            #statement = "INSERT INTO " + BinaryFlagTableNames[((col+2)/3) - 1] + "(EntryNumber, Category, Valence) VALUES (" + str(row[0]) + ", " +  str(row[col]) + ", " + str(row[col+1]) + ");"
            #try:
              #cursor.execute(statement)
            #except:
              #print("wrong")
              #continue
        statement = "INSERT INTO BinaryAll (EntryNumber, BlackCulture, BCVal, BlueLives, BLVal, Christian, ChristianVal, Clinton, ClintonVal, LatinX, LatinXVal, Immigration, ImmigrationVal, Constitution, ConstitutionVal, WhiteSupremacy, WSVal, LGBTQ, LGBTQVal, LiberalFeminism, LFVal, Media, MediaVal, Muslim, MuslimVal, NativeAmerican, NAVal, Patriot, PatriotVal, RedPill, RPVal, Refugees, RefugeesVal, Sanders, SandersVal, SecondAmendment, SAVal, Seperatist, SeperatistVal, SouthernCulture,SCVal, Syria, SyriaVal, Texas, TexasVal, Trump, TrumpVal, Veterans, VeteransVal, otherCandidates, OCVal, voterFraud, VFVal, voterMisdirection, VMVal, voterTurnoutSuppression, VTSVal, NoCategory) VALUES (" + str(row[0]) + ", " + str(row[1]) + ", " + str(row[2]) + ", " + str(row[3]) + ", " + str(row[4]) + ", " + str(row[5]) + ", " + str(row[6]) + ", " + str(row[7]) + ", " + str(row[8]) + ", " + str(row[9]) + ", " + str(row[10]) + ", " + str(row[11]) + ", " + str(row[12]) + ", " + str(row[13]) + ", " + str(row[14]) + ", " + str(row[15]) + ", " +str(row[16]) + ", " + str(row[17]) + ", " + str(row[18]) + ", " + str(row[19]) + ", " + str(row[20]) + ", " + str(row[21]) + ", " + str(row[22]) + ", " + str(row[23]) + ", " + str(row[24]) + ", " + str(row[25]) + ", " + str(row[26]) + ", " + str(row[27]) + ", " + str(row[28]) + ", " + str(row[29]) + ", " + str(row[30]) + ", " + str(row[31]) + ", " + str(row[32]) + ", " + str(row[33]) + ", " + str(row[34]) + ", " + str(row[35]) + ", " + str(row[36]) + ", " + str(row[37]) + ", " + str(row[38]) + ", " + str(row[39]) + ", " + str(row[40]) + ", " + str(row[41]) + ", " + str(row[42]) + ", " + str(row[43]) + ", " + str(row[44]) + ", " + str(row[45]) + ", " + str(row[46]) + ", " + str(row[47]) + ", " + str(row[48]) + ", " + str(row[49]) + ", " + str(row[50]) + ", " + str(row[51]) + ", " + str(row[52]) + ", " + str(row[53]) + ", " + str(row[54]) + ", " + str(row[55]) + ", " + str(row[56]) + ", " + str(row[57]) + ");"
        cursor.execute(statement)
    connection.commit()
    connection.close()
if __name__ == '__main__':
    main()
