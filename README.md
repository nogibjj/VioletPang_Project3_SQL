# VioletPang_Project3_SQL
# Project Title

VioletPang_Project3_SQL


## Description

This is project3 for IDS706 Data Engineering and Dataops at Duke University 2022 fall. 

## Getting Started

### Dependencies

* This project is buiilt in github codespaces 
* Please install Python on your computer or build virtual environment for Python to run this project. 

### Installing

* Simply clone this repository and run connect.py. You will be able to connect to sqlite3 databse and run the queries. 

### Executing program

* Step 1
* Enable line 10 - line 14 in connect.py in order to build a connection with sqlite3 databse and create a newe table
```
table = 'CREATE TABLE steam_info (appid INTEGER PRIMARY KEY, name TEXT, release_date TEXT, english INTEGER, developer TEXT, publisher TEXT, platforms TEXT, required_age INTEGER, categories TEXT, genres TEXT, steamspy_tags TEXT, achievements INTEGER, positive_ratings INTEGER, negative_ratings INTEGER, average_playtime INTEGER, median_playtime INTEGER, owners INTEGER, price INTEGER)'
cursor = conn.cursor()
cursor.execute(table)
conn.commit()
print('Table created successfully')
```
* Step 2
* Run connect.py by unsing the command in the terminal or choose run in your menu

* Step 3
* If you want to run connect.py after creating the table, please comment line 10 -line 14 in connect.py in order to duplication and error. 


## Help

Please don't forget to comment line 10 -line 14 in connect.py in order to duplication and error after 1st time run.
```
# table = 'CREATE TABLE steam_info (appid INTEGER PRIMARY KEY, name TEXT, release_date TEXT, english INTEGER, developer TEXT, publisher TEXT, platforms TEXT, required_age INTEGER, categories TEXT, genres TEXT, steamspy_tags TEXT, achievements INTEGER, positive_ratings INTEGER, negative_ratings INTEGER, average_playtime INTEGER, median_playtime INTEGER, owners INTEGER, price INTEGER)'
# cursor = conn.cursor()
# cursor.execute(table)
# conn.commit()
# print('Table created successfully')
```

## Authors

Violet Pang 
[@Ultraviolet0909]

## Version History

* 0.2
    * Update connect.py with more queries

* 0.1
    * Initial Release

