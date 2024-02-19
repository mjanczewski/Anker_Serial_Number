import requests
import json
from config.connectionConfig import BaselinkerToken


def getInvoices():
    TOKEN = BaselinkerToken()
    # status_id = "58904"
    getInvoices = "getInvoices"
    baselinker_query = dict({"order_id": 178241300})
    baselinker_query = json.dumps(baselinker_query)

    data = {"token": TOKEN, "method": getInvoices, "parameters": baselinker_query}

    response = requests.post("https://api.baselinker.com/connector.php", data=data)

    show = response.json()
    json_format = json.dumps(show, indent=2)
    print(json_format)
