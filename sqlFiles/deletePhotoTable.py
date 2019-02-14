#!/usr/bin/env/python
import sys
import sqlite3
import os

def main():
      connection = sqlite3.connect("ReddFlag.db")
      cursor = connection.cursor()
      cursor.execute("DROP TABLE IF EXISTS PhotoCollection;")

if __name__ == '__main__':
    main()
