class Fone:
    def __init__(self, id:str, number:str):
        self.__id: str = id
        self.__number: str = number

    def get_id(self)->str:
        return self.__id
    
    def get_number(self)->str:
        return self.__number
    
    def isValid(self)->bool:
        validos="0123456789()."
        for carac in self.__number:
            if carac not in validos:
                return False
        return True 
    
    def __str__(self)->str:
        return f"{self.__id}:{self.__number}"
    
class Contato:
    def __init__(self, nome:str):
        self.__nome:str=nome
        self.__favorito:bool=False
        self.__fones:list[Fone|None]=[]

    def get_nome(self)->str:
        return self.__nome
    
    def get_favorito(self)->bool:
        return self.__favorito
    
    def get_fone(self):
        return self.__fones
    
    def addFone(self, nome:str, number:str):
        fone=Fone(nome,number)
        
        if not fone.isValid():
            raise Exception("fone invalido")
        
        self.__fones.append(fone)
    
    def remover(self, index:int):
        if index < 0 or index >= len(self.__fones):
                return 
        
        del self.__fones[index]
        return 
    
    def toogleFavorited(self):
        self.__favorito = not self.__favorito

    def isfavorited(self)->bool:
        return self.__favorito
    
    def set_nome(self,nome:str):
        self.__nome=nome
            
    def __str__(self):
        fones= ", ".join(str(elem) for elem in self.__fones)
        return f"{fones}"
       


class Agenda:
    def __init__(self):
        self.__contatos:list[Contato|None]=[]

    def get_contatos(self):
        return self.__contatos
    
    
        

def main():
    contato=None    
    while True:
        line:str=input()
        print ("$"+line)
        args:list[str]=line.split(" ")
        if args[0]=="end":
            break
        elif args[0]=="show":
            print(contato)
        elif args[0]=="init":
            nome:str=(args[1])
            contato=Contato(nome)
            
