import sqlite3
import pandas as pd


conn = sqlite3.connect('SQLite_Python.db')
cursor = conn.cursor()
print("Database created and Successfully Connected to SQLite")

## create new table for steam.csv
table = 'CREATE TABLE steam_info (appid INTEGER PRIMARY KEY, name TEXT, release_date TEXT, english INTEGER, developer TEXT, publisher TEXT, platforms TEXT, required_age INTEGER, categories TEXT, genres TEXT, steamspy_tags INTEGER, achievements INTEGER, positive_ratings INTEGER, negative_ratings INTEGER, average_playtime TEXT, median_playtime INTEGER, owners INTEGER, price INTEGER)'
cursor = conn.cursor()
cursor.execute(table)
conn.commit()
print('Table created successfully')

# load the data into a Pandas DataFrame
steam = pd.read_csv('steam.csv')
# write the data to a sqlite table
steam.to_sql('steam_info', conn, if_exists='append', index = False)

# fetch all rows from steam table
cursor.execute('''SELECT * FROM steam_info''').fetchall()

# Select first 5 record from the table
query_select = 'SELECT * FROM steam_info LIMIT 5'
for i in cursor.execute(query_select):
    print(i)
