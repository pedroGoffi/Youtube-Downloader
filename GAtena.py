
defaultDB = "YtdHistory"

def saveBySqlite(
        titulo, 
        tipo, 
        data, 
        author, 
        dbName=None):

    #import sqlite3
    from sqlite3 import connect, Cursor
    global defaultDB
    if not dbName:  dbName = defaultDB

    connection = connect(dbName)
    hand = connection.cursor()

    try:
        hand.execute(
            f"""
            CREATE TABLE {dbName}  (
                ID int,
                INFO text NOT NULL,
                DATE text NOT NULL,
                AUTHOR text NOT NULL
            )
            """
        )
        hand.execute(
            f"""
            INSERT INTO {dbName} VALUES (
                0,
                '{tipo}:{titulo}',
                '{data}',
                '{author}'
            )
            """
        )
    except:
        index = len(hand.execute(
            f"""
                SELECT * FROM {dbName}
            """
        ).fetchall())
        hand.execute(
            f"""
            INSERT INTO {dbName} VALUES (
                '{index}',
                '{tipo}:{titulo}',
                '{data}',
                '{author}'
            )
            """
        )
    connection.commit()
def showSQL(dbName):
    from sqlite3 import connect, Cursor
    connect = connect(dbName)
    hand = connect.cursor()
    try:
        dados = hand.execute(
            f"""
            SELECT * FROM {dbName}
            """
        )
        for dado in dados:
            print(dado)
        return True
    except:
        print(f"Not found any data in the db relative to: {dbName}")
        return False

if __name__ == "__main__":
    showSQL(defaultDB)
