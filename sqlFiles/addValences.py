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
        selected = [0] * 83
        for col in range(2, 74, 3):
          if(row[col] != ''):
            #selected[col-1] = row[col]
            statement = "INSERT INTO " + BinaryFlagTableNames[((col+1)/3) - 1] + "(EntryNumber, Category, Valence) VALUES (" + str(row[0]) + ", " +  str(row[col+ 1 ]) + ", " + str(row[col+2]) + ");"
            try:
              cursor.execute(statement)
            except:
              print("MISSING DATA " + statement)
              continue
            '''#statement = "INSERT INTO BinaryAll (EntryNumber BlackCulture,
             BCVal, BlueLives, BLVal, Christian, ChristianVal, Clinton,
             ClintonVal, LatinX, LatinXVal, Immigration, ImmigrationVal,
             Constitution, ConstitutionVal, WhiteSupremacy, WSVal, LGBTQ,
             LGBTQVal, LiberalFeminism, LFVal, Media, MediaVal, Muslim,
             MuslimVal, NativeAmerican, NAVal, Patriot, PatriotVal, RedPill,
             RPVal, Refugees, RefugeesVal, Sanders, SandersVal,
             SecondAmendment, SAVal, Seperatist, SeperatistVal,
             SouthernCulture,SCVal, Syria, SyriaVal, Texas, TexasVal, Trump,
             TrumpVal, Veterans, VeteransVal, otherCandidates, OCVal,
             voterFraud, VFVal, voterMisdirection, VMVal,
             voterTurnoutSuppression, VTSVal INTEGER) VALUES (" + str(row[0])
             +  ", " + str(row[3]) +   ", " + str(row[4]) +  ", " +
             str(row[6]) +  ", " + str(row[7]) +  ", " + str(row[9]) +  ", " +
             str(row[10]) +  ", " + str(row[12]) +  ", " + str(row[13]) +  ",
             " + str(row[15]) +  ", " + str(row[16]) +  ", " + str(row[18]) +
             ", " + str(row[19]) +  ", " + str(row[21]) +  ", " + str(row[22])
             + ", " + str(row[24]) + ", " + str(row[25]) + ", " + str(row[27])
             + ", " + str(row[28]) + ", " + str(row[30]) + ", " + str(row[31])
             + ", " + str(row[33]) + ", " + str(row[34]) + ", " + str(row[36])
             + ", " + str(row[37]) + ", " + str(row[39]) + ", " + str(row[40])
             + ", " + str(row[42]) + "," + str(row[42]) + ");"
        #cursor.execute(statement)
        '''
    connection.commit()
    connection.close()
if __name__ == '__main__':
    main()
