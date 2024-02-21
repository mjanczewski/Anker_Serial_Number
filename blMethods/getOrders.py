import requests
import json
import os
import pandas as pd
from config.connectionConfig import BaselinkerToken
from otherMethods.getLastOrderID import get_last_order_id
from blMethods.getInvoices import get_invoices


def get_orders():
    list_orders_df = pd.DataFrame()
    TOKEN = BaselinkerToken()
    file_name = "last_order_id.txt"
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

                # print(
                #     f"Tylko uzupełniony komentarz \t {bl_order_id} \t {bl_admin_comment}"
                # )
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

            # print(
            #     show["orders"][i]["order_id"],
            #     show["orders"][i]["admin_comments"],
            #     show["orders"][i]["user_login"],
            #     show["orders"][i]["delivery_fullname"],
            #     show["orders"][i]["products"][j]["sku"],
            # )

        # if number_of_products == 1:
        #     print(
        #         show["orders"][i]["order_id"],
        #         show["orders"][i]["admin_comments"],
        #         show["orders"][i]["user_login"],
        #         show["orders"][i]["delivery_fullname"],
        #         show["orders"][i]["products"][0]["sku"],
        #     )
        # else:
        #     for j in range(number_of_products):
        #         print(
        #             show["orders"][i]["order_id"],
        #             show["orders"][i]["admin_comments"],
        #             show["orders"][i]["user_login"],
        #             show["orders"][i]["delivery_fullname"],
        #             show["orders"][i]["products"][j]["sku"],
        #             "=========================================",
        #         )

    with open(file_name, "w") as file:
        file.write(str(last_order_id + 1))
    file.close()

    list_orders_df = pd.DataFrame(orders_list)

    # print(list_orders_df)
    get_invoices(orders_list)
