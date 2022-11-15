from pickle import FALSE, TRUE
import sqlite3
from models.product_model import Product

class Product_DAO:    
    _instance = None
    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = Product_DAO
        ()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./database/sqlite.db')

    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Jogos;
        """)
        results = []
        for result in self.cursor.fetchall():
            results.append(Product(keyword = result[0],
                                      name = result[1],
                                      description = result[2],
                                      value = result[3],
                                      image = result[4]))
        self.cursor.close()
        return results
    
    def add_item(self, item):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Jogos (id, nome, descricao, preco, imagem)
            VALUES(?,?,?,?,?);
        """, (item.get_Keyword(), 
              item.get_Name(), 
              item.get_Description(), 
              item.get_Value(), 
              item.get_Image()))
        self.conn.commit()
        self.cursor.close()
    
    def get_item(self, product):
        id = product.get_Keyword()
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Jogos WHERE id == '{id}';
        """)
        item = None
        result = self.cursor.fetchone()
        if result != None:
            item = Product(keyword = result[0],
                           name = result[1],
                           description = result[2],
                           value = result[3],
                           image = result[4])
        self.cursor.close()
        return item

    def update_item(self,item):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Jogos 
                SET nome = '{item.get_Name()}', preco = '{item.get_Value()}'
                WHERE id == '{item.get_Keyword()}';
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def del_item(self, product):
        id = product.get_Keyword()
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE from Jogos WHERE id == '{id}';
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def search_all_for_name(self, nome):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Jogos WHERE nome LIKE '{nome}%';
        """)
        results = []
        for result in self.cursor.fetchall():
            results.append(Product(keyword = result[0],
                                      name = result[1],
                                      description = result[2],
                                      value = result[3],
                                      image = result[4]))
        self.cursor.close()
        return results