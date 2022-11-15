class Product():    
    def __init__(self,name,description,keyword,value,image):
        self._name = name
        self._description = description
        self._keyword = keyword
        self._value = value
        self._image = image
    
    def get_Name(self):
        return self._name
    
    def get_Description(self):
        return self._description
    
    def get_Keyword(self):
        return self._keyword
    
    def get_Value(self):
        return self._value
    
    def get_Image(self):
        return self._image
        
    def __str__(self) -> str:
        return f'Name: {self._name} - R$ {str(self._value)}'