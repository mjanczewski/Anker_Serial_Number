import requests
import json
import pandas as pd
from config.connectionConfig import BaselinkerToken


def get_invoices(orders_list):
    TOKEN = BaselinkerToken()
    list_orders_df = pd.DataFrame(orders_list, dtype="object")
    file_name = "orders.csv"

    print(list_orders_df.info())

    # getInvoices = "getInvoices"
    # baselinker_query = dict({"order_id": 178241300})
    # baselinker_query = json.dumps(baselinker_query)

    # data = {"token": TOKEN, "method": getInvoices, "parameters": baselinker_query}

    # response = requests.post("https://api.baselinker.com/connector.php", data=data)

    # show = response.json()
    # print(show["invoices"][0]["external_invoice_number"])

    for index, row in list_orders_df.iterrows():
        getInvoices = "getInvoices"
        baselinker_query = dict({"order_id": row[0]})
        baselinker_query = json.dumps(baselinker_query)

        data = {"token": TOKEN, "method": getInvoices, "parameters": baselinker_query}

        response = requests.post("https://api.baselinker.com/connector.php", data=data)

        show = response.json()
        invoices_namber = show["invoices"][0]["external_invoice_number"]
        # print(invoices_namber)
        # row["FS"] = invoices_namber
        list_orders_df.loc[index, "FS"] = invoices_namber
        # print(list_orders_df.loc[index])

        # print(list_orders_df)
        # with open(file_name, "a") as file:
        #     file.write(str(list_orders_df.loc[index]))
        # file.close()

    list_orders_df.to_csv(
        file_name, sep=";", index=False, mode="a", header=False, encoding="utf8"
    )

    # json_format = json.dumps(show, indent=2)
    # print(json_format)
