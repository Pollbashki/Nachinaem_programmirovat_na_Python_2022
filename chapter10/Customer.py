class Customer:
    def __init__(self, name, adress, phone):
        self.__name = name
        self.__adress = adress
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_adress(self, adress):
        self.__adress = adress

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name
    
    def get_adress(self):
        return self.__adress
    
    def get_phone(self):
        return self.__phone
    
    def __str__(self):
        return (
            f"Имя: {self.__name} \n" + \
            f"Телефон: {self.__phone} \n" + \
            f"Электронная почта {self.__adress }"
        )