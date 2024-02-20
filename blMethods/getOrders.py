import requests
import json
import os
from config.connectionConfig import BaselinkerToken
from otherMethods.getLastOrderID import get_last_order_id


def get_orders():
    TOKEN = BaselinkerToken()
    file_name = "last_order_id.txt"
    status_id = 68690
    getOrders = "getOrders"
    id_from = get_last_order_id()

    parameters = json.dumps({"id_from": id_from, "status_id": status_id})
    data = {"token": TOKEN, "method": getOrders, "parameters": parameters}

    response = requests.post("https://api.baselinker.com/connector.php", data=data)

    show = response.json()

    for i in range(len(show["orders"])):

        number_of_products = len(show["orders"][i]["products"])
        last_order_id = show["orders"][i]["order_id"]

        if number_of_products == 1:
            print(
                show["orders"][i]["order_id"],
                show["orders"][i]["admin_comments"],
                show["orders"][i]["user_login"],
                show["orders"][i]["delivery_fullname"],
                show["orders"][i]["products"][0]["sku"],
            )
        else:
            for j in range(number_of_products):
                print(
                    show["orders"][i]["order_id"],
                    show["orders"][i]["admin_comments"],
                    show["orders"][i]["user_login"],
                    show["orders"][i]["delivery_fullname"],
                    show["orders"][i]["products"][j]["sku"],
                    "=========================================",
                )

    with open(file_name, "w") as file:
        file.write(str(last_order_id + 1))
    file.close()

    id_from = last_order_id + 1
    print(id_from)

    # print(show["orders"][0]["order_id"], show["orders"][0]["admin_comments"])
    # print(len(show["orders"]))
    # print(show["orders"][0])

    # json_format = json.dumps(show, indent=2)
    # print(json_format)
