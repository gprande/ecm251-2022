from pickle import FALSE, TRUE
import sqlite3
from models.user_model import User

class User_DAO:    
    _instance = None
    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = User_DAO
        ()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./database/sqlite.db')
    
    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Usuarios;
        """)
        results = []
        for result in self.cursor.fetchall():
            results.append(User(username = result[0],
                                    name = result[1],
                                    email = result[2],
                                    password = result[3],
                                    cpf = result[4],
                                    birthdate = result[5]))
        self.cursor.close()
        return results

    def add_users(self,user):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Usuarios (username, name, email, password, cpf, birthdate)
            VALUES(?,?,?,?,?,?);
        """, (user.get_Username(), 
              user.get_Name(), 
              user.get_Email(), 
              user.get_Password(), 
              user.get_Cpf(), 
              user.get_Birthdate()))
        self.conn.commit()
        self.cursor.close()
        
    def get_users(self,username):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Usuarios WHERE username == '{username}';
        """)
        item = None
        result = self.cursor.fetchone()
        if result != None:
            item = User(username = result[0],
                        name = result[1],
                        email = result[2],
                        password = result[3],
                        cpf = result[4],
                        birthdate = result[5])
        self.cursor.close()
        return item
    
    def update_users(self,user):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Usuarios 
                SET email = '{user.get_Email()}', password = '{user.get_Password()}'
                WHERE username == '{user.get_Username()}';
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def del_user(self, username):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE from Usuarios WHERE id == '{username}';
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True

