# VioletPang_Project3_SQL
# Project Title

VioletPang_Project3_SQL


## Description

This is project3 for IDS706 Data Engineering and Dataops at Duke University 2022 fall. In this project, a script with 5 queries is built and connect to sqlit3 database by using sqlite3 library. Pandas library is also used in order to transform csv file in to the table in the database. 

Steam Store Games dataset created by NIK DAVIS from Kaggle.com is used in this project. Acoording to NIK's notes, this dataset gathered around May 2019, and contains most games on the steam game store released prior to that date. 

In order to have some explorations about this dataset, 5 questions will be answered by using sqlite queries in connect.py: 

* Question 1 - Who are the top 3 developers who developed most games in steam store? 
* Question 2 - What are the top 10 games that have most positive ratings?
* Question 3 - What are the top 10 games that has most negative ratings? 
* Question 4 - What are the 10 most expensive games in steam store?
* Question 5 - What are the top 10 games that have longest median playing time?

## Structure
![sqlite3](https://user-images.githubusercontent.com/65413798/199886073-489d53c2-f9cb-4622-a730-0709f1ebc840.png)
Source: [Python SQLite tutorial using sqlite3](https://pynative.com/python-sqlite/)


## Getting Started

### Dependencies

* This project is built in github codespaces 
* Please install Python on your computer or build virtual environment for Python to run this project. 

### Installing

* Simply clone this repository and run connect.py. You will be able to connect to sqlite3 databse and run the queries. 

### Executing program

* Step 1
* Enable line 10 - line 14 in connect.py in order to build a connection with sqlite3 databse and create a new table
```
table = 'CREATE TABLE steam_info (appid INTEGER PRIMARY KEY, name TEXT, release_date TEXT, english INTEGER, developer TEXT, publisher TEXT, platforms TEXT, required_age INTEGER, categories TEXT, genres TEXT, steamspy_tags TEXT, achievements INTEGER, positive_ratings INTEGER, negative_ratings INTEGER, average_playtime INTEGER, median_playtime INTEGER, owners INTEGER, price INTEGER)'
cursor = conn.cursor()
cursor.execute(table)
conn.commit()
print('Table created successfully')
```
* Step 2
* Run connect.py by using python connect.py command in the terminal or choose run in your menu

* Step 3
* If you want to run connect.py after creating the table, please comment line 10 -line 14 in connect.py in order to avoid duplication and error. 


## Help

Please don't forget to comment line 10 - line 14 in connect.py in order to avoid duplication and error after 1st time run.
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

## Acknowledgments
* [Steam Store Games (Clean dataset) at Kaggle](https://www.kaggle.com/datasets/nikdavis/steam-store-games?select=steam.csv)
* [Python SQLite tutorial using sqlite3](https://pynative.com/python-sqlite/)

