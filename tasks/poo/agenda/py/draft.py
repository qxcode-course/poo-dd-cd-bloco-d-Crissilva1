class Fone:
    def __init__(self, id:str, number:str):
        self.__id :str = id
        self.__number:str = number

    def get_number(self)->str:
        return self.__number
    
    def get_id(self)->str:
        return self.__id
    
    def isValid(self, number:str):
        

    
    def __str__(self)->str:
        return f"{self.__number}:{self.__id}"
    
class Contato:
    def __init__(self, nome:str, favorito:bool):
        self.__nome:str = nome
        self.__favorito:bool = favorito
        self.__fone:list[Fone|None]=[]
    
    def get_nome(self)->str:
        return self.__nome
    
    def get_favorito(self)->bool:
        return self.__favorito
    
    def get_fone(self):
        return self.__fone
    