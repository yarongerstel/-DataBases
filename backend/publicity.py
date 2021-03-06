from flask_mysqldb import MySQL
import utils


def insert(mysql: MySQL, price, location, goal):
    query = f"insert into publicity(price, location, goal) values({price},'{location}',{goal})"
    utils.execute_action(mysql, query)


def update(mysql: MySQL, id, price, location, goal):
    query = f"update publicity " \
            f"set " \
            f"price={price}, " \
            f"location='{location}', " \
            f"goal='{goal}'" \
            f"where id={id}"
    utils.execute_action(mysql, query)