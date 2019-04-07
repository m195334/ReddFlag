#!/usr/bin/env/pythON
import sys
import sqlite3
import os


ViewDelete = '''
DROP VIEW IF EXISTS AllDataWithBinary;'''

ViewDelete2 = '''
DROP VIEW IF EXISTS AllDataLeftJoin;'''

ViewCreate = '''
CREATE VIEW AllDataWithBinary
AS
SELECT * 
FROM MainTable
JOIN BinaryAll ON BinaryAll.EntryNumber = MainTable.EntryNumber
;'''

ViewCreate2 = '''
CREATE VIEW AllDataLeftJoin
AS
SELECT *
FROM MainTable
LEFT OUTER JOIN BinaryAll ON MainTable.EntryNumber = BinaryAll.EntryNumber
;'''


def main():
      connection = sqlite3.connect("ReddFlag.db")
      cursor = connection.cursor()
      cursor.execute(ViewDelete)
      cursor.execute(ViewCreate)
      cursor.execute(ViewDelete2)
      cursor.execute(ViewCreate2)

if __name__ == '__main__':
    main()
