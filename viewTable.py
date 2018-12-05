import sqlite3

connection = sqlite3.connect("committeeInfo.db")

cursor = connection.cursor()
cursor.execute("SELECT * FROM CommitteeInfo")
print("fetchall:")
result = cursor.fetchall()
#result = cursor.fetchone()
for r in result:
  print(r)

