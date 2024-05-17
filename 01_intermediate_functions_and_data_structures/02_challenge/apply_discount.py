def apply_discount(
    products, minimum_price, discount_rate
):
   calculate_discount = lambda a : a * (1-discount_rate*0.01)
   
   
   result = [
       (
           elem["name"],
           calculate_discount(elem["price"]),
       )
       for elem in products
       if elem["price"] >= minimum_price
   ]
   print(result)
   return result
   
data1=[
    {"name": "Laptop", "category": "Electronics", "price": 1200},
    {"name": "Bread", "category": "Food", "price": 2},
    {"name": "Jacket", "category": "Apparel", "price": 100}
]

data2=[
    {"name": "Smartphone", "category": "Electronics", "price": 800},
    {"name": "Sneakers", "category": "Footwear", "price": 120},
    {"name": "Coffee", "category": "Beverage", "price": 5}
]

apply_discount(data1,50,10)
apply_discount(data2,100,15)