def get_last_order_id():
    file = open("last_order_id.txt")
    last_order_id = file.read()
    return last_order_id
