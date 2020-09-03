import importlib
from flask import Flask, redirect, render_template, url_for, request,session
import psycopg2 as pg
from markupsafe import escape



weekly_table_cmd = {
    'create_table': '''
    CREATE TABLE {} (
        type varchar,
        act_index int,
        Sun varchar,
        Mon varchar,
        Tu varchar,
        We varchar,
        Th varchar,
        Fr varchar,
        Sa varchar
    );
    ''',
    'load_table': '''SELECT * FROM {} WHERE type = 'time' or type = 'data' or type = 'name' '''

}

daily_table_cmd = {
    'create_table': '''
        CREATE TABLE {} (
            type varchar,
            act_index int,
            begin_time varchar,
            end_time varchar,
            name varchar,
            description varchar,
            active varchar
        );
    ''',
    'index': {
        'type':0,
        'act_index':1,
        'begin_time':2,
        'end_time':3,
        'name':4,
        'description':5,
        'active':6
    } ,  
    'load_table': '''SELECT * FROM {} WHERE type = 'time' or type = 'data' or type = 'name' '''
}

_login = {
    'check_login': '''
        SELECT * FROM USERS WHERE username = %s AND pwd = %s
    ''' 

} 

cmd = [weekly_table_cmd,daily_table_cmd]

