import sqlite3

from blMethods.getOrders import get_orders

# from getOrders import get_orders


# def create_table():

#     conn = sqlite3.connect("config.sqlite")
#     c = conn.cursor()

#     c.execute(
#         """CREATE TABLE lastOrderId
#                 (last_order_id TEXT)"""
#     )

#     c.execute(
#         """INSERT INTO lastOrderId VALUES
#             ('0')"""
#     )

#     # c.execute(
#     #     """CREATE TABLE serial_number
#     #             (ID TEXT, BL_Id TEXT, Serial_Number TEXT, Nick TEXT, Imie_Nazwisko TEXT, SKU TEXT)"""
#     # )

#     conn.commit()
#     conn.close()


# create_table()
get_orders()
