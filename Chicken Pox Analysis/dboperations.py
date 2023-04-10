import csv
import os.path
import sqlite3
import json

import mysql.connector

class DBOperations():




    def databaseconnection(self):
        try:
            os.chdir('/Users/mac/PycharmProjects/ML_Test_Projects')

            mydb=mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
            )
            mycursor1=mydb.cursor()

            mycursor1.execute("CREATE DATABASE TestDB_new6")

        except:
            myconnection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='TestDB_new6'
            )

            return myconnection





    def createTable(self):
        connn= self.databaseconnection()
        conn=connn.cursor()

        with open('predefined.json','r') as file:
            jsonfile=json.load(file)
        ColumnNames=jsonfile['Columns']
        for key in ColumnNames.keys():
            datatype=ColumnNames[key]
            try:
                conn.execute('CREATE TABLE TestTable_Test_new  ({columnname} {datatype})'.format(columnname=key,datatype=datatype))
            except:
                conn.execute('DROP TABLE TestTable_Test_new')
                conn.execute('CREATE TABLE TestTable_Test_new  ({columnname} {datatype})'.format(columnname=key,datatype=datatype))

    def insertdataintotable(self):
        connn=self.databaseconnection()
        conn=connn.cursor()
        path='CSV Files'
        file= [file for file in os.listdir(os.getcwd()+'/'+os.path.join('CSV Files'))]
        for files in file:
            with open(path+'/'+files,'r') as file:
                next(file)
                reader = csv.reader(file)
                values = enumerate(reader)
                for value in values:
                    for line in value[1]:
                        try:
                            conn.execute('INSERT INTO TestTable_Test_new values ({values})'.format(values=line))
                        except Exception as e:
                            raise e


    def tabledatatocsv(self):
        inputfilepath='CSV Files'
        connn=self.databaseconnection()
        conn=connn.cursor()
        conn.execute("SELECT * FROM TestTable_Test_new")
        dataforcsv=[data for data in conn.fetchall()]
        headers=[i[0] for i in conn.description]
        os.chdir(inputfilepath)
        with open('input.csv','w') as file:
            csvwriter=csv.writer(file)
            csvwriter.writerow(headers)
            csvwriter.writerow(dataforcsv)
        conn.close()






