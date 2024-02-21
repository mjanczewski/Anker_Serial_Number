import requests
import json
import pandas as pd
from config.connectionConfig import BaselinkerToken


def get_invoices():
    TOKEN = BaselinkerToken()

    getInvoices = "getInvoices"
    baselinker_query = dict({"order_id": 178241300})
    baselinker_query = json.dumps(baselinker_query)

    data = {"token": TOKEN, "method": getInvoices, "parameters": baselinker_query}

    response = requests.post("https://api.baselinker.com/connector.php", data=data)

    show = response.json()
    print(show)
    # json_format = json.dumps(show, indent=2)
    # print(json_format)
