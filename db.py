import mysql.connector as mysql


class Db:

    def __init__(self):
        self.db = mysql.connect(
            host="localhost",
            user="root",
            password="abols",
            database="todos_db"
        )

        self.cursor = self.db.cursor(prepared=True)

      # insert
    def insert(self, to_do):
        query = "INSERT INTO todos (to_do_name) VALUES (%s)"
        values = (to_do, )
        self.cursor.execute(query, values)
        self.db.commit()
        print("To do registered")

  # select
    def select(self):
        query = "SELECT id, to_do_name FROM todos"

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        for record in records:
            id = record[0]
            to_do = record[1]

            print("Id: " + str(id) + " and to do: " + to_do)
            print("------")

        # delete funkcijaja

    def delete(self, id):

        query = "DELETE FROM todos WHERE id =%s"

        values = (id, )

        self.cursor.execute(query, values)

        self.db.commit()

        print(self.cursor.rowcount, "records deleted")

 # update funkcijaja

    def update(self, condition, value):

        query = "UPDATE  todos SET to_do_name = %s WHERE id = %s"

        values = (value, condition)

        self.cursor.execute(query, values)

        self.db.commit()

        print(self.cursor.rowcount, "records update")
