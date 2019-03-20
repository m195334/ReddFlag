#!/usr/bin/env/python
import sys
import sqlite3
import os



def main():
    connection = sqlite3.connect("../ReddFlag.db")
    cursor = connection.cursor()

    statement = '''SELECT MainTable.EntryNumber, MainTable.AdText, MainTable.FileName
    FROM MainTable
    INNER JOIN BlackCulture ON MainTable.EntryNumber = BlackCulture.EntryNumber;'''

    cursor.execute(statement)
    rows=cursor.fetchall()

    for row in rows:
      print(row[0], row[1], row[2])

      
    connection.commit()
    connection.close()

if __name__ == '__main__':
    main()
