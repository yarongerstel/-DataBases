from flask_mysqldb import MySQL
from flask import Flask, jsonify, request


def execute_action(mysql, query):
        con = mysql.connect
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()
        cursor.close()
        con.close()
        return True


def cursor_result_to_json(cursor):
    return [
        dict(
            (cursor.description[i][0], value)
            for i, value in enumerate(row)
        )
        for row in cursor.fetchall()
    ]


def get_table(mysql: MySQL, table_name):
    query = "select * from %s"
    with mysql.connection.cursor() as cursor:
        cursor.execute(query % (table_name,))
        result = cursor_result_to_json(cursor)
    return result


def execute_select(mysql: MySQL, path, params={}):
    with open(path) as query:
        with mysql.connection.cursor() as cursor:
            cursor.execute(query.read())
            result = cursor_result_to_json(cursor)
    return result


def delete_from_table(mysql: MySQL, table_name, id, id_col_name='id'):
    query = f"DELETE FROM {table_name} WHERE {id_col_name}={id}"
    execute_action(mysql, query)
