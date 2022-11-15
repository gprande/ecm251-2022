class Cart_Control():
    def __init__(self) -> None:
        self._cart = []
    
    def add(self,product):
        for item in self._cart:
            if product.get_Name() == item.get_Name():
                return False
        self._cart.append(product)  
        return True 

    def remove(self,product):
        if product in self._cart:
            self._cart.remove(product) 
    
    def show_Products(self,product):
        return self._cart[product]

    def show_All(self):
        result = []
        for item in self._cart:
            result.append(item.get_Name())
        return result
          
    def get_Product_Qty(self):
        return len(self._cart)
    
    def get_Total(self):
        total = 0.0
        for product in self._cart:
            total += product.get_Value()
        return total