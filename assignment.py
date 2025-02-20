import sqlite3
import re
ids = []
connection = sqlite3.connect('dbase.db')
cursor = connection.cursor()

#1 table structure
print("1.")
cursor.execute('pragma table_info(npc);')
result = cursor.fetchall()
for i in result:
    print(i)

#2
print("\n2.")
cursor.execute('select id from npc;')
a = str(cursor.fetchall()[-1])
a = re.sub('[(),]', '', a)
print(a)

#3
print("\n3.")
cursor.execute("select class from npc where class='Knight'")
print(len(cursor.fetchall()))

#4
print("\n4.")
cursor.execute("select class from npc")
b = cursor.fetchall()
b.sort()
for i in b:
    i = str(i)
    
Class = ["('Warrior',)","('Ranger',)","('Knight',)","('Sorcerer',)","('Sage',)","('Priest',)","('Thief',)","('Bard',)","('Barbarian',)","('Monk',)","('Assassin',)","('Jester',)","('Samurai',)"]

