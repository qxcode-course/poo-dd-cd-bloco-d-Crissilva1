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

    def get_nome(self)->str:
        return self.__nome
    
    def get_favorito(self)->bool:
        return self.__favorito
    
    def addFone(self, id:str, number:str):
       if id in self.__fones:
           raise Exception(f"fone {id} já existe")
       self.__fones[id]= Fone(id,number)

    def existeFone(self, id:str)->bool:
        return id in self.__fones

       
    
    def rmfone(self, index:int):
        if index < 0 or index >= len(self.__fones):
                return 
        
        chaves= list(self.__fones.keys())
        if 0 <=index < len(chaves):
            chave=chaves[index]
            del self.__fones[chave]

        
      
    
    def toogleFavorited(self):
        self.__favorito = not self.__favorito

    def isfavorited(self)->bool:
        return self.__favorito
    
    def set_nome(self,nome:str):
        self.__nome=nome
            
    def __str__(self):
        fones= ", " .join(str(elem) for elem in self.__fones.values())
        return f"- {self.__nome} [{fones}]"
       


class Agenda:
    def __init__(self):
        self.__contatos:dict[str,Contato]={}

    def addContato(self, nome:str, fones:dict[str,Fone]):
        if nome not in self.__contatos:
            self.__contatos[nome]=Contato(nome)
        contato=self.__contatos[nome]    
       
        for id, fone in fones.items():
          if not contato.existeFone(id):
              contato.addFone(id, fone.get_number())

    def rmContato(self,nome:str):
        if nome in self.__contatos:
         del self.__contatos[nome]

    def get_contatos(self):
        return self.__contatos
    
    def __str__(self):

        contatos_Ordenados= sorted(self.__contatos.values(), key=lambda c:c.get_nome())
        return "\n".join(str(c)for c in contatos_Ordenados)

    
    
    
        
def main():
    agenda=Agenda( )   
    while True:
        line:str=input()
        print ("$"+line)
        args:list[str]=line.split(" ")
        if args[0]=="end":
            break
        elif args[0]=="show":
            print(agenda)
        elif args[0]=="add":
            nome=args[1]

            pares= args[2:]
            fones:dict[str,Fone]={}

            for p in pares:
                id, numero = p.split(":")
                fones[id]=Fone(id,numero)
            agenda.addContato(nome, fones)
        elif args[0]=="rmfone":
            nome= args[1]
            index=int(args[2])
            contato=agenda.get_contatos().get(nome)

            if contato:
                contato.rmfone(index)  
        elif args[0]=="rm":
            nome=args[1]
            agenda.rmContato(nome)
           
main()