class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = 'products.txt'

    def __init__(self):
        self.products = self.get_products()

    def get_products(self):
        products = []
        try:
            with open(self.__file_name, 'r') as file:
                for line in file:
                    name, weight, category = line.strip().split(', ')
                    products.append(Product(name, float(weight), category))
        except FileNotFoundError:
            open(self.__file_name, 'w').close()
        return products

    def add(self, *products):
        for product in products:
            if isinstance(product, Product):
                if any(p.name == product.name for p in self.products):
                    print(f"Продукт '{product.name}' уже есть в магазине.")
                else:
                    self.products.append(product)
                    with open(self.__file_name, 'a') as file:
                        file.write(f"{product}\n")
            else:
                print("Передан неверный тип продукта.")

if __name__ == "__main__":
    shop = Shop()


    potato = Product('Potato', 50.0, 'Vegetables')
    tomato = Product('Tomato', 30.0, 'Vegetables')
    
    shop.add(potato) 
    shop.add(tomato)
    shop.add(potato)

    for product in shop.products:
        print(product)


s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')

p2 = Product('Spaghetti', 3.4, 'Groceries')

p3 = Product('Potato', 5.5, 'Vegetables')



print(p2) 



s1.add(p1, p2, p3)



print(s1.get_products())