from models.product_model import Product
from dao.product_dao import Product_DAO
import base64

class Product_Control():
    def __init__(self) -> None:
        self.product_db = Product_DAO()
        self._product_list = self.product_db.get_all()
    
    def add_new_product(self,name,description,keyword,value,imagem):
        try:
            bin_string = base64.b64encode(imagem.getvalue())
            construct_img = base64.b64decode((bin_string))
            Aux = Product(name,description,keyword,value,construct_img)  
            self.product_db.add_item(Aux)
        except:
            return False 
        return True
    
    def show_Products(self,product):
        return self._product_list[product]
    
    def get_Product(self,index):
        return self._product_list[index]
    
    def get_Product_Qty(self):
        return len(self._product_list)
    
    def remove(self,product):
        return self.product_db.del_item(product)