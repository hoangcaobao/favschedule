from flask import Flask, redirect, render_template, url_for, request
import psycopg2 as pg
import time
import threading
app = Flask(__name__)

class postgresDB ():
    def __init__(self,user=None,pwd=None,host=None,port=None,database=None,limited_time=10):
        # public
        self.user = user;
        self.pwd = pwd;
        self.host = host;
        self.port = port;
        self.database = database;
        self.limited_time = limited_time;
        self.life_time = 0;
        # private
        self.isConnect = False;
        self.connection = None;
        # count
        # self.count = threading.Thread(target=self.__count);
        # self.count.setDaemon(True);
        # self.run_thread = False;
        # self.stop_thread = False;

    def createConnection (self,user=None,pwd=None,host=None,port=None,database=None):
        if (self.isConnect):
            print("Already connect to PostgreSQL");
            return self;
        try:
            self.connection = pg.connect(
                user = user or self.user,
                password = pwd or self.pwd,
                host = host or self.host,
                port = port or self.port,
                database = database or self.database
            )
            # self.run_thread = True;
            self.user = user or self.user;
            self.pwd = pwd or self.pwd;
            self.host = host or self.host;
            self.port = port or self.port;
            self.database = database or self.database;
            self.isConnect = True;
            return self.connection;
        except (Exception, pg.Error) as error :
            self.isConnect = False;
            print ("Error while connecting to PostgreSQL", error)
            return error
    
    def closeConnection (self):
        if(self.isConnect and self.connection):
            # self.resetCount();
            self.connection.close()
            print("PostgreSQL connection is closed")
            self.connection = None;
            self.isConnect = False;
            self.run_thread = False;
        else:
            print("PostgreSQL connection is already closed")

    def isConnect (self):
        return self.isConnect;
    
    def getConnection (self):
        if (not self.isConnect):
            print('No existence connection, creating new one ...');
            return self.createConnection(self.user,self.pwd,self.host,self.port,self.database);
        else:
            return self.connection;
    
    def execute (self,cmd,args=None):
        try:
            conn = self.getConnection();
            cursor = conn.cursor();
            cursor.execute(cmd,args);
            conn.commit();
            return cursor;
        except (Exception, pg.Error) as error :
            print ("Error while execute command {} (PostgreSQL)".format(cmd), error)
            return error
