#!/usr/bin/env python
import sys
import json
import sqlite3
import datetime
import math
import re
import os
import string
from pprint import pprint

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def create_entry(conn, entry):
    """
    Create a new entry
    :param conn:
    :param task:
    :return:
    """

    sql = '''INSERT INTO reddit(
             author,
             author_flair_text,
             body,
             controversiality,
             created_utc,
             distinguished,
             edited,
             gilded,
             id,
             is_submitter,
             link_id,
             parent_id,
             permalink,
             retrieved_on,
             score,
             stickied,
             subreddit,
             subreddit_id)
             VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''

    cur = conn.cursor()
    cur.execute(sql, entry)
    return cur.lastrowid

def main():
    # database = "reddit.db"

    blackCulture ="black|african|pan-african|Black\s*Lives\s*Matter"
    police = "police|law\s*enforcement|cop"
    refugee = "immigrant|invader|refugee|immigration(s?)|wall|caravan"
    texas = "Texas|community"
    southernCulture = "Southern|south|confederate|history"
    seperatist = "seperatist|calexit|texit|secede|secession|movement"
    muslim = "muslim|mosque|arab|islam|allah"
    christian = "church|christian|jesus|baptist|god"
    lgbt = "lgbt|gay|lesbian|queer|pride"
    nativeAm = "native\s*american"
    meme = "meme|red\s*pill"
    patriotism = "patriot|patriotic|nationalism|tea\s*party"
    liberal = "liberal|left|feminism|feminist|women"
    veteran = "veteran|va|vet"
    gunRights = "gun|2nd|amendment|second\s*amendment"
    syria = "syria|isis|pro-assad|assad"
    isis = "isis|isil"
    media = "media|news|newspaper|trustworth"
    trump = "trump|donald|president|apprentice"
    clinton = "clinton|hillary|killary"
    sanders = "sanders|bernie|bern"
    otherCandidates = "stein"
    vote_fraud = "voter\s*fraud|fraudulent|voting|vote|polls|election"
    vote_misdirection = "voter|polling|votes|vote|election"
    vote_suppression = "voter|polling|votes|vote|election"
    hashtag = "#\s*"

    try:
        reddit = open(sys.argv[1])
    except IndexError:
        print("Please enter a file name as an argument in the command line.")
        sys.exit(0)
    except IOError:
        print("File does not appear to exist.")
        sys.exit(0)

    try:
        database = sys.argv[2]
    except IndexError:
        print("No output database filename specified, defaulting to \'reddit.db\'")
        database = "reddit.db"

    conn = create_connection(database)
    with conn:

        # create table
        conn.execute('''CREATE TABLE IF NOT EXISTS reddit(
                        author,
                        author_flair_text,
                        body,
                        controversiality INT,
                        created_utc DATETIME,
                        distinguished,
                        edited DATETIME,
                        gilded INT,
                        id,
                        is_submitter INT,
                        link_id,
                        parent_id,
                        permalink,
                        retrieved_on DATETIME,
                        score INT,
                        stickied INT,
                        subreddit,
                        subreddit_id,
                        hashtag
                        )''')

        for line in reddit:
            # converts json object to dictionary
            result = json.loads(line)

            databaseKeys = ['author',
                            'author_flair_text',
                            'body',
                            'controversiality',
                            'created_utc',
                            'distinguished',
                            'edited',
                            'gilded',
                            'id',
                            'is_submitter',
                            'link_id',
                            'parent_id',
                            'permalink',
                            'retrieved_on',
                            'score',
                            'stickied',
                            'subreddit',
                            'subreddit_id']

            # create null values for non-existent fields
            for key in databaseKeys:
                if key not in list(result.keys()):
                    result[key] = None

            if result['edited'] == None:
                edited = None
            else:
                edited = datetime.timedelta(seconds = result['edited']) + datetime.datetime(1970,1,1)

            # Hastag Finder, does not work well with Reddit posts
            ######################################################################
            flagsFound = []

            def findFlag(finder):
                m = re.search(finder, result['body'], flags = re.VERBOSE|re.IGNORECASE)
                if m and result['controversiality'] == 1:
                    flagsFound.append(True)
                    #print('Found')
                    print()
                    print(finder)
                    print(result['body'])
                else:
                    flagsFound.append(False)

            findFlag(blackCulture)
            findFlag(blackCulture)
            findFlag(police)
            findFlag(refugee)
            findFlag(texas)
            findFlag(southernCulture)
            findFlag(seperatist)
            findFlag(muslim)
            findFlag(christian)
            findFlag(lgbt)
            findFlag(nativeAm)
            findFlag(meme)
            findFlag(patriotism)
            findFlag(liberal)
            findFlag(veteran)
            findFlag(gunRights)
            findFlag(syria)
            findFlag(isis)
            findFlag(media)
            findFlag(trump)
            findFlag(clinton)
            findFlag(sanders)
            findFlag(otherCandidates)
            findFlag(vote_fraud)
            findFlag(vote_misdirection)
            findFlag(vote_suppression)
            ######################################################################

            entry = (result['author'],
                     result['author_flair_text'],
                     result['body'],
                     result['controversiality'],
                     datetime.timedelta(seconds = result['created_utc']) + datetime.datetime(1970,1,1),
                     result['distinguished'],
                     edited,
                     result['gilded'],
                     result['id'],
                     result['is_submitter'],
                     result['link_id'],
                     result['parent_id'],
                     result['permalink'],
                     datetime.timedelta(seconds = result['retrieved_on']) + datetime.datetime(1970,1,1),
                     result['score'],
                     result['stickied'],
                     result['subreddit'],
                     result['subreddit_id'])

            create_entry(conn, entry)

if __name__ == '__main__':
    main()
