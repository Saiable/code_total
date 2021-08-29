import os
import sys
import psycopg2

def connectPostgreSQL():
    conn = psycopg2.connect(database="komablog", user="postgres", password="psqlsai@345", host="1.116.68.249", port="5432")
    print('connect successful!')

if __name__=='__main__':
    connectPostgreSQL()