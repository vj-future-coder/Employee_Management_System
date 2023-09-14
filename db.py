import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY,
        name TEXT,
        age TEXT,
        doj TEXT,
        email TEXT,
        gender TEXT,
        contact TEXT,
        address TEXT
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # insert function
    def insert(self, name, age, doj, email, gender, contact, address):
        self.cur.execute("INSERT INTO employees VALUES (NULL,?,?,?,?,?,?,?)",
                         (name, age, doj, email, gender, contact, address))
        self.con.commit()
    #fetch all data from db
    def fetch(self):
        self.cur.execute("SELECT * FROM employees")
        row=self.cur.fetchall()
        #print(row)
        return row

    #delete a record in db
    def remove(self,id):
        self.cur.execute("delete from employees where id=?",(id,))
        self.con.commit()
    #udate a record in db

    def update(self, id, name, age, doj, email, gender, contact, address):
        self.cur.execute(
            "UPDATE employees SET name=?, age=?, doj=?, email=?, gender=?, contact=?, address=? WHERE id=?",
            (name, age, doj, email, gender, contact, address, id))
        self.con.commit()

#o = Database("employees.db")
#o.update(2, "srityram", "23", "29-04-2000", "sri@gmail.com", "male", "9345354556", "5/114 south salakkadu,rasampalyayam")
#o.insert("srityram", "23", "29-04-2000", "sri@gmail.com", "male", "9345354556", "5/114 south salakkadu,rasampalyayam")
#o.remove("3")
#o.fetch()
