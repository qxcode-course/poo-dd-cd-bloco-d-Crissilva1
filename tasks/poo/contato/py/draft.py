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
        self.__fones:list[Fone]=[]

    def get_nome(self,nome:str)->None:
        self.__nome=nome
    
    def get_favorito(self)->bool:
        return self.__favorito
    
    def get_fone(self):
        return self.__fones
    
    def addFone(self, id:str, number:str):
       fone=Fone(id,number)
       if not fone.isValid():
           raise Exception(f"fail: invalid number")
       self.__fones.append(fone)


       
    
    def rmFone(self, index:int):
       del self.__fones[index]

    
    def toogleFavorited(self):
        self.__favorito = not self.__favorito

    def isfavorited(self)->bool:
        return self.__favorito
    
    def set_nome(self,nome:str):
        self.__nome=nome
            
    def __str__(self):
       favorito="@ "  if self.__favorito is True else "- "
       fones=", ".join(str(x)for x in self.__fones)
       return f"{favorito}{self.__nome} [{fones}]"
       
      

def main():
    contato=Contato   
    while True:
        line:str=input()
        print ("$"+line)
        args:list[str]=line.split(" ")
        try:
            if args[0]=="end":
               break
            elif args[0]=="show":
              print(contato)
            elif args[0]=="init":
              nome:str=(args[1])
              contato=Contato(nome)
            elif args[0]=="add":
              id=args[1]
              numero=args[2]
              contato.addFone(id,numero)
            elif args[0]=="rm":
              index=int(args[1])
              contato.rmFone(index)
            elif args[0]=="tfav":
              contato.toogleFavorited()
            else:
              print("comando invalido")
        except Exception as e:
          print(e)    
            
main()