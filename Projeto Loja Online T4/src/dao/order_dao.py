import sqlite3
from models.order_model import Order

class Order_DAO:
    _instance = None
    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = Order_DAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./database/sqlite.db')

    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Pedidos;
        """)
        results = []
        for result in self.cursor.fetchall():
            results.append(Order(order_num = result[0],
                                     id_customer = result[1], 
                                     products = result[2],
                                     total = result[3], 
                                     day_time = result[4]))
        self.cursor.close()
        return results
    
    def new_order(self, order):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            INSERT INTO Pedidos (
                id, 
                id_cliente, 
                produtos,
                valor_total, 
                data_hora
            )
            VALUES(
                "{order.order_num}",
                "{order.id_customer}",
                "{order.products}",
                "{order.total}",
                "{order.day_time}"
            );
        """)
        self.conn.commit()
        self.cursor.close()
    
    def get_order(self, order_num):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Pedidos WHERE id == "{order_num}";
        """)
        results = []
        for result in self.cursor.fetchall():
            results.append(Order(order_num = result[0],
                                     id_customer = result[1], 
                                     products = result[2],
                                     total= result[3], 
                                     day_time = result[4]))
        self.cursor.close()
        return results
    
    def update_order(self, order):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Pedidos 
                SET produtos = "{order.products}", valor_total = "{order.total}", data_hora = "{order.day_time}"
                WHERE id == "{order.order_num}";
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def del_order(self, order):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE FROM Pedidos WHERE id == "{order.order_num}";
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True