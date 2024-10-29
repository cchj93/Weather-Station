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
 
 id INTEGER PRIMARY KEY,
 username TEXT NOT NULL,
 EMAIL TEXT NOT NULL,
 password TEXT NOT NULL,
 role integer NOT NULL default 1,
 status BOOLEAN DEFAULT TRUE,
 created_ at TIMESTAP DEFAULT (datetime('now','localtime')),
 update_at TIMESTAP DEFAULT (datetime('now','localtime')),
 deleted_at NULL
 )
 '''


 #execute query


sensors_model = '''
 create table if not exists sensors(
 
 id INTEGER PRIMARY KEY,
 name TEXT NOT NULL,
 model TEXT NOT NULL,
 descripstion TEXT NOT NULL,
 url_datasheet TEXT NULL,
 url_image TEXT NULL,
 status BOOLEAN DEFAULT TRUE,
 created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
 update_at TIMESTAMP DEFAULT (datetime('now','localtime')),
 delete_at null
 )

 '''

#close conenction
cur.execute(users_model)
cur.execute(sensors_model)
#con.close()