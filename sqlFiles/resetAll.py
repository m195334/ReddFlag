#!/usr/bin/env/python
import sys
import sqlite3
import os
import deletePhotoTable
import deleteBinaryTables
import addValences
import makeView
import populateMainFromUpdated
import makeTablesUpdatedMain
import deleteMain
def main():
    deleteMain.main()
    deleteBinaryTables.main()
    makeTablesUpdatedMain.main()
    populateMainFromUpdated.main()
    addValences.main()
    makeView.main()
if __name__ == '__main__':
    main()
