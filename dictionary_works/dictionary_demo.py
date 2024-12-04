#create a dictionary product with keys id,title,price,brand

product={"id":17,"title":"perfume","price":400,"brand":"My Op"}
print(product["title"])

#update product price as 500

product["price"]=500
print(product)

#update brand as blossom

product["brand"]="blosssom"
print(product)

#add a field

product["ude_by_date"]="30.07.2003"
print(product)

#add offer is 10 if offer exist else offer as 20

if "offer" is product:
    product["offer"]=10

else:
    product["offer"]=20

print(product)