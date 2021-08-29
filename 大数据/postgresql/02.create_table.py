import os
import sys
import psycopg2

def connectPostgreSQL():
    conn = psycopg2.connect(database="komablog", user="postgres", password="psqlsai@345", host="1.116.68.249", port="5432")
    print('connect successful!')
    cursor=conn.cursor()
    cursor.execute('''
        create table public.member(
            id integer not null primary key,
            name varchar(32) not null,
            password varchar(32) not null,
            singal varchar(128)
        )
    ''')
    conn.commit()
    conn.close()
    print('table public.member is created!')

if __name__=='__main__':
    connectPostgreSQL()