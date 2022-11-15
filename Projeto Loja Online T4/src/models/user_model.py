class User():
    def __init__(self, username, 
                 email, 
                 password, 
                 cpf, 
                 birthdate, 
                 name):
        self._username = username
        self._email = email
        self._password = password
        self._cpf = cpf
        self._birthdate = birthdate
        self._name = name
        self._contador = 0
    
    def get_Username(self):
        return self._username

    def get_Name(self):
        return self._name
    
    def get_Email(self):
        return self._email

    def set_Email(self, email):
        self._email = email   
    
    def get_Cpf(self):
        return self._cpf
    
    def get_Birthdate(self):
        return self._birthdate

    def get_Password(self):
        return self._password  

    def set_Password(self, password):
        self._password = password
    
    def __str__(self) -> str:
        return f'Username:"{self._username}", E-mail:"{self._email}", Password:"{self._password}", Nome:"{self._name}", Nascimento:"{self._birthdate}", CPF:"{self._cpf}".'