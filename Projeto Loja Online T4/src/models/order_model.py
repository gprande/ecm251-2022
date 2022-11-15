class Order:
    def __init__(self, order_num, id_customer, products, total, day_time) -> None:
        self.order_num = order_num
        self.id_customer = id_customer
        self.products = products
        self.total = total
        self.day_time = day_time

    def __str__(self) -> str:
        return f'Order number: {self.order_num} - Customer: {self.id_customer} - Date: {self.day_time}\nProducts: {self.products}\nTotal: {str(self.total)}'
