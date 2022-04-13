import sqlite3
defaultDB = "YtdHistory"
def saveBySqlite(titulo, tipo, data, dbName=None):
    global defaultDB
    if not dbName:  dbName = defaultDB

    connection = sqlite3.connect(dbName)
    hand = connection.cursor()

    try:
        hand.execute(
            f"""
            CREATE TABLE {dbName}  (
                ID int,
                INFO text NOT NULL,
                DATE text NOT NULL
            )
            """
        )
        hand.execute(
            f"""
            INSERT INTO {dbName} VALUES (
                0,
                '{tipo}:{titulo}',
                '{data}'
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
                {index},
                '{tipo}:{titulo}',
                '{data}'
            )
            """
        )
    connection.commit()
def showSQL(dbName):
    connect = sqlite3.connect(dbName)
    hand = connect.cursor()
    dados = hand.execute(
        f"""
        SELECT * FROM {dbName}
        """
    )
    for dado in dados:
        print(dado)

if __name__ == "__main__":
    showSQL(defaultDB)
