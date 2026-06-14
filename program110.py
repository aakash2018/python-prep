class BaseChai:
    
    def __init__(self,type_):
        self.type = type_
        
    def prepare(self):
        print(f"Preaparing {self.type} chai....")
        

class MasalaChai(BaseChai):
    
    def add_spices(self):
        print("adding cardamon,ginger,cloves.")
        

class ChaiShop:
    chai_cls = BaseChai
    
    def __init__(self) -> None:
        self.chai = self.chai_cls("Regular")
    
    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()
    

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai
    
    def __init__(self) -> None:
        self.chai = self.chai_cls("Regular")
    
    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()
        

shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()

        

   