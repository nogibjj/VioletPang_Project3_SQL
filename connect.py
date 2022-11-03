import sqlite3
import pandas as pd


conn = sqlite3.connect('SQLite_Python.db')
cursor = conn.cursor()
print("Database created and Successfully Connected to SQLite")

## create new table for steam.csv
# table = 'CREATE TABLE steam_info (appid INTEGER PRIMARY KEY, name TEXT, release_date TEXT, english INTEGER, developer TEXT, publisher TEXT, platforms TEXT, required_age INTEGER, categories TEXT, genres TEXT, steamspy_tags TEXT, achievements INTEGER, positive_ratings INTEGER, negative_ratings INTEGER, average_playtime INTEGER, median_playtime INTEGER, owners INTEGER, price INTEGER)'
# cursor = conn.cursor()
# cursor.execute(table)
# conn.commit()
# print('Table created successfully')

# load the data into a Pandas DataFrame
steam = pd.read_csv('steam.csv')
# write the data to a sqlite table
# steam.to_sql('steam_info', conn, if_exists='append', index = False)

# fetch all rows from steam table
cursor.execute('''SELECT * FROM steam_info''').fetchall()

# Select first 5 record from the table
query_select = 'SELECT * FROM steam_info LIMIT 5'
for i in cursor.execute(query_select):
    print(i)

#### query 1 : select top 3 developers who developed most games
query1 =  """SELECT Distinct developer, count(appid) 
		   FROM steam_info
		   WHERE developer != ''
		   Group by developer
		   Order by count(appid) DESC
		   LIMIT 3;"""
developer_with_most_games = cursor.execute(query1).fetchall()

# show result
print('*'* 70)
print("Top 3 developers who developed most games:")
for dev in developer_with_most_games:
    print(dev)

#### query 2 : select top 10 games that has most positive ratings 
query2 =  """SELECT name, positive_ratings 
		   FROM steam_info
		   WHERE name != ''
		   Group by name
		   Order by positive_ratings DESC
		   LIMIT 10;"""
most_pos_rating_games = cursor.execute(query2).fetchall()

# show result
print('*'* 70)
print("Top 10 games that has most positive ratings:")
for i in most_pos_rating_games:
    print(i)

#### query 3 : select top 10 games that has most negative ratings 
query3 =  """SELECT name, negative_ratings 
		   FROM steam_info
		   WHERE name != ''
		   Group by name
		   Order by negative_ratings DESC
		   LIMIT 10;"""
most_neg_rating_games = cursor.execute(query3).fetchall()

# show result
print('*'* 70)
print("Top 10 games that has most negative ratings:")
for n in most_neg_rating_games:
    print(n)

#### query 4 : select 10 most expensive games in steam store 
query4 =  """SELECT name, developer, price 
		   FROM steam_info
		   WHERE name != ''
		   Group by name
		   Order by price DESC
		   LIMIT 10;"""
most_expensive_games = cursor.execute(query4).fetchall()

# show result
print('*'* 70)
print("10 most expensive games in steam store:")
for i in most_expensive_games:
    print(i)

#### query 5 : select Top 10 games that have longest median playing time
query5 =  """SELECT name, developer, median_playtime 
		   FROM steam_info
		   WHERE name != ''
		   Group by name
		   Order by median_playtime DESC
		   LIMIT 10;"""
longest_median_playtime_games = cursor.execute(query5).fetchall()

# show result
print('*'* 70)
print("Top 10 games that have longest median playing time:")
for i in longest_median_playtime_games:
    print(i)


