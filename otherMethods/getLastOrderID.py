import sqlite3 as sql
import pandas as pd


def get_last_order_id():
    conn = sql.connect("config.sqlite")
    last_order_id = pd.read_sql("select last_order_id from lastOrderId", conn)
    last_order_id = last_order_id["last_order_id"]
    last_order_id = last_order_id.to_string().split()
    last_order_id = last_order_id[1]

    return last_order_id
