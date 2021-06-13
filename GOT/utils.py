from pymongo import MongoClient

conn_str = " "
def get_col_handle():
    client = MongoClient(conn_str)
    db_handle = client.Fynd
    col_handle = db_handle.GOT
    return col_handle


'''def get_collection_handle(db_handle):
    return db_handle['GOT']'''