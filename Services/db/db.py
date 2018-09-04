import sqlite3
import os


class DBService:

    def __init__(self):
        self.db = None
        self.cursor = None

        self.self_dir = os.path.dirname(os.path.abspath(__file__))

    def init_db(self):
        if os.path.isfile(os.path.join(self.self_dir, "wudb")):
            return

        self.connect_db()

        if os.path.isfile(os.path.join(self.self_dir, "dump.sql")):
            schema = open(os.path.join(self.self_dir, "dump.sql"), "r").readlines()
        else:
            schema = open(os.path.join(self.self_dir, "schema.sql"), "r").readlines()

        for line in schema:
            db_answer = self.exec(line)
            if db_answer["error"] is not None:
                print(db_answer["error"])

        self.disconnect_db()

    def dump_db(self):
        self.connect_db()

        with open(os.path.join(self.self_dir, "dump.sql"), 'w') as f:
            for line in self.db.iterdump():
                if line != "COMMIT;" and line != "BEGIN TRANSACTION;":
                    f.write('%s\n' % line)

        self.disconnect_db()

    def remove_db(self):
        os.remove(os.path.join(self.self_dir, "wudb"))

    def exec(self, query: str):
        error = None
        answer = []
        try:
            self.cursor.execute(query)
            self.db.commit()
            answer = self.cursor.fetchall()

        except sqlite3.OperationalError as err:
            error = err

        return {"fetch": answer, "error": error}

    def connect_db(self):
        self.db = sqlite3.connect(os.path.join(self.self_dir, "wudb"))
        self.cursor = self.db.cursor()

    def disconnect_db(self):
        self.db.close()
        self.db = None
        self.cursor = None
