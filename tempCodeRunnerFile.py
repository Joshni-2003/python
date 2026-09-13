class Product:
    def __init__(self,b,c,p):
        self.brand=b
        self.color=c
        self.price=p

        
    def Show(self):
        print(self.brand)
        print(self.color)
        print(self.price)
    def disc(self,discu):
        discount=(self.price*discu)/100
        print(discount)
        total_purchase=(self.price-discount)
        print(total_purchase,"total_amount")
obj=Product("iqoo","black",27000)
obj.Show()
obj.disc(5)