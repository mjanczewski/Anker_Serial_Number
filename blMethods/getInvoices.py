import requests
import json
import pandas as pd
import sqlite3 as sql
from config.connectionConfig import BaselinkerToken


def get_invoices(orders_list):
    TOKEN = BaselinkerToken()
    list_orders_df = pd.DataFrame(orders_list, dtype="object")
    file_name = "orders.csv"
    rename_columns = {
        "index": "ID",
        0: "BL_Id",
        1: "Serial_Number",
        2: "Nick",
        3: "Imie_Nazwisko",
        4: "SKU",
    }

    for index, row in list_orders_df.iterrows():
        getInvoices = "getInvoices"
        baselinker_query = dict({"order_id": row[0]})
        baselinker_query = json.dumps(baselinker_query)

        data = {"token": TOKEN, "method": getInvoices, "parameters": baselinker_query}
        response = requests.post("https://api.baselinker.com/connector.php", data=data)

        show = response.json()
        invoices_namber = show["invoices"][0]["external_invoice_number"]
        list_orders_df.loc[index, "FS"] = invoices_namber

    list_orders_df = list_orders_df.rename(columns=rename_columns)
    list_orders_df.to_csv(
        file_name, sep=";", index=False, mode="a", header=False, encoding="utf8"
    )

    conn = sql.connect("serial_number.sqlite")
    list_orders_df.to_sql("serial_number", conn, if_exists="append")
