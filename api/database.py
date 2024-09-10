'''

Dev: cristian hurtado
Script description: weather_station Database
Engine: SQLITE
DATE: 09/09/2024
'''

#Import  database engine packege
import sqlite3

#create weather_station database
con = sqlite3.connect('weather_station.db')

#create cursor
cur = con.cursor()

# user model
users_model = '''
 create table if not exists users(
 
 id INTERGER PRIMARY KEY,
 username TEXT NOT NULL,
 EMAIL TEXT NOT NULL,
 password TEXT NOT NULL,
 role TEXT NOT NULL,
 status BOOLEAN DEFAULT TRUE,
 created_ at TIMESTAP DEFAULT (datetime('now','localtime')),
 update_at TIMESTAP DEFAULT (datetime('now','localtime')),
 deleted_at NULL
 )

 '''

 #execute query
cur.execute(users_model)

#close conenction

con.close()