
cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt","dct"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt","torque"]},
]

#print count of vehicles
print(f"total vehicles=>{len(cars)}")


#print available colors of baleno
baleno_colors=[c.get("colors") for c in cars if c.get("name")=="baleno"]
print(baleno_colors)
#print(baleno_colors[0]) #to remove two list and print only one list


#print all brands
all_brands=[c.get("brand") for c in cars]
print(set(all_brands))
# all_brands={c.get("brand") for c in cars}
# print(all_brands)


#print car names available in amt transmission
amt_cars=[c.get("name") for c in cars if "amt" in c.get("transmissions")]
print(amt_cars) 


#cars available in blue color
blue_cars=[c.get("name") for c in cars if "blue" in c.get("colors")] 
print(blue_cars)


#print all transmission type car
all_transmission_type={t for c in cars for t in c.get("transmissions")}
print(all_transmission_type)


#print all colors
all_colors={cl for c in cars for cl in c.get("colors")}
print(all_colors)


#most popular color
popular_color=[color for c in cars for color in c.get("colors")]
#print(popular_color)
color_count={color:popular_color.count(color) for color in popular_color}
print("most_popular_color=>",max(color_count))


#costly car
costly_car=max(cars,key=lambda d:d.get("price"))
print(costly_car.get("name"))
# max_price=costly_car.get("price")
# costly_cars=[c.get("name") for c in cars if c.get("price")==max_price]
# print(costly_cars)



# #car with minimum cost
min_price_car=min(cars,key=lambda d:d.get("price"))
print(min_price_car.get("name"))
# min_price=costly_car.get("price")
# costly_cars=[c.get("name") for c in cars if c.get("price")==min_price]
# print(costly_cars)



# #sort cars wrt price
sorted_car=sorted(cars,key=lambda d:d.get("price"),reverse=True)  #reverse order
sorted_car_name={c.get("name"):c.get("price") for c in sorted_car} #to print name and price
# sorted_car_name={c.get("name"):[c.get("price"),c.get("brand")] for c in sorted_car}  #to print name price brand use list
print(sorted_car_name)

