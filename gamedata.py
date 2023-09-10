
from kivy.app import App

from kivy.uix.floatlayout import FloatLayout

import mysql
from mysql import  *

class username(FloatLayout):
    def __init__(self,**kwargs):
        super(username, self).__init__(**kwargs)
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "msdhoni7777"
        )
        c =  mydb.cursor()
        c.execute("CREATE DATABASE ARGINTINA")
        print("database created")
        c.execute("SHOW DATABASES")
        for db in c:
            print(db)




class okapp(App):
    def build(self):
        return username()

okapp().run()