#!/usr/bin/env python
import sys
import json
import sqlite3
import datetime
import math

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
                        subreddit_id
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

            # checks if entries in reddit file have different keys
            """
            keys = list(result.keys())
            keys.sort()

            if keys not in array:
                array.append(keys)
            """

            # convert 'created_utc' / 'retrieved_on' to datetime
            # print(datetime.timedelta(seconds = result['created_utc']) + datetime.datetime(1970,1,1))

if __name__ == '__main__':
    main()
