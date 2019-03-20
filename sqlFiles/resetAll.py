#!/usr/bin/env/python
import sys
import sqlite3
import os
import deleteMain
import deletePhotoTable
import deleteBinaryTables
import populateMain
import populateBinary
import makeTables
import addValences

def main():
    deleteMain.main()
    deleteBinaryTables.main()
    makeTables.main()
    populateMain.main()
    #populateBinary.main()
    addValences.main()
if __name__ == '__main__':
    main()
