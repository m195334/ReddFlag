#!/usr/bin/env/pythON
import sys
import sqlite3
import os


ViewDelete = '''
DROP VIEW IF EXISTS AllData;'''

ViewCreate = '''
CREATE VIEW AllData
AS
SELECT * 
FROM MainTable
JOIN BinaryAll ON BinaryAll.EntryNumber = MainTable.EntryNumber
;'''


def main():
      connection = sqlite3.connect("ReddFlag.db")
      cursor = connection.cursor()
      cursor.execute(ViewDelete)
      cursor.execute(ViewCreate)

if __name__ == '__main__':
    main()
