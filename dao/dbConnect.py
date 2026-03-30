import pathlib

import mysql.connector

class DBConnect:

    _myPool = None

    def __init__(self):
        raise RuntimeError("Attenzione! Non devi creare un istanza, usa i metodi di classe.")

    @classmethod
    def getConnection(cls):
        #try:
        #    cnx = mysql.connector.connect(
        #        user = "root",
        #        password = "1234",
        #        host = "127.0.0.1",
        #        database = "sw_gestionale"
        #    )
        #    return cnx
#
        #except mysql.connector.Error as err:
        #    print("Non riesco a collegarmi al db")
        #    print(err)
        #    return None

        if cls._myPool is None:
            try:
                cls._myPool = mysql.connector.pooling.MySQLConnectionPool(
                     user = "root",
                     password = "1234",
                     host = "127.0.0.1",
                     database = "sw_gestionale",
                     pool_size= 3,
                     pool_name = "myPool",
                     option_files = f"{pathlib.Path(__file__).resolve().parent}/connector.cfg"
                 )
                return cls._myPool.get_connection()
            except mysql.connector.Error as err:
                print("Non riesco a collegarmi al db")
                print(err)
                return None
        else:
            #vuol dire che la connessione è stata già attivata
            return cls._myPool.get_connection()