import requests
import json
import os
import pandas as pd
import sqlite3 as sql
from config.connectionConfig import BaselinkerToken
from otherMethods.getLastOrderID import get_last_order_id
from blMethods.getInvoices import get_invoices


def get_orders():

    TOKEN = BaselinkerToken()
    status_id = 68690
    getOrders = "getOrders"
    id_from = get_last_order_id()
    orders_list = []

    parameters = json.dumps({"id_from": id_from, "status_id": status_id})
    data = {"token": TOKEN, "method": getOrders, "parameters": parameters}

    response = requests.post("https://api.baselinker.com/connector.php", data=data)
    show = response.json()

    for i in range(len(show["orders"])):

        number_of_products = len(show["orders"][i]["products"])
        last_order_id = show["orders"][i]["order_id"]

        for j in range(number_of_products):
            if show["orders"][i]["admin_comments"] != "":
                bl_order_id = show["orders"][i]["order_id"]
                bl_admin_comment = show["orders"][i]["admin_comments"]
                bl_user_login = show["orders"][i]["user_login"]
                bl_user_fullname = show["orders"][i]["delivery_fullname"]
                bl_sku = show["orders"][i]["products"][j]["sku"]

                orders_list.append(
                    [
                        bl_order_id,
                        bl_admin_comment,
                        bl_user_login,
                        bl_user_fullname,
                        bl_sku,
                    ]
                )
            else:
                continue

    last_order_id += 1

    conn = sql.connect("config.sqlite")
    conn.execute(f"""UPDATE lastOrderId SET last_order_id = {last_order_id}""")
    conn.commit()

    get_invoices(orders_list)
