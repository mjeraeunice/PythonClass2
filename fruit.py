class Fruit:
    taste="sweet"
    def __init__(self,colour,name,price):
        self.colour = colour
        self.name=name
        self.price=price
    def buy_fruits(self):
        total= self.price *5
        return f"I bought 5 {self.name} fruits at {total} kshs"
    def make_juice(self):
        return f"I made {self.taste} {self.name} juice"
    def sell_juice(self):
        return f"I sold {self.name} juice at a price of {self.price}ksh per glass"