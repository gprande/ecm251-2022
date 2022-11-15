from models.order_model import Order
from dao.order_dao import Order_DAO

class Order_Control:
    def __init__(self) -> None:
        self.order_db = Order_DAO()

    def new_order(self,id_customer, cart, day_time):
        try:
            order_num = len(self.order_db.get_all())+1
            products = str(cart.show_all())
            total = cart.get_Total()
            Aux = Order(order_num, id_customer, products, total, day_time)
            self.order_db.new_order(Aux)
        except:
            return False
        return True