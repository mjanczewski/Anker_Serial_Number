import requests
import json
from config.connectionConfig import BaselinkerToken


def getOrders():
    TOKEN = BaselinkerToken()
    status_id = "58904"
    getOrders = "getOrders"

    data = {
        "token": TOKEN,
        "method": getOrders,
    }

    response = requests.post("https://api.baselinker.com/connector.php", data=data)

    show = response.json()
    json_format = json.dumps(show, indent=2)
    print(json_format)
