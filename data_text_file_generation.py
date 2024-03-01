import mysql.connector


class DatabaseTextFile:
    def __init__(self, database: str, table: str, host: str, user: str, password: str, port: str):
        self.database = database
        self.table = table
        self.host = host
        self.user = user
        self.password = password
        self.port = port

    def data_collection_from_database(self, batch_size=6000):
        try:
            my_database = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port,
                database=self.database
            )

            cursor = my_database.cursor()
            cursor.execute("SELECT * FROM {}".format(self.table))

            while True:
                batch = cursor.fetchmany(batch_size)
                if not batch:
                    break

                for row in batch:
                    yield ','.join(map(str, row))

            cursor.close()
            my_database.close()

        except mysql.connector.Error as err:
            print("Sql error: SQL database error", err)

    def database_data_to_text(self, data_encoding: str, limit: int):
        i = 0
        try:
            with open(self.table + "_data.txt", "w", encoding=data_encoding) as file:
                for row in self.data_collection_from_database():
                    file.write(row + "\n")
                    i += 1

                    if i >= limit:
                        break
        except Exception as e:
            print("Error: Unexpected error occurred", e)
